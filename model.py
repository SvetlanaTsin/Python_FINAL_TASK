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


def _next_id(): #добавление подчерк в начале имени функции обозначает, что эта функция работает только в этом модуле
    global dict_note
    return max(map(int, dict_note)) + 1

def add_note(note: dict):
    global dict_note
    if dict_note:
        dict_note[_next_id()] = note #если словарь с заметками не пустой, то новая заметка - это элемент словаря со следующим id 
    else:
        dict_note[1] = note #если словарь пустой,то записывается заметка с id 1


def find_note_by_date(data_date: str) -> dict:
    global dict_note
    result = {}
    current_date = '/'.join([item.zfill(2) for item in data_date.split('/')])
    for note_id, note in dict_note.items():
        if current_date == note['timestamp'].split()[0]: #если введенная дата совпадает с ключом таймстемп в заметке
            result[note_id] = note #в словарь результат добавляется эта заметка и ей присваивается этот id
    return result


def edit_note(note_id: str, note: dict) -> str:
    global dict_note
    current_note = dict_note[note_id] #берем заметку с тем id, который ввел пользователь - это текущая заметка
    for key in ['title', 'note']: #проходим по ключам титул и заметка
        current_note[key] = note[key] if note[key] else current_note[key] #в текущее значение каждого ключа записываем значение из первоначальной заметки, если оно есть (нажат enter), либо новое значение (в ключ титул записываем старый или новый титул, в ключ заметка записываем старую или новую заметку) 
    dict_note[note_id] = current_note #текущую заметку сохраняем в общий словарь заметок, с тем же id
    return current_note['title'] #возвращаем название измененной заметки


def delete_note(note_id: str) -> str:
    global dict_note
    return dict_note.pop(note_id)['title'] #при удалении id удаляется вся заметка, но мы возвращаем титул по ключу титул, чтобы использовать его в сообщении пользователю
