# Assistente de Encomendas com RAG

Projeto de estudo que combina um agente criado com Google ADK e uma busca RAG (Retrieval-Augmented Generation). O agente consulta um documento local, recupera os trechos mais relacionados à pergunta e os usa como contexto para responder.

## Como funciona

1. O texto em `Documentos/arquivo.txt` é dividido em trechos.
2. A API Gemini gera embeddings para os trechos e para a pergunta.
3. O projeto compara os vetores usando similaridade de cosseno e seleciona os trechos mais relevantes.
4. O agente recebe o contexto recuperado para responder.

## Estrutura

```text
PythonRag/
├── Documentos/
│   └── arquivo.txt          # Documento consultado pelo RAG
├── src/
│   ├── assistente/
│   │   └── agent.py         # Agente principal do Google ADK
│   ├── rag/
│   │   ├── chunker.py       # Divisão do texto em trechos
│   │   ├── embedding.py     # Geração de embeddings
│   │   ├── leitor.py        # Leitura do documento
│   │   └── retriever.py     # Busca por similaridade
│   └── tools/
│       └── consulta.py      # Ferramenta de consulta RAG
└── IA_encomendas/
    └── Rag.py               # Experimento independente com o fluxo RAG
