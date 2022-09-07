class Menu:
    def __init__(self, options):
        self.options = options
        self.show_menu()

    def show_menu(self):
        menu = ""
        for i, item in enumerate(self.options):
            if i != len(self.options) - 1:
                menu += f"[{i}] {item}\n"
            else:
                menu += f"[{i}] {item}"
        print(menu)

    def ask_menu(self):
        choice = input("Option: ")
        return choice

