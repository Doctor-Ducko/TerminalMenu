from menu_sys import Menu

class MyMenu(Menu):
    def __init__(self, title, menu_options=["Test"], auto_load=False, start_at_zero=False):
        super().__init__(title, menu_options, auto_load, start_at_zero)

    def load_choice(self, input_value):
        print("Hello!")


my_menu = MyMenu("My Menu")
my_menu.load_menu()