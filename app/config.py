import os
from dotenv import load_dotenv

load_dotenv()

TECNICOS_TELEGRAM = {
    "Bruno Felipe dos Santos Silva": 1975250571,
    "Thiago de Almeida Deulefeu": 5607578205,
    "Irving Simões Pereira": 6580432806,
    "Bernardo Santos da Cunha": 984543528,
    "Hugo Cesar dos santos": 5950455869,
    "Michael Gledson Dantas Dias": 6133776497,
    "Rodrigo Pinheiro de Sá": 749922700,
    "Lucas Roese Bernardo": 7975779512,
    "Marcos José de Oliveira": 6844538318,
    "Alexvan Santos de Oliveira": 5954233191,
    "ADRIANO LUIS VIVAN": 6762356130,
    "Petter Fabio Coutinho da Silva": 6602704540,
    "Luiz Ricardo Monteiro da Silva": 6871546168,
    "Joarez Soares de Oliveira Junior": 7329891276,
    "Walerson dos Santos Ferreira": 6582128768,
    "Eujanio Nascimento": 8673773591,
}
class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
    JIRA_EMAIL = os.getenv("JIRA_EMAIL")
    JIRA_PASSWORD = os.getenv("JIRA_PASSWORD")
    JIRA_AGENDAMENTO_FIELD = os.getenv("JIRA_AGENDAMENTO_FIELD")



settings = Settings()
