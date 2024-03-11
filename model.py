from datetime import datetime
import json
import os

dict_note = {} #создаем словарь, где будем хранить заметки во время работы с файлом
path = 'notes.json'

def open_file():
    global dict_note  #благодаря global можем брать переменную извне функции
    if os.path.exists(path):  #если файл существует
        with open(path, 'r', encoding='UTF-8') as json_file:
            dict_note = json.load(json_file)


def save_file():
    global dict_note
    with open(path, 'w', encoding='UTF-8') as json_file:
        json.dump(dict_note, json_file, indent=4, ensure_ascii=False)  #indent определеяет отступы, ensure_ascii=False позволяет вывести кириллицу


def _next_id():
    global dict_note
    return max(map(int, dict_note)) + 1

def add_note(note: dict):
    global dict_note
    if dict_note:
        dict_note[_next_id()] = note #если словарь с заметками не пустой, то новая заметка - это элемент словаря со следующим id 
    else:
        dict_note[1] = note #если словарь пустой,то записывается заметка с id 1