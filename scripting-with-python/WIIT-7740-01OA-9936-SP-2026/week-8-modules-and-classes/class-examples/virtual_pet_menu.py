class VirtualPetMenu:
    menu_options = {
        1:'Feed',
        2:'Water',
        3:'Play with',
        4:'Give nap',
        5:'Put to sleep'
    }

    def __init__(self, pet_name='Frisco'):
        self.pet_name = pet_name

    def print_menu(self):
        # loop through the keys
        for key in self.menu_options.keys():
            print(key, '--', self.menu_options[key])

    def feed_menu_option(self):
        print('1. Feed ' + self.pet_name)

    def water_menu_option(self):
        print('2. Water ' + self.pet_name)

    def play_with_menu_option(self):
        print('3. Play with ' + self.pet_name)

    def give_nap_menu_option(self):
        print('4. Give ' + self.pet_name + 'a nap')

    def quit_put_to_sleep_menu_option(self):
        print('5. Put ' + self.pet_name + 'to sleep')
