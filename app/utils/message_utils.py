def send_large_message(bot, chat_id, text, parse_mode="Markdown"):
    max_length = 3500  
    
    for i in range(0, len(text), max_length):
        bot.send_message(
            chat_id,
            text[i:i + max_length],
            parse_mode=parse_mode
        )
