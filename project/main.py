# -*- coding: utf-8 -*-
import telebot
import random, json, constants
from telebot import types

file = open('slova.json', 'r', encoding='utf-8')
word_rus = json.load(file)
file.close()
critical_trie = 6
token = '5188285015:AAEVPBMesbRY4jhnly7d1NRt6mPg0R8Df1U'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item1 = types.KeyboardButton('/1')
    item2 = types.KeyboardButton('/2')

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, Вы хотите играть с определением слова или наугад? Выберите /1, если Вы хотите играть с определением и /2, если Вы хотите играть без определения.".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['1'])
def first(message):
    markup1 = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    item1 = types.KeyboardButton('природа')
    item2 = types.KeyboardButton('животные')
    item3 = types.KeyboardButton('профессии')
    item4 = types.KeyboardButton('части тела')
    item5 = types.KeyboardButton('виды спорта')

    markup1.add(item1, item2, item3, item4, item5)

    msg1 = bot.send_message(
        message.chat.id,
        text='На какую тему Вы хотите слово? Есть варианты: природа, животные, профессии, части тела, виды спорта',
        reply_markup=markup1)

    bot.register_next_step_handler(msg1, opredelenie)


def opredelenie(message):
    global slovo,tries
    dict_of_tem = {'природа': '1', 'животные': '2', 'профессии': '3', 'части тела': '4', 'виды спорта': '5'}
    if message.text in dict_of_tem:
        num_tema = dict_of_tem[message.text]
        dict_of_slov = {'1': ['дерево', 'цветок', 'воздух', 'небо', 'птица'],
                        '2': ['лошадь', 'корова', 'попугай', 'хомяк', 'собака'],
                        '3': ['повар', 'архитектор', 'пожарный', 'судья', 'доктор'],
                        '4': ['рука', 'голова', 'ноги', 'живот', 'спина'],
                        '5': ['баскетбол', 'футбол', 'бег', 'гольф', 'гимнастика']}
        spisok_po_teme = dict_of_slov[num_tema]
        slovo = random.choice(spisok_po_teme)
        dict_of_znach0 = open('dictik-1.json', 'r', encoding='utf-8')
        dict_of_znach = json.load(dict_of_znach0)
        defenition = dict_of_znach[slovo]
        dict_of_znach0.close()
        markup1 = types.ReplyKeyboardRemove(selective=False)
        tries = 3
        msg = bot.send_message(message.chat.id, defenition, parse_mode='html')
        bot.register_next_step_handler(msg, slovoo1)
def slovoo1(s):
    global tries
    if s.text.lower() == slovo.lower():
        bot.send_message(s.chat.id, 'Вы выиграли!')
    else:
        tries -= 1
        if tries == 0:
            bot.send_message(s.chat.id, f'Вы проиграли, это было слово "{slovo}"')
        if tries == 1:
            msg = bot.send_message(s.chat.id, f'Вы не угадали, у Вас еще {tries} попытка')
        if tries != 1 and tries != 0:
            msg = bot.send_message(s.chat.id, f'Вы не угадали, у Вас еще {tries} попытки')
        if tries != 0:
            bot.register_next_step_handler(msg, slovoo1)
@bot.message_handler(commands=['2'])
def gamemode2(message):
    markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item1 = types.KeyboardButton('3')
    item2 = types.KeyboardButton('4')
    item3 = types.KeyboardButton('5')
    item4 = types.KeyboardButton('6')
    item5 = types.KeyboardButton('7')
    item6 = types.KeyboardButton('8')
    item7 = types.KeyboardButton('9')
    item8 = types.KeyboardButton('10')
    item9 = types.KeyboardButton('11')
    item10 = types.KeyboardButton('12')
    item11 = types.KeyboardButton('13')
    item12 = types.KeyboardButton('14')
    item13 = types.KeyboardButton('15')
    item14 = types.KeyboardButton('16')
    item15 = types.KeyboardButton('17')

    markup2.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14,
                item15)
    msg = bot.send_message(message.chat.id, 'Выберите длину загадываемого слова',
                   parse_mode='html', reply_markup=markup2)
    bot.register_next_step_handler(msg, lening)
def lening(message):
    global conceived_word, shadow_form_word, str_conceived_word, critical_trie
    markup2 = types.ReplyKeyboardRemove(selective=False)
    shadow_form_word = '*' * int(message.text)
    conceived_word = ' '
    while len(conceived_word) != int(message.text):
        conceived_word = word_rus[random.randint(0, 1000)]
    str_conceived_word = ''
    len_of_word = len(conceived_word)
    critical_trie = 10
    if 12 > len_of_word >= 8:
        critical_trie = 7
    if 14 > len_of_word >= 12:
        critical_trie = 8
    if 16 > len_of_word >= 14:
        critical_trie = 9
    if len_of_word == 16:
        critical_trie = 10
    bot.send_message(message.chat.id, f'Я загадал слово! Давайте играть! У Вас еще {critical_trie} жизней')
    bot.send_message(message.chat.id, f'Называйте по одной букве, если буква в слове, то вы увидите где')
    msg = bot.send_message(message.chat.id, '*' * int(message.text))
    guessed_letters = []
    guessed_words = []
    conceived_word = list(conceived_word)
    for i in range(len(conceived_word)):
        str_conceived_word += conceived_word[i]
    shadow_form_word = list(shadow_form_word)
    bot.register_next_step_handler(msg, gm21)
def gm21(message):
    global critical_trie
    if message.text in conceived_word:
        for j in range(len(conceived_word)):
            if conceived_word[j].lower() == message.text.lower():
                shadow_form_word[j] = message.text
        bot.send_message(message.chat.id, ''.join(shadow_form_word))
        if shadow_form_word == conceived_word:
            bot.send_message(message.chat.id, 'Ура! Вы выиграли!')
        msg = bot.send_message(message.chat.id,'Вводите')
        bot.register_next_step_handler(msg,gm21)
    else:
        critical_trie -= 1
        bot.send_message(message.chat.id, f'У вас осталось {critical_trie} жизней')
        if critical_trie != 0:
            msg = bot.send_message(message.chat.id,'Вводите')
            bot.register_next_step_handler(msg, gm21)
        else:
            bot.send_message(message.chat.id, f'Вы проиграли, это было слово "{str_conceived_word}"')
bot.polling(none_stop=True)
