from google.adk.agents.llm_agent import Agent
from src.tools.consulta import fazer_cosulta
from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    name="Suporte_encomendas",
    model="gemini-3.6-flash",
    description="voce e um agente especialista em suporte de encomendas",
    instruction="""Voce deve agir com respeito e cordialidade,
    
    Regra 1: nunca criar chamados que nao existem
    Regra 2: nao crie informaçoes 
    Regra 3: use os dados do contexto que voce achar 
    """,
    tools=[fazer_cosulta]
)