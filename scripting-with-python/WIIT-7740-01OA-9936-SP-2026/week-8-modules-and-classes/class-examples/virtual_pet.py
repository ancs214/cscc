class VirtualPet:

    def __init__(self, pet_name, pet_hunger, pet_thirst, pet_boredom, pet_tiredness):
        self.pet_name = pet_name
        self.pet_hunger = pet_hunger
        self.pet_thirst = pet_thirst
        self.pet_boredom = pet_boredom
        self.pet_tiredness = pet_tiredness

    def get_name(self):
        return self.pet_name

    def get_hunger(self):
        return self.pet_hunger

    def get_thirst(self):
        return self.pet_thirst

    def get_boredom(self):
        return self.pet_boredom

    def get_tiredness(self):
        return self.pet_tiredness

    def feed_pet(self):
        self.pet_hunger -= 20
        self.pet_thirst += 5

        if self.pet_hunger < 0:
            self.pet_hunger = 0

    def water_pet(self):
        self.pet_thirst -= 20
        self.pet_tiredness += 30

        if self.pet_thirst < 0:
            self.pet_thirst = 0

    def play_with_pet(self):
        self.pet_boredom -= 20
        self.pet_hunger += 10
        self.pet_thirst +=  10

        if self.pet_boredom < 0:
            self.pet_boredom = 0

    def pet_nap_time(self):
        self.pet_tiredness -= 20
        self.pet_hunger += 20
        self.pet_thirst += 4

        if self.pet_tiredness < 0:
            self.pet_tiredness = 0

    def tick(self):
        self.pet_hunger += 1
        self.pet_thirst += 1
        self.pet_boredom += 1
        self.pet_tiredness += 1

        if self.pet_hunger < 75:
            print(self.pet_name + ' starts to gnaw at your leg.')

        if self.pet_thirst < 75:
            print(self.pet_name + ' is drinking out of the toilet.')

        if self.pet_boredom < 75:
            print(self.pet_name + ' tore the couch apart.')

        if self.pet_tiredness < 75:
            print(self.pet_name + ' growls at anything that moves...')

        if self.pet_hunger > 100 or self.pet_thirst > 100:
            self.pet_is_alive = False

        if self.pet_boredom > 100 or self.pet_tiredness > 100:
            self.pet_has_not_runaway = False


    @staticmethod
    def ascii_art_dog():
        print("      /\\,_/\\  ")
        print("      /==_ (")
        print("     (Y_.) /       /// ")
        print("      U ) (__,_____) ) ")
        print("        )'   >     `/ ")
        print("        |._  _____  | ")
        print("        | | (    \\| ( ")
        print("        | | |    || | ")
        print("   ,,-. ),)_/ ., ))_/,,.-,_")