import os.path

FILE_NAME = 'Note.txt'
ID = 'ID'
TITLE_NOTE = 'Заголовок заметки'
MESSAGE_NOTE = 'Сообщение заметки'
DATE_NOTE = 'Дата заметки'
HEADERS = [ID, DATE_NOTE, TITLE_NOTE, MESSAGE_NOTE]
ANSWER = {'y', 'yes,' 'да'}



def load_date():
    '''МЕТОД ПО ЗАГРУЗКЕ ДАННЫХ ИЗ ФАЙЛ, ЕСЛИ ФАЙЛА НЕТ, ТО ОН ЕГО ПРОСТО СОЗДАСТ'''
    check_file = os.path.exists('Note.txt')
    date = []
    if(check_file):
        with open(FILE_NAME, 'r', encoding = 'utf-8') as file:
            for i, line in enumerate(file, start = 1):
                row = [i] + line.strip().split(";")
                date.append(dict(zip(HEADERS, row)))

        return date

    else:
        file = open(FILE_NAME, 'a+', encoding = 'utf-8')
        file.close()
        print("\n\tФайла не было, создали файл, можете его заполнять")
        return date



def print_date(date):
    '''МЕТОД ПО ВЫВОДУ ВСЕХ ЗАМЕТОК НА ЭКРАН'''
    for item in date:
        print(*(f"{k}: {v:<16}" for k, v in item.items()))


def print_note_by_date(date):
    '''МЕТОД ПО ВЫВОДУ ЗАМЕТОК ЧЕРЕЗ ДАТУ'''
    date_user = input('Введите дату, по которой хотите увидеть заметки: ')
    date_user.strip().capitalize()
    for item in date:
        if item[DATE_NOTE] == date_user:
            print(*(f"{k}: {v:<16}" for k, v in item.items()))
        else:
            print("Заметка не принадлежит этой дате, смотрим следующую")



def add_new_note(date):
    '''МЕТОД ПО ДОБАВЛЕНИЮ НОВОЙ ЗАМЕТКИ В ПАМЯТЬ И АВТОМАТИЧЕСКОЕ ЕЕ СОХРАНЕНИЕ В ФАЙЛ'''

    row = input('Введите дату заметки, название заметки и сам текст заметки через (;) : ').split(";")
    line = [len(date) + 1] + [item.strip().capitalize() for item in row]
    date.append(dict(zip(HEADERS, line)))
    print("Новая заметка добавлена")

    with open(FILE_NAME, 'a+', encoding = 'utf-8') as file:
        file.write('; '.join(f"{v}" for k, v in date[len(date) - 1].items() if k != ID) + "\n")
        print("Файл обновлен и в него добавлены новые заметки")


def edit_text_note(title_old_message: str, date):
    '''МЕТОД ПО ИЗМЕНЕНИЮ ЗАМЕТКИ И АВТОМАТИЧЕСКОЕ ПЕРЕСОХРАНЕНИЕ В ФАЙЛ'''
    new_message = input("Введите новый текст для заметки: ")
    new_message.strip().capitalize()
    for item in date:
        if item[TITLE_NOTE] == title_old_message:
            item[MESSAGE_NOTE] = new_message
            print("Замена заметки прошла успешно")
            print(*(f"{k}: {v:<16}" for k, v in item.items()))

            with open(FILE_NAME, 'w', encoding='utf-8') as file:
                for note in date:
                    for k, v in note.items():
                        if k != ID:
                            file.write(f"{v}; ")
                    file.write("\n")
                print("Файл обновлен")

    # Выводим все строки после изменения
    for note in date:
        print(*(f"{k}: {v:<16}" for k, v in note.items()))
#        else:
           # print("Нет такого названия заметки")'''


def delete_note_by_id(number: str, date):
    '''МЕТОД ПО УДАЛЕНИЮ ЗАМЕТКИ ЧЕРЕЗ 'ID' ИЗ ПАМЯТИ И ФАЙЛА'''
    id_num = int(number)

    if number.isdigit() and id_num <= len(date):
        print(*(f"{k}: {v:<16}" for k, v in date[len(date) - 2].items()))
        question = input("Удаляем (y/n): ")
        if question in ANSWER:
            date.pop(id_num - 1)
            print("Запись успешно удалена")

            with open(FILE_NAME, 'w', encoding='utf-8') as file:
                for note in date:
                    for k, v in note.items():
                        if k != ID:
                            file.write(f"{v}; ")
                    file.write("\n")
                print("Файл обновлен")
        else:
            print(f"Записи под таким номером - {ID} нет.")

        # Выводим все строки после удаления
        for note in date:
            print(*(f"{k}: {v:<16}" for k, v in note.items()))

def main(date):
    '''МЕТОД ПО УПРАВЛЕНИЮ ПРОГРАММОЙ, ДАННЫЙ МЕТОД ВЫЗЫВАЕТ ДРУГИЕ МЕТОДЫ В ЗАВИСИМОСТИ ОТ ТОГО, ЧТО ВЫБРАЛ ПОЛЬЗОВАТЕЛЬ'''
    while (True):
        print(f'''\nЧто вы хотите сделать?
        1: Вывести на экран все заметки
        2: Вывести на экран заметку по определенной дате
        3: Добавить и сохранить новую заметку
        4: Редактировать заметку по названию заметки
        5: Удалить заметку
        0: Выйти''')

        choose = input('Ваш выбор: ')

        if choose == "1":
            print_date(date)
        elif choose == "2":
            print_note_by_date(date)
        elif choose == "3":
            add_new_note(date)
        elif choose  == "4":
            title_old_message = input("Введите название заметки, которую хотите заменить: ")
            title_old_message.strip().capitalize()
            edit_text_note(title_old_message= title_old_message, date=date)

        elif choose == "5":
            num_cell = input("Введите id поля которое хотите удалить: ")
            delete_note_by_id(number = num_cell, date = date)
        elif choose == "0":
            break
        else:
            print("Неверная команда")



if __name__ == '__main__':
    main(load_date())