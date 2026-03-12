from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.handlers.menu_handler import mostrar_menu_chamados

def register_tecnicos_handler(bot):

    @bot.callback_query_handler(func=lambda call: call.data == "voltar_inicio")
    def voltar_inicio(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)

    @bot.callback_query_handler(func=lambda call: call.data == "proprios")
    def tecnicos_proprios(call):

        tecnicos = {
            "Gabriel": 12,
            "Marcos": 8,
            "Luis": 5
        }

        markup = InlineKeyboardMarkup()

        for nome, total in tecnicos.items():
            markup.add(
                InlineKeyboardButton(
                    f"👷 {nome} ({total})",
                    callback_data=f"tecnico_{nome}"
                )
            )

        markup.add(
            InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_chamados")
        )

        bot.edit_message_text(
            "👷 *Técnicos Próprios*\n\nSelecione o técnico:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup,
            parse_mode="Markdown"
        )


    @bot.callback_query_handler(func=lambda call: call.data == "terceiros")
    def tecnicos_terceiros(call):

        tecnicos = {
            "Carlos Terceiro": 6,
            "João Terceiro": 4
        }

        markup = InlineKeyboardMarkup()

        for nome, total in tecnicos.items():
            markup.add(
                InlineKeyboardButton(
                    f"🤝 {nome} ({total})",
                    callback_data=f"tecnico_{nome}"
                )
            )

        markup.add(
            InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_chamados")
        )

        bot.edit_message_text(
            "🤝 *Técnicos Terceiros*\n\nSelecione o técnico:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup,
            parse_mode="Markdown"
        )


    @bot.callback_query_handler(func=lambda call: call.data == "voltar_chamados")
    def voltar_chamados(call):
        mostrar_menu_chamados(
            bot,
            call.message.chat.id,
            call.message.message_id
        )

