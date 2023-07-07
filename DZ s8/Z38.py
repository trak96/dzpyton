# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def show_menu():
    print("\n Выберите действие:\n"
          "1.Отобразить весь справочник\n"
          "2.Изменить данные\n"
          "3.Удалить данные\n")
    choise = int(input("Ваш выбор: "))
    return choise

def work_with_file():
    choise = show_menu()
    home = read_csv('home.csv')
    while (choise !=3):
        if choise == 1:
            print(home)
            choise = show_menu()


    
def read_csv(file_name):
    data = list()
    fields = ["Фамилия", "Имя", "Телефон"]
    with open(file_name, 'r', encoding ='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

read_csv()