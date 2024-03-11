import text
import view
import model

def start_app():
    while True:
       user_choice = view.main_menu()
       match user_choice:
            case 1:
                model.open_file()
                view.show_message(text.load_successful)
            case 2:
                model.save_file()
                view.show_message(text.save_successful)
            case 3:
               view.show_notes(model.dict_note, text.empty_dict_note)  
            case 4:
                note = view.input_note(text.create_note)
                model.add_note(note)
                view.show_message(text.add_note_successful(note['title'])) #выводим сообщение об успешном добавлении заметки и динамически выводим ее название 