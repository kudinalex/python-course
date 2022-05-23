import telebot, random
token='5387244419:AAHaQZqRDnPdU9qo4zy3CKzgeefZT09qIfw'
bot = telebot.TeleBot(token)
global spisok
spisok = []
@bot.message_handler(commands=['start'])
def hello(message):
    msg = bot.send_message(message.chat.id,'Вводите')
    spisok.append(msg.text)
    if msg.text != '/go':
        bot.register_next_step_handler(msg, hello)
@bot.message_handler(commands=['go'])
def opros(message):
    msg = bot.send_message(message.chat.id,random.choice(spisok))
    bot.register_next_step_handler(msg, opros)
bot.polling(none_stop=True)