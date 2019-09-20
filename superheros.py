import random
from functools import reduce

class Ability():
    def __init__(self, name, attack_strength):
        ''' 
        Initiate the abilities class with its name and attack strength
            Args: 
                name (string): a single word discriptor of the ability
                attack_strength (int): the value of the abilities strength
            Returns:
                ability object: a new object
        '''
        self.name = name;
        self.max_damage = attack_strength

    def attack(self):
        ''' A function that returns random int between 0 and the initilized max_damage property'''
        return random.randint(0, self.max_damage)


class Armor():
    def __init__(self, name, blocking_strength):
        '''
        Initiate the armor class with name and blocking strength
            Args:
                name (string): a detailed one word discriptor of the armor
                blocking_strength (int): the max value that the armor can block
            Returns:
                armor (object): a new armor object
        '''
        self.name = name
        self.max_block = blocking_strength

    def block(self):
        '''A function that returns a random int between 0 and the initalized max_block property'''
        return random.randint(0, self.max_block)


class Hero():
    #TODO: Make a way for hero abilities to run out or be lost, and watch for heros still having abilities
    def __init__(self, name, starting_health=100):
        '''
        Initiate the hero class with name and starting health
            Args:
                name (string): a one word discription of the hero
                starting_health (int): a value for the heros inital health with a default of 100
                abilities (list): a list of the heros abilities
                armors (list): a list of the heros armors

            Returns:
                hero (object): a new hero object
        '''
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, new_ability):
        '''A setter function that adds a new ability to the hero'''
        self.abilities.append(new_ability)

    def add_armor(self, new_armor):
        '''A setter function that adds a new armor object to the hero'''
        self.armors.append(new_armor)

    def attack(self):
        '''A getter function that creates a list of attack values by looping through the heros abilities and then returns the sum of the list'''
        attack_values = list(map(lambda ability: ability.attack(), self.abilities))
        return reduce(lambda first_value, next_value: first_value + next_value, attack_values)

    def defend(self, damage_amount):
        '''
        A getter function that creates a list of block values by looping through the heros armors and then returns the sum of the list
            Args: 
                damage_amount (int): the amount of damage given to the hero
            Returns:
                damage_taken (int): the damage_taken subtracted by the heros total block 
        '''
        block_values = list(map(lambda armor: armor.block(), self.armors))
        damage_taken = damage_amount - reduce(lambda first_value, next_value: first_value + next_value, block_values)
        if damage_taken < 0:
            return 0
        else:
            return damage_taken

    def take_damage(self, damage):
        '''
        A setter function that updates the users current_health to reflect the damage minus the defence
            Args:
                damage (value): the value of the damage given to the hero
            Updates:
                current_health (int): sets the curret health equal to itself and the damage taken from defending
        '''
        self.current_health -= self.defend(damage)

    def is_alive(self):
        '''A getter function that returns true of false depending on whether or not the hero is alive'''
        if self.current_health <= 0:
            return False
        else:
            return True
        
    def fight(self, opponent):
        '''
        A function that takes in a hero to fight and pits them agians the current hero untill one dies or no ailities are left
            Args:
                opponent (Hero): a hero object 
            Returns:
                outcome (string): either which hero won or that the fight endded in a draw
        '''
        while self.is_alive() and opponent.is_alive():
            hero_attack = self.attack()
            opponent_attack = opponent.attack()
            self.take_damage(opponent_attack)
            opponent.take_damage(hero_attack)
        if self.is_alive() == False and opponent.is_alive == False:
            print('Draw! Both heros died from their injuries!')
        elif self.is_alive() == False:
            print(f'{opponent.name} won!')
        elif opponent.is_alive() == False:
            print(f'{self.name} won!')

if __name__ == '__main__':
    # Test the superhero classes by running `python3 superheros.py`
    ability = Ability('Kick', 15)
    another_ability = Ability('Punch', 10)
    armor = Armor('Shirt', 5)
    another_armor = Armor('Mouth Guard', 8)

    Bob = Hero('Bob Johson')
    Bob.add_ability(ability)
    Bob.add_ability(another_ability)
    Bob.add_armor(armor)
    Bob.add_armor(another_armor)

    Jan_The_Man = Hero('Jan the Man')
    Jan_The_Man.add_ability(ability)
    Jan_The_Man.add_ability(another_ability)
    Jan_The_Man.add_armor(armor)
    Jan_The_Man.add_armor(another_armor)

    Bob.fight(Jan_The_Man)



