""" Solution to the second puzzle of Day 11 on adventofcode.com
"""

class Base26Password(object):
    """ When you're too lazy to write a BaseN class or
        figure out a better way to do this..
    """
    def __init__(self, string):
        self.value = []

        for char in string:
            self.value.insert(0, (ord(char) - 97))

    def to_string(self):
        """ Return the number as a string of letters
        """
        string = ''
        for place in reversed(self.value):
            string += chr(place + 97)

        return string

    def validate(self):
        """ Check to see if this password is valid
        """
        if 'i' in self.value or \
           'o' in self.value or \
           'l' in self.value:
            return False

        pair_count = 0
        place = 0
        while place < len(self.value) - 1:
            if self.value[place] == self.value[place + 1]:
                pair_count += 1
                place += 1

            if pair_count >= 2:
                break

            place += 1

        if pair_count < 2:
            return False

        straight_found = False
        place = 0
        while place < len(self.value) - 2:
            if self.value[place + 1] == self.value[place] - 1 and \
               self.value[place + 2] == self.value[place] - 2:
                straight_found = True
                break

            place += 1

        if not straight_found:
            return False

        return True


    def next_pw(self):
        """ Generate the next password
        """
        place = 0
        self.value[place] += 1

        while place < len(self.value):
            if self.value[place] >= 26:
                remainder = self.value[place] % 25
                self.value[place] -= 26

                if place + 1 > len(self.value) - 1:
                    self.value.append(remainder)
                else:
                    self.value[place + 1] += remainder

            place += 1




def main():
    """ Figure out Santa's new password
    """

    password = Base26Password('hepxxyzz')

    for _ in range(1000000):
        password.next_pw()
        if password.validate():
            break

    if password.validate():
        print password.to_string()


if __name__ == '__main__':
    main()

