#!/usr/bin/python
# -*- coding: utf-8 -*-

# Библиотека функций, используемых для зашифровки / дешифровки кода Виженера.

# данный алгоритм способен зашифровать произвольные текст, но он зашифровыает только символы, которые есть
# в его алфавите (см. функцию form_alph()). Прочие символы он записывает без зашифровки. Дешифрует аналогично


# Функция form_alph требуется для формирования алфавита символов (те символы, которые 
# будет шифровать функция enchipher и дешифровать функция dechipher.

# создается список с символами, для проверки в функциях шифровки и дешифровки (есть ли символ в алфавите)
def form_alph():
    alph = []
    for i in range(1040, 1104): # перебор кодов символов от А до я (оба регистра); 1040 - А, 1104 - я
        alph.append(chr(i))        # добавление символа в конец списка
    return alph


# функция шифровки текста
# принимает на вход простой текст (text) и ключ (key), возвращает зашифрованный по ключу текст
def enchipher(text, key):
    enchipher_text = ''
    alph = form_alph()
    i = 0
    for sym in text:
        # если символ есть в алфавите - шифруем по Виженеру
        if sym in alph:
            en_sym = ((ord(sym) + ord(key[i % len(key)]) - 2080)) % 64 + 1040 # изменение кода символа по формуле
            en_sym = chr(en_sym)
            i += 1
        # иначе записываем символ без изменений
        else:
            en_sym = sym
        # вносим символ в зашифрованный текст
        enchipher_text += en_sym
    return enchipher_text


# функция дешифровки
# принимает на вход зашифрованный текст (text) и ключ (key), возвращает дешифрованный по ключу текст
def dechipher(text, key):
    dechipher_text = ''
    alph = form_alph()
    i = 0
    for sym in text:
        # если символ есть в алфавите - дешифруем по Виженеру
        if sym in alph:
            de_sym = ((ord(sym) - ord(key[i % len(key)]) + 64)) % 64 + 1040 # изменение кода символа по формуле
            de_sym = chr(de_sym)
            i += 1
        # иначе записываем символ без изменений
        else:
            de_sym = sym
        dechipher_text += de_sym
    return dechipher_text


# две следующие функции (import_file и write_file) нужны лишь для более простой организации ввода-вывода в файл.
# в самом шифровании они не принимают никакого участия

# открывает файл
def import_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


# записывает файл
def write_file(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)


# пример работы алгоритма: шифрует и дешифрует фразу "Привет, мир!" по ключу "ключ"
if __name__ == "__main__":
    text = 'Привет, мир!'
    key = 'ключ'
    chipher_text = enchipher(text, key)
    print(chipher_text)
    print(dechipher(chipher_text, key))
