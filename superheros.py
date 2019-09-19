import random

class Ability():
    def __init__(self, name, attack_strength):
        ''' 
        Initiate the abilities class with its name and strength
            Args: 
                name (string): a single word discriptor of the ability
                attack_strength (int): the value of the abilities strength
            Returns:
                ability object: a new object with filled in parameters
        '''
        self.name = name;
        self.max_damage = attack_strength

    def attack(self):
        ''' A function that returns random int between 0 and the initilized max_damage property'''
        return random.randint(0, self.max_damage)


class Armor():
    def __init__(self, name, blocking_strength):
        '''
        Initiate the armor class with name and blocking_strength
            Args:
                name (string): a detailed one word discriptor of the armor
                blocking_strength (int): the max value that the armor can block
            Returns:
                armor (object): a new armor object with filled in parameters
        '''
        self.name = name
        self.max_block = blocking_strength

    def block(self):
        '''A function that returns a random int between 0 and the initalized max_block property'''
        return random.randint(0, self.max_block)

if __name__ == '__main__':
    # Test the superhero classes by running `python3 superheros.py`
    ability = Ability('Flick', 4)
    print('name:', ability.name)
    print('power:', ability.attack())

    armor = Armor('Shirt', 5)
    print('name:', armor.name)
    print('power:', armor.block())