import datetime
import json


def create_note():
    note_id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "created_at": created_at
    }

    return note



def save_note(note):
    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write("\n")
    print("Заметка успешно сохранена.")



def read_notes():
    with open("notes.json", "r") as file:
        for line in file:
            note = json.loads(line)
            print("ID:", note["id"])
            print("Заголовок:", note["title"])
            print("Текст:", note["body"])
            print("Дата создания:", note["created_at"])




def edit_note():
    note_id = input("Введите идентификатор заметки, которую хотите отредактировать: ")
    updated_note = create_note()

    with open("notes.json", "r") as file:
        lines = file.readlines()

    with open("notes.json", "w") as file:
        for line in lines:
            note = json.loads(line)
            if note["id"] == note_id:
                json.dump(updated_note, file)
                file.write("\n")
                print("Заметка успешно отредактирована.")
            else:
                json.dump(note, file)
                file.write("\n")



def delete_note():
    note_id = input("Введите идентификатор заметки, которую хотите удалить: ")

    with open("notes.json", "r") as file:
        lines = file.readlines()

    with open("notes.json", "w") as file:
        for line in lines:
            note = json.loads(line)
            if note["id"] != note_id:
                json.dump(note, file)
                file.write("\n")
        print("Заметка успешно удалена.")



def main():
    while True:
        print("1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            note = create_note()
            save_note(note)
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()



