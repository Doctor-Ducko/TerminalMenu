# Base class for all future menus to work off of
class Menu():

    def __init__(self, title, menu_options=["Quit"], auto_load=False, start_at_zero=False):
        self.title          = title
        self.menu_options   = menu_options
        self.start_at_zero  = start_at_zero

        if auto_load:
            self.load_menu()


    # Displays the menu to the terminal then loads selection method
    def load_menu(self):
        print(self.title)

        for i, item in enumerate(self.menu_options):
            if not self.start_at_zero:
                print(str(i+1) + ") " + item)
            else:
                print(str(i) + ") " + item)

        self.get_choice()


    # Gets the users input and validates it, then loads a menu option define in a subclass
    def get_choice(self):
        choices     = len(self.menu_options)
        lowest      = 0

        # Offsets calculations for menus starting at zero
        if self.start_at_zero:
            choices -= 1
            lowest  -= 1

        while True:
            input_value = input("Input: ")

            # Handle non-int values
            try:
                input_value = int(input_value)
            except ValueError:
                print("ERROR! Non-integer value was provided.")
                continue

            # Check if input is within valid constraints
            if (input_value > choices) or (input_value <= lowest):
                print("ERROR! Input out of range")
                continue

            break

        # Calls so people dont have to rewrite things
        self.load_choice(input_value)


    # Should be replaced in a subclass
    def load_choice(self, input_value):
        print("ERROR! Menu does not have any choices to parse")


class ExampleMenu(Menu):
    def __init__(self, title, menu_options=["About", "Credits", "Quit"], auto_load=False, start_at_zero=False):
        super().__init__(title, menu_options, auto_load, start_at_zero)

    def load_choice(self, input_value):
        match input_value:
            case 1:
                print("A simple menu system i wont get away with resuing in the american computer science leauge\n")
                self.load_menu()
            case 2:
                print("Lead Dev: Sean \"Doctor Ducko\" Brierley")
                print("Moral Support: Ari \"Chilli\" Coleman")
                print("Moral Support: Eli \"Hydrop0x\" Machan\n")
                self.load_menu()
            case 3:
                quit()


if __name__ == "__main__":
    example_menu = ExampleMenu("Example Menu")
    example_menu.load_menu()