import random

class Ability():
    def __init__(self, name, attack_strength):
        ''' 
        Initiate the abilities class with its name and strength
            Args: 
                name (string): a single word discriptor of the ability
                attack_strength (int): the value of the abilities strength
            Returns:
                ability object: a new object with filled in peramiters
        '''
        self.name = name;
        self.max_damage = attack_strength

    def attack(self):
        ''' A function that returns a value between 0 and the abilities self.max_damage property'''
        return random.randint(0, self.max_damage)



if __name__ == '__main__':
    # Test the ability class
    ability = Ability('Flick', 4)
    print('name', ability.name)
    print('power', ability.attack())