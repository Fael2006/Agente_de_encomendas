import numpy as np

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