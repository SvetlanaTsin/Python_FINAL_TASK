#ДЛЯ ПОИСКА В МЕНЮ
menu_items = [
    'Главное меню:',
    'Открыть файл',
    'Сохранить файл',
    'Показать все заметки',
    'Добавить заметку',
    'Показать по дате',
    'Редактировать заметку',
    'Удалить заметку',
    'Выход'
]

menu_choice = 'Выберите пункт меню: '
menu_choice_error = f'Введите пункт меню от 1 до {len(menu_items) - 1}'


#ДЛЯ РАБОТЫ С ФАЙЛОМ
load_successful = 'Файл открыт успешно!'
save_successful = 'Файл сохранен успешно!'


#ДЛЯ СОЗДАНИЯ ЗАМЕТОК
create_note = ['Введите заголовок заметки: ',
               'Введите заметку: ']

def add_note_successful(title: str) -> str:
    return f'Заметка "{title}" создана успешно!'


#ДЛЯ ПОИСКА ПО ДАТЕ
empty_dict_note = 'Заметок нет или файл не открыт!'

input_find_date = 'Введите дату для поиска в формате DD/MM/YY: '

def find_by_date_error(date: str) -> str:
    return f'Заметок созданных {date} не найдено!'


#ДЛЯ РЕДАКТИРОВАНИЯ
input_note_id = 'Введите ID заметки, которую хотите отредактировать: '

or_enter = ' или ENTER (оставить без изменений): '
edit_note = ['Введите измененный заголовок заметки' + or_enter,
             'Измените заметку' + or_enter]

def edit_note_successful(title: str) -> str:
    return f'Заметка "{title}" изменена успешно!'

def error_id_note(note_id: str) -> str:
    return f'Заметки с ID {note_id} не существует!'


#ДЛЯ УДАЛЕНИЯ ЗАМЕТОК
delete_note_id = 'Введите ID заметки, которую хотите удалить: '

def delete_note_successful(title: str) -> str:
    return f'Заметка "{title}" удалена успешно!'