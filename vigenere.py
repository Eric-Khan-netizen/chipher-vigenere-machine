#!/usr/bin/python
# -*- coding: utf-8 -*-


# формирование алфавита
# создается список с символами, для проверки в функциях шифровки и дешифровки (есть ли символ в алфавите)
def form_alph():
    d = []
    for i in range(1040, 1104):
        d.append(chr(i))
    return d


# функция зашифровки
def enchipher(text, key):
    enchipher_text = ''
    alph = form_alph()
    i = 0
    for sym in text:
        # если символ есть в алфавите - шифруем по Виженеру
        if sym in alph:
            en_sym = ((ord(sym) + ord(key[i % len(key)]) - 2080)) % 64 + 1040
            en_sym = chr(en_sym)
            i += 1
        # иначе записываем символ без изменений
        else:
            en_sym = sym
        # вносим символ в зашифрованный текст
        enchipher_text += en_sym
    return enchipher_text


def dechipher(text, key):
    dechipher_text = ''
    alph = form_alph()
    i = 0
    for sym in text:
        # если символ есть в алфавите - дешифруем по Виженеру
        if sym in alph:
            de_sym = ((ord(sym) - ord(key[i % len(key)]) + 64)) % 64 + 1040
            de_sym = chr(de_sym)
            i += 1
        # иначе записываем символ без изменений
        else:
            de_sym = sym
        dechipher_text += de_sym
    return dechipher_text


# открывает файл
def import_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


# записывает файл
def write_file(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)
