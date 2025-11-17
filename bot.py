import telebot
import time
import os

TOKEN = os.getenv("TOKEN")  # Railway वरील token

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    chat_id = message.chat.id
    message_id = message.message_id
    
    time.sleep(4 * 60 * 60)  # 4 तास

    try:
        bot.delete_message(chat_id, message_id)
    except:
        pass

bot.infinity_polling()
