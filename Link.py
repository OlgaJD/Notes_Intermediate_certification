from Controller import Controller as C
from Function import Function as F
from Interface import Interface as I

def run():
    act = ""
    option = C(F('notes.json'), I())
    while (act!=8):
        match option.menu():
            case '1':
                option.create_note()
            case '2':
                option.read_note()
            case '3':
                option.print_sorted_list()
            case '4':
                option.update_note()
            case '5':
                option.del_note()
            case '6':
                option.del_all_notes()
            case '7':
                option.print_all_notes()
            case '8':
                option.bye()
                exit()
            case _:
                option.wrong_index()
run()