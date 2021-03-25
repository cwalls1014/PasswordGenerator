import random


class PasswordGenerator:
    def __init__(self):
        self.lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                              'u', 'v', 'w', 'x', 'y', 'z']

        self.upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
                             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                             'V', 'W', 'X', 'Y', 'Z']

        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

        self.characters = (self.lower_case_letters, self.upper_case_letters,
                           self.numbers, self.symbols)

        self.password = []

    def generate_password(self):
        x = 35
        while x != 0:
            pick_character_type = random.choice(self.characters)
            pick_character = random.choice(pick_character_type)
            self.password.append(pick_character)
            x -= 1
            if x == 27:
                self.password.append('-')
                x -= 1
            elif x == 18:
                self.password.append('-')
                x -= 1
            elif x == 9:
                self.password.append('-')
                x -= 1

        print(*self.password, sep='')

gp = PasswordGenerator()
gp.generate_password()
