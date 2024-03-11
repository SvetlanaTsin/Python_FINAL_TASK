import text
from datetime import datetime

def main_menu():
    for i, item in enumerate(text.menu_items):
        print(f'\t{i}. {item}' if i else item) #печатаем отступ, номер и пункт меню, если i (i!=0), иначе только пункт. Т.о.пункт Главное меню печатаем без отступа и номера
    while True:
        user_choice = input(text.menu_choice)
        if user_choice.isdigit() and 0 < int(user_choice) < len(text.menu_items):
            return int(user_choice)
        print(text.menu_choice_error)


def show_message(message: str):
    print('\n' + '=' * len(message)) #печатаем отступ, затем строчку из = (умножаем = на длину сообщения)
    print(message)
    print('=' * len(message) + '\n')


def input_note(message: list[str]) -> dict[str, str]:
    timestamp = datetime.now().strftime("%d/%m/%y %I:%M") #применяем функцию datetime сейчас и задаем формат даты и времени 
    data = [input(item) for item in message] #вводим данные в виде списка, где 0 элемент - это заголовок, 1 элемент - это заметка; список задан сообщением create_note
    return {'title': data[0], 'note': data[1], 'timestamp': timestamp}  #возвращаем данные в виде словаря: ключи - title, note, timestamp, а в элементы передаем значения из введенного списка плюс дата/время


def show_notes(dict_note: dict, error_message: str):
    if dict_note:
        print()
        for note_id, note in dict_note.items(): #в словаре dict_note содержатся id, титулы, заметки, таймстемп
            note_list = []
            for item in note.values():
                note_list.append(item) #все элементы из словаря добавляются в список note_list
            print(f'#{note_id} | {note_list[-1]}\nТема: {note_list[0]}\n{note_list[1]}\n') #печатаем id, посл элемент списка - это таймстемп, затем 0 элемент списка - титул, затем 1 элемент списка - заметку
             
    else:
        show_message(error_message)