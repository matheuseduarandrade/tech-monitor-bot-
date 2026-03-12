from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def teclado_chamados_do_dia(dados):
    markup = InlineKeyboardMarkup()

    for tecnico, chamados in dados.items():
        markup.add(
            InlineKeyboardButton(
                f"👷 {tecnico} ({len(chamados)})",
                callback_data=f"tecnico|{tecnico}"
            )
        )

    return markup
