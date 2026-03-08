from virtual_pet_menu import VirtualPetMenu
from virtual_pet import VirtualPet

def main():
    my_virtual_pet = VirtualPet('Carver',70,70,70,70)
    my_virtual_pet_menu = VirtualPetMenu()

    while True:
        print('This is your virtual pet. It is your responsibility to take care of ' + my_virtual_pet.get_name() + '.\n')

        print('Hunger: ' + str(my_virtual_pet.get_hunger()))
        print('Thirst: ' + str(my_virtual_pet.get_thirst()))
        print('Bored: ' + str(my_virtual_pet.get_boredom()))
        print('Tiredness: ' + str(my_virtual_pet.get_tiredness()))
        print()
        print()
        print('What do you want to do with your pet?')

        my_virtual_pet_menu.print_menu()
        menu_option = ''
        try:
            menu_option = int(input('Please enter an action for ' + my_virtual_pet.get_name() + '.'))
        except:
            print('Incorrect option. Please enter a number listed.')

        if menu_option == 1:
            my_virtual_pet.feed_pet()
            print('You fed ' + my_virtual_pet.get_name() + '.\n')
        elif menu_option == 2:
            my_virtual_pet.water_pet()
            print('You gave ' + my_virtual_pet.get_name() + ' some water.\n')
        elif menu_option == 3:
            my_virtual_pet.play_with_pet()
            print('You played with ' + my_virtual_pet.get_name() + '.\n')
        elif menu_option == 4:
            my_virtual_pet.pet_nap_time()
            print(my_virtual_pet.get_name() + ' took a nap.\n')
        elif menu_option == 5:
            print(my_virtual_pet.get_name() + 'has crossed the rainbow bridge. Thanks for being a good pet owner.\n')
            break

        my_virtual_pet.tick()

if __name__ == '__main__':
        main()