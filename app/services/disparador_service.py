from apscheduler.schedulers.background import BackgroundScheduler
from app.services.jira_service import organizar_chamados
from app.config import TECNICOS_TELEGRAM


def iniciar_agendador(bot):
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        func=lambda: disparar_chamados(bot),
        trigger="cron",
        hour=9,
        minute=10
    )

    scheduler.start()


def disparar_chamados(bot):
    print("⏰ Iniciando disparo automático...")

    dados = organizar_chamados()

    for tecnico, chamados in dados["dados"].items():

        chat_id = TECNICOS_TELEGRAM.get(tecnico)

        if not chat_id:
            continue

        if not chamados:
            mensagem = (
                f"👷 Bom dia, {tecnico}!\n\n"
                "✅ Você não possui chamados agendados para hoje."
            )
        else:
            mensagem = f"👷 Bom dia, {tecnico}!\n\n"
            mensagem += f"📋 Você possui {len(chamados)} chamados hoje:\n\n"

            for i, chamado in enumerate(chamados, start=1):
                mensagem += (
                    f"{i}. {chamado['agendamento']}\n"
                    f"Tipo: {chamado['tipo']}\n"
                    f"Cliente: {chamado['cliente']}\n\n"
                )

        bot.send_message(chat_id, mensagem)

    print("✅ Disparo finalizado.")