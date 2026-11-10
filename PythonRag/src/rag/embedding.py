
from google import genai
client = genai.Client()

def criar_embedings(conteudo):
    resposta = client.models.embed_content(
        model="gemini-embedding-2",
        contents=conteudo
    )
    return resposta.embeddings[0].values