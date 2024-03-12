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
            
            case 5:
                find_date = view.input_data(text.input_find_date)
                result = model.find_note_by_date(find_date)
                view.show_notes(result, text.find_by_date_error(find_date))

            case 6:
                edit_note_id = view.input_data(text.input_note_id)
                if edit_note_id in model.dict_note:  #если этот id существует в нашем словаре, где все заметки
                    edited_note = view.input_note(text.edit_note)
                    new_title = model.edit_note(edit_note_id, edited_note)
                    view.show_message(text.edit_note_successful(new_title))
                else:
                    view.show_message(text.error_id_note(edit_note_id))

            case 7:
                delete_note_id = view.input_data(text.delete_note_id)
                if delete_note_id in model.dict_note:
                    deleted_title = model.delete_note(delete_note_id)
                    view.show_message(text.delete_note_successful(deleted_title))
                else:
                    view.show_message(text.error_id_note(delete_note_id))
            case 8:
                break