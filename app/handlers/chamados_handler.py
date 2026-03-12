from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.services.jira_service import organizar_chamados
from app.keyboards.chamados_keyboard import teclado_chamados_do_dia


cache_chamados = None


def register_chamados_handler(bot):

    # ================================
    # 📅 ABRIR RESUMO
    # ================================
    @bot.message_handler(func=lambda msg: msg.text == "📅 Chamados do Dia")
    def abrir_resumo(message):
        global cache_chamados

        cache_chamados = organizar_chamados()

        total_geral = cache_chamados["total_geral"]
        tecnicos_ativos = cache_chamados["tecnicos_ativos"]
        dados = cache_chamados["dados"]
        atualizado_em = cache_chamados.get("atualizado_em", "--:--")
        fonte = cache_chamados.get("fonte", "Desconhecida")

        texto = (
            "📋 *Chamados do Dia*\n\n"
            f"Total geral hoje: {total_geral}\n"
            f"Técnicos ativos: {tecnicos_ativos}\n\n"
            f"🕒 Atualizado às {atualizado_em}\n"
            f"📡 Fonte: {fonte}\n\n"
            "Selecione um técnico:"
        )

        bot.send_message(
            message.chat.id,
            texto,
            reply_markup=teclado_chamados_do_dia(dados),
            parse_mode="Markdown"
        )

    # ================================
    # 👷 MOSTRAR TÉCNICO
    # ================================
    @bot.callback_query_handler(func=lambda call: call.data.startswith("tecnico|"))
    def mostrar_tecnico(call):
        global cache_chamados

        if not cache_chamados:
            bot.answer_callback_query(call.id, "Dados expirados. Clique novamente em Chamados do Dia.")
            return

        tecnico = call.data.split("|")[1]
        chamados = cache_chamados["dados"].get(tecnico, [])

        texto = f"👷 *{tecnico}*\n\n"
        texto += f"Chamados hoje: {len(chamados)}\n\n"

        for i, chamado in enumerate(chamados, start=1):
            texto += (
                f"{i}️⃣ {chamado['agendamento']}\n"
                f"Tipo: {chamado['tipo']}\n"
                f"Cliente: {chamado['cliente']}\n\n"
            )

        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("⬅ Voltar", callback_data="voltar_resumo")
        )

        bot.edit_message_text(
            texto,
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup,
            parse_mode="Markdown"
        )

    # ================================
    # ⬅ VOLTAR PARA RESUMO
    # ================================
    @bot.callback_query_handler(func=lambda call: call.data == "voltar_resumo")
    def voltar_resumo(call):
        global cache_chamados

        if not cache_chamados:
            bot.answer_callback_query(call.id, "Dados expirados. Clique novamente em Chamados do Dia.")
            return

        total_geral = cache_chamados["total_geral"]
        tecnicos_ativos = cache_chamados["tecnicos_ativos"]
        dados = cache_chamados["dados"]
        atualizado_em = cache_chamados.get("atualizado_em", "--:--")
        fonte = cache_chamados.get("fonte", "Desconhecida")

        texto = (
            "📋 *Chamados do Dia*\n\n"
            f"Total geral hoje: {total_geral}\n"
            f"Técnicos ativos: {tecnicos_ativos}\n\n"
            f"🕒 Atualizado às {atualizado_em}\n"
            f"📡 Fonte: {fonte}\n\n"
            "Selecione um técnico:"
        )

        bot.edit_message_text(
            texto,
            call.message.chat.id,
            call.message.message_id,
            reply_markup=teclado_chamados_do_dia(dados),
            parse_mode="Markdown"
        )
