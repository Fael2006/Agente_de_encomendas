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