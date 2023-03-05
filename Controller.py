from Notes import Notes


class Controller:
    def __init__(self, Function, Interface):
        self.function = Function
        self.interface = Interface

    def menu(self):
        return self.interface.comands()

    def create_note(self):
        self.function.add_note(Notes(self.interface.input_title(), self.interface.input_text()))
        self.interface.completed_add()

    def read_note(self):
        try:
            self.interface.print_note(self.function.return_note(self.function.check_index(self.interface.input_id())))
        except:
            self.interface.error_index()

    def update_note(self):
        try:
            self.function.edit_note(self.function.check_index(self.interface.input_id()), self.interface.input_title(),
                                    self.interface.input_text())
            self.interface.completed_rafact()
        except:
            self.interface.error_index()

    def print_sorted_list(self):
        self.interface.print_sorted_list(self.function.sort_notes(self.function.read_notes()))

    def del_note(self):
        try:
            self.function.del_note((self.function.check_index(self.interface.input_id())))
            self.interface.completed_del_note()
        except:
            self.interface.error_index()

    def del_all_notes(self):
        self.function.del_notes()
        self.interface.completed_del_notes()

    def print_all_notes(self):
        self.interface.print_all_notes(self.function.sort_notes(self.function.read_notes()))

    def wrong_index(self):
        self.interface.out_of_index()

    def bye(self):
        self.interface.bye()