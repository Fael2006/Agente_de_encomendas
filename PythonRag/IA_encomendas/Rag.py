from pathlib import Path
import numpy as np
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()


client = genai.Client()



def criar_embedings(conteudo):
    resposta = client.models.embed_content(
        model="gemini-embedding-2",
        contents=conteudo
    )
    return resposta.embeddings[0].values


#LER UM DOCUMENTO
def ler_arquivo(caminho):
    return Path(caminho).read_text(
        encoding="utf-8"
    )

texto = ler_arquivo("Documentos/arquivo.txt")






#DIVIDIR EM CHUNKS
def dividir_texto(texto,tamanho=300, overlap=50):
    chunks= []
    inicio= 0

    while inicio < len(texto):
        fim= inicio + tamanho

        chunk = texto[inicio:fim]
        chunks.append(chunk)

        inicio += tamanho - overlap 
    return chunks







def similaridade_cosseno(vetor_a, vetor_b):
    a = np.array(vetor_a)
    b = np.array(vetor_b)

    return np.dot(a,b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

def buscar_melhores_chunks(
        vetor_pergunta,
        vetor_documento,
        chunks,
        top_k=3
        ):
    resultado = []

    for i, vetor in enumerate(vetor_documento):
        score = similaridade_cosseno(
            vetor_pergunta,
            vetor
        )

        resultado.append((score, chunks[i]))

    resultado.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return resultado[:top_k]






def salvar_base(registros, caminho="base.json"):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            registros,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

registro = {
    "id":"chunk_001",
    "texto":"A empresa oferece 30 de ferias",
    "embedings": [0.21, 0.85, 0.13],
    "documento": "politica_RH.pdf"
}








def gerar_resposta(contexto, pergunta):

    prompt = f"""
        voce e um agente respostavel por responder informaçeos que voce achar nos contextos, sempre verifique a sua base de informaçeos ou seja o contexto

        REGRAS:
        1. nao invente informaçoes 
        2. use somente o contexto

        Contexto para ser ultilizado:
        {contexto}
        Pergunta para responder:
        {pergunta}

    """
    resposta = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return resposta.text

caminho_doc = Path("Documentos/arquivo.txt")
caminho_doc.parent.mkdir(parents=True,exist_ok=True)

if not caminho_doc.exists():
    caminho_doc.write_text(
            "A política interna da empresa estabelece que todos os colaboradores têm direito a 30 dias de férias por ano "
            "após completar 12 meses de trabalho. O horário comercial é das 9h às 18h.",
            encoding="utf-8"
        
    )

texto = ler_arquivo(caminho_doc)
chunks = dividir_texto(texto)

documentos = [criar_embedings(chunk) for chunk in chunks]

registro = [
    {"id":f"chunk_{i:03d}", "texto":chunk, "embeddings": vetor}
    for i, (chunk, vetor) in enumerate(zip(chunks,documentos)) 
]
salvar_base(registro) 

pergunta = "me dig oque é Redução da Mobilização do Solo" 
print(pergunta)

vetor_pergunta = criar_embedings(pergunta)
melhores = buscar_melhores_chunks(vetor_pergunta,documentos,chunks)

contexto_recuperado = "\n---\n".join([item[1] for item in melhores])

reposta_certa = gerar_resposta(contexto=contexto_recuperado, pergunta=pergunta)

print(reposta_certa)