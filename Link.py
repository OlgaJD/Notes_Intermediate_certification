def run():
    act = ""
    while (act!=8):
        match option:
            case '1':
                # создать заметку
            case '2':
                # прочитать заметку
            case '3':
                # вывести все id по дате изменения
            case '4':
                # редактировать заметку
            case '5':
                # удалить заметку
            case '6':
                # удалить все заметки
            case '7':
                # прочитать все заметки
            case '8':
                # выход
                exit()
            case _:
                # обработка неверного ввода
