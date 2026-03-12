import requests
from datetime import datetime, timedelta
from app.config import settings
import pytz


_cache_dados = None
_cache_timestamp = None
CACHE_TEMPO_MINUTOS = 5


TECNICOS_PROPRIOS = [
    "Bruno Felipe dos Santos Silva",
    "Thiago de Almeida Deulefeu",
    "Irving Simões Pereira",
    "Bernardo Santos da Cunha",
    "Hugo Cesar dos santos",
    "Michael Gledson Dantas Dias",
    "Rodrigo Pinheiro de Sá",
    "Lucas Roese Bernardo",
    "Marcos José de Oliveira",
    "Alexvan Santos de Oliveira",
    "ADRIANO LUIS VIVAN",
    "Petter Fabio Coutinho da Silva",
    "Luiz Ricardo Monteiro da Silva",
    "Joarez Soares de Oliveira Junior",
    "Walerson dos Santos Ferreira",
]


def normalizar_nome(nome):
    if not nome:
        return None
    return nome.strip().lower()


def organizar_chamados():
    global _cache_dados, _cache_timestamp

    agora = datetime.now()

    if _cache_dados and _cache_timestamp:
        diferenca = agora - _cache_timestamp
        if diferenca < timedelta(minutes=CACHE_TEMPO_MINUTOS):
            print("🟢 Usando cache")
            _cache_dados["fonte"] = "Cache"
            return _cache_dados

    print("🔵 Consultando Jira")

    url = f"{settings.JIRA_BASE_URL}/rest/api/2/search"

    jql = """
    "Agendamento" >= startOfDay()
    AND "Agendamento" <= endOfDay()
    AND "Técnico em campo" is not EMPTY
    AND status IN (
        "A fazer - Monitoramento Projetos",
        "Monitoramento - A fazer"
    )
    ORDER BY "Agendamento" ASC
    """

    auth = (settings.JIRA_EMAIL, settings.JIRA_PASSWORD)

    try:
        response = requests.get(
            url,
            params={
                "jql": jql,
                "fields": [
                    settings.JIRA_AGENDAMENTO_FIELD,
                    "customfield_10623",
                    "customfield_10700",
                    "customfield_15615",
                ],
                "maxResults": 1000,
            },
            auth=auth,
        )

        if response.status_code != 200:
            print("Erro Jira:", response.text)
            return {"total_geral": 0, "tecnicos_ativos": 0, "dados": {}}

        issues = response.json().get("issues", [])

        dados = {tec: [] for tec in TECNICOS_PROPRIOS}
        mapa_tecnicos = {
            normalizar_nome(tec): tec for tec in TECNICOS_PROPRIOS
        }

        for issue in issues:
            fields = issue.get("fields", {})

            tecnico_raw = fields.get("customfield_10623")
            tecnico_normalizado = normalizar_nome(tecnico_raw)

            if tecnico_normalizado in mapa_tecnicos:
                tecnico_real = mapa_tecnicos[tecnico_normalizado]

                agendamento_raw = fields.get(settings.JIRA_AGENDAMENTO_FIELD)

                if agendamento_raw:
                    try:
                        data_obj = datetime.strptime(
                            agendamento_raw,
                            "%Y-%m-%dT%H:%M:%S.%f%z"
                        )

                        fuso_brasil = pytz.timezone("America/Fortaleza")

                        data_local = data_obj.astimezone(fuso_brasil)

                        agendamento_formatado = data_local.strftime("%d/%m %H:%M")

                    except Exception:
                        agendamento_formatado = agendamento_raw
                else:
                    agendamento_formatado = "Sem horário"

                tipo_field = fields.get("customfield_10700")
                if isinstance(tipo_field, dict):
                    tipo = tipo_field.get("value", "Não informado")
                else:
                    tipo = "Não informado"

                cliente_field = fields.get("customfield_15615")
                if isinstance(cliente_field, dict):
                    cliente = cliente_field.get("value", "Não informado")
                else:
                    cliente = cliente_field or "Não informado"

                dados[tecnico_real].append(
                    {
                        "agendamento": agendamento_formatado,
                        "tipo": tipo,
                        "cliente": cliente,
                    }
                )

        dados_filtrados = {k: v for k, v in dados.items() if v}
        total_proprios = sum(len(lista) for lista in dados_filtrados.values())

        resultado = {
            "total_geral": total_proprios,
            "tecnicos_ativos": len(dados_filtrados),
            "dados": dados_filtrados,
            "atualizado_em": agora.strftime("%H:%M:%S"),
            "fonte": "Jira",
        }

        _cache_dados = resultado
        _cache_timestamp = agora

        return resultado

    except Exception as e:
        print("Erro ao consultar Jira:", str(e))
        return {"total_geral": 0, "tecnicos_ativos": 0, "dados": {}}

  