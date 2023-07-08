# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def show_menu():
    print("\n Выберите действие:\n"
          "1.Отобразить весь справочник\n"
          "2.Изменить данные\n"
          "3.Добавить данные\n"
          "4.Удалить данные\n")
    choise = int(input("Ваш выбор: "))
    return choise

def work_with_file():
    choise = show_menu()
    home = 'home.csv'
    while (choise !=0):
        if choise == 1:
            choise = read_csv(home)
            choise = show_menu()
        elif choise == 2:
            edit_data(home)
            choise = show_menu()
        elif choise == 3:
            add_data(home)
            choise = show_menu()
        elif choise == 4:
            delete_data(home)
            choise = show_menu()
        else:
            choise = 0


def read_csv(file_name):
    print("\nПП | ФИО | Телефон")
    with open(file_name, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

# Изменяет информацию из файла
def edit_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(",")
    fio = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    # num = elements[0]
    if len(fio) == 0:
        fio = elements[0]
    if len(name) == 0:
        name = elements[1]   
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{fio},{name},{phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

# Удаляет информацию из файла
def delete_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

# Записывает информацию в файл
def add_data(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        fio = input("Введите Фамилию: ")
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        data.write(f"{num},{fio},{name},{phone}\n")
        print(f"Добавлена запись : {num},{fio},{name},{phone}\n")

work_with_file()