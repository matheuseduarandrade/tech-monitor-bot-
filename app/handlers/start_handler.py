from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def register_start_handler(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("📅 Chamados do Dia"))

        bot.send_message(
            message.chat.id,
            "Bem-vindo ao Bot de Atendimento Técnico 👷‍♂️",
            reply_markup=markup
        )
