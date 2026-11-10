from src.rag.chunker import dividir_texto
from src.rag.embedding import criar_embedings
from src.rag.leitor import ler_arquivo
from src.rag.retriever import buscar_melhores_chunks

from pathlib import Path


def fazer_cosulta(pergunta = str):
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

        vetor_pergunta = criar_embedings(pergunta)

        melhores = buscar_melhores_chunks(vetor_pergunta,documentos,chunks)

        contexto_recuperado = "\n---\n".join([item[1] for item in melhores])

        return contexto_recuperado