from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_menu_handler(bot):

    @bot.message_handler(func=lambda msg: msg.text == "📅 Chamados do Dia")
    def chamados_do_dia(message):
        mostrar_menu_chamados(bot, message.chat.id)


def mostrar_menu_chamados(bot, chat_id, message_id=None):

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("👷 Técnicos Próprios", callback_data="proprios")
    )
    markup.add(
        InlineKeyboardButton("🤝 Técnicos Terceiros", callback_data="terceiros")
    )
    markup.add(
        InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_inicio")
    )

    if message_id:
        bot.edit_message_text(
            "📅 *Chamados do Dia*\n\nSelecione o tipo de técnico:",
            chat_id,
            message_id,
            reply_markup=markup,
            parse_mode="Markdown"
        )
    else:
        bot.send_message(
            chat_id,
            "📅 *Chamados do Dia*\n\nSelecione o tipo de técnico:",
            reply_markup=markup,
            parse_mode="Markdown"
        )
