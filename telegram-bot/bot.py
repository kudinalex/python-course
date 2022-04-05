import telebot
token = '5188285015:AAEVPBMesbRY4jhnly7d1NRt6mPg0R8Df1U'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')
bot.polling(none_stop=True)