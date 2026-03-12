from telebot import TeleBot
from app.config import settings

from app.handlers.start_handler import register_start_handler
from app.handlers.chamados_handler import register_chamados_handler
from app.services.scheduler_service import start_scheduler
from app.services.disparador_service import iniciar_agendador


def main():
    bot = TeleBot(settings.BOT_TOKEN)

    register_start_handler(bot)
    
    register_chamados_handler(bot)

    start_scheduler(bot)

    iniciar_agendador(bot)

    print("🤖 Bot Técnicos iniciado...")
    bot.infinity_polling()


if __name__ == "__main__":
    main()