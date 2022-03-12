# -*- coding: utf-8 -*-
import random,json
file = open('slova.json','r',encoding = 'utf-8')
word_rus = json.load(file)
tries = 0
critical_trie = 6
game_mode = int(input('Вы хотите играть с определением слова или наугад? Введите 1, если вы хотите играть с определением и 2, если вы хотите играть без определения'))
if game_mode != 1 and game_mode != 2:
    while game_mode != 1 or game_mode != 2:
        game_mode = int(input('Вам нужно ввести либо 1, либо 2'))
if game_mode == 1:
    temi = ['природа', 'животные', 'профессии', 'части тела', 'виды спорта']
    tema_of_word = input('На какую тему вы хотите слово? Есть варианты: природа, животные, профессии, части тела, виды спорта')
    if tema_of_word not in temi:
        while tema_of_word not in temi:
            tema_of_word = input('Есть варианты: природа, животные, профессии, части тела, виды спорта')
    dict_of_tem = {'природа': '1', 'животные':'2', 'профессии':'3', 'части тела':'4', 'виды спорта':'5'}
    num_tema = dict_of_tem[tema_of_word]
    dict_of_slov = {'1':['дерево', 'цветок','воздух','небо','птица'], '2':['лошадь','корова', 'попугай', 'хомяк','собака'], '3':['повар','архитектор','пожарный', 'судья','доктор'], '4':['рука','голова', 'ноги','живот','спина'],'5': ['баскетбол','футбол','бег','гольф','гимнастика']}
    spisok_po_teme = dict_of_slov[num_tema]
    slovo = random.choice(spisok_po_teme)
    dict_of_znach0 = open('dictik-1.json','r',encoding = 'utf-8')
    dict_of_znach = json.load(dict_of_znach0)
    defenition = dict_of_znach[slovo]
    triess1 = 0
    while triess1 != 3 or s != slovo:
        print(defenition,'у вас', 3-triess1,'попытки')
        s = input()
        if s == slovo:
            print('Вы выиграли')
            break
        else:
            triess1 += 1
            if triess1 == 3:
                print('Вы проиграли,это было слово', slovo)
                break
elif game_mode == 2:
    len_of_word = input('Введите длину загадываемого слова от 3 до 16')
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
        len_of_word = input('Введите длину загадываемого слова от 3 до 16')
    shadow_form_word = '*' * len_of_word
    conceived_word = ' '
    while len(conceived_word) != len_of_word:
        conceived_word = word_rus[random.randint(0, 1000)]
    print('Я загадал слово! Давайте играть! У вас еще ', critical_trie, 'жизней')
    print('Называйте по одной букве, если буква в слове, то вы увидите где')
    for i in range(len_of_word):
        print('*', end=' ')
    guessed_letters = []
    guessed_words = []
    conceived_word = list(conceived_word)
    shadow_form_word = list(shadow_form_word)
    while shadow_form_word != conceived_word or critical_trie == tries:
        letter = input('Введите одну русскую букву')
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
                print('Вы проиграли, это было слово', *conceived_word )
                break
dict_of_znach0.close()
file.close()
