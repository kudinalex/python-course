# -*- coding: utf-8 -*-
import telebot
import random, json, constants
from telebot import types

file = open('slova.json', 'r', encoding='utf-8')
word_rus = json.load(file)
tries = 0
critical_trie = 6
token = '5188285015:AAEVPBMesbRY4jhnly7d1NRt6mPg0R8Df1U'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, ты хочешь играть с определением слова или наугад? Выбери 1, если ты хочешь играть с определением и 2, если ты хочешь играть без определения.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def game_select(message):
    if message.chat.type == 'private':
        if message.text == 1:
            temi = ['природа', 'животные', 'профессии', 'части тела', 'виды спорта']
            bot.send_message(message.chat.id,
                             'На какую тему ты хочешь слово? Есть варианты: природа, животные, профессии, части тела, виды спорта')

            @bot.message_handler(content_types=['text'])
            def slovo_po_teme(message):
                dict_of_tem = {'природа': '1', 'животные': '2', 'профессии': '3', 'части тела': '4', 'виды спорта': '5'}
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
                triess1 = 0
                while triess1 != 3 or s != slovo:
                    ostatok = 3 - triess1
                    bot.send_message(message.chat.id,f'{defenition}, у вас, {ostatok} попытки')
                    s = input()
                    if s == slovo:
                        bot.send_message(message.chat.id,'Вы выиграли')
                        break
                    else:
                        triess1 += 1
                        if triess1 == 3:
                            bot.send_message(message.chat.id,f'Вы проиграли,это было слово {slovo}')
                            break
    elif game_mode == 2:
        len_of_word = input(GAME_START_LEN_OF_WORD)
        lens = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        len_of_word = int(len_of_word)
        if 12 > len_of_word >= 8:
            critical_trie = 7
        if 14 > len_of_word >= 12:
            critical_trie = 8
        if 16 > len_of_word >= 14:
            critical_trie = 9
        if len_of_word == 16:
            critical_trie = 10
        while len_of_word not in lens:
            print('Не подходит!')
            len_of_word = input(GAME_START_LEN_OF_WORD)
        shadow_form_word = '*' * len_of_word
        conceived_word = ' '
        while len(conceived_word) != len_of_word:
            conceived_word = word_rus[random.randint(0, 1000)]
        print('Я загадал слово! Давайте играть! У Вас еще ', critical_trie, 'жизней')
        print('Называйте по одной букве, если буква в слове, то вы увидите где')
        for i in range(len_of_word):
            print('*', end=' ')
        guessed_letters = []
        guessed_words = []
        conceived_word = list(conceived_word)
        shadow_form_word = list(shadow_form_word)
        while shadow_form_word != conceived_word or critical_trie == tries:
            letter = input(GAME_INPUT_ONE_LETTER)
            if letter in conceived_word:
                for j in range(len(conceived_word)):
                    if conceived_word[j] == letter:
                        shadow_form_word[j] = letter
                print(*shadow_form_word)
                if shadow_form_word == conceived_word:
                    print('Вы выиграли!')
                    break
            else:
                tries += 1
                print('Вы не угадали, у вас осталось', critical_trie - tries, 'жизней')
                if critical_trie == tries:
                    print('Вы проиграли, это было слово', *conceived_word)
                    break


dict_of_znach0.close()
file.close()
bot.polling(none_stop=True)
