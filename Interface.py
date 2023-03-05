class Interface:

    def comands(self):
        command = input("Меню : \n"
                    '1 - создать заметку\n'
                    '2 - прочитать заметку\n'
                    '3 - вывести все id по дате изменения\n'
                    '4 - редактировать заметку\n'
                    '5 - удалить заметку\n'
                    '6 - удалить все заметки\n'  
                    '7 - прочитать все заметки\n'
                    '8 - выход\n'                   
                    'Для выбора введите число и нажмите Enter: ')
        return command

    def input_title(self):
        print('\nВведите название заметки: ')
        title = input()
        while len(title) < 1:
            print('Поле не должно быть пустым: ')
            title = input()            
        else:
            return title

    def input_text(self):
        text = input("Введите текст заметки: ")
        return text

    def print_all_notes(self, notes):
        if len(notes) != 0:
            print('\nСписок всех заметок')
            print("NOTE FROM JSON")
        else:
            print('\nСписок заметок пуст')


    def print_sorted_list(self, notes):
        if len(notes) != 0:
            print('\nВсе заметки по дате изменения:')
            print("NOTE FROM JSON")
        else:
            print('\nСписок заметок пуст')
            
    def print_note(self, note):
        if len(note) != 0:
            print("NOTE FROM JSON")
        else:
            print('\nСписок заметок пуст')

    def input_id(self):
        return input("Введите id заметки: ")
    
    def completed_add(self):
        print('\nЗаметка добавлена')

    def completed_rafact(self):
        print('\nЗаметка изменена')

    def error_index(self):
        print('\nНеверный индекс')

    def completed_del_note(self):
        print('\nЗаметка удалена')

    def completed_del_notes(self):
        print('\nВсе заметки удаленыn')

    def out_of_index(self):   
        print("\nВыберете действие от 1 до 7")
    
    def bye(self):
        print("\nДо свидания!")