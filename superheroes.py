import random
import math
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
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        ''' A method that returns random int between 0 and the initilized max_damage property'''
        return random.randint(0, self.max_damage)


class Weapon(Ability):
    def __init__(self, name, attack_strength):
        '''
        Initiate the weapons subclass with name and attack_strength
            Args:
                name (string): a single word descriptor of the weapon
                attack_strength (int): value for the weapons may power
            Returns:
                weapon (object): new weapon object
        '''
        super().__init__(name, attack_strength)

    def attack(self):
        '''A method that returns a randome int between 0 and half the iniitlaized max_damage property'''
        return random.randint(math.floor(self.max_damage/2), self.max_damage)


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
        '''A method that returns a random int between 0 and the initalized max_block property'''
        return random.randint(0, self.max_block)


class Hero():
    # TODO: Make a way for hero abilities to run out or be lost, and watch for heroes still having abilities
    def __init__(self, name, starting_health=100):
        '''
        Initiate the hero class with name, starting health, kills, and deaths
            Args:
                name (string): a one word discription of the hero
                starting_health (int): a value for the heroes inital health with a default of 100
            Returns:
                hero (object): a new hero object
        '''
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    def add_kill(self, num_kills):
        '''A method for adding a kill to the heroes kill count'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        '''A method for adding a death the the heroes death count'''
        self.deaths += num_deaths

    def add_ability(self, new_ability):
        '''A setter method that adds a new ability to the hero'''
        self.abilities.append(new_ability)

    def add_armor(self, new_armor):
        '''A setter method that adds a new armor object to the hero'''
        self.armors.append(new_armor)

    def add_weapon(self, weapon):
        '''A method for adding a new weapon object to the hero'''
        self.abilities.append(weapon)

    def attack(self):
        '''A getter method that creates a list of attack values by looping through the heroes abilities and then returns the sum of the list'''
        return sum(ability.attack() for ability in self.abilities)

    def defend(self, damage_amount=0):
        '''
        A getter method that creates a list of block values by looping through the heroes armors and then returns the sum of the list
            Args:
                damage_amount (int): the amount of damage given to the hero
            Returns:
                damage_taken (int): the damage_taken subtracted by the heroes total block
        '''
        return sum(armor.block() for armor in self.armors)
        

    def take_damage(self, damage):
        '''
        A setter method that updates the users current_health to reflect the damage minus the defence
            Args:
                damage (value): the value of the damage given to the hero
            Updates:
                current_health (int): sets the curret health equal to itself and the damage taken from defending
        '''
        damage_taken = damage - self.defend(damage)
        if damage_taken > 0:
            self.current_health -= damage_taken

    def is_alive(self):
        '''A getter method that returns true of false depending on whether or not the hero is alive'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        ''' 
        A method that takes in a hero to fight and pits them agians the current hero untill one dies or no ailities are left
            Args:
                opponent (Hero): a hero object
            Returns:
                outcome (string): either which hero won or that the fight endded in a draw
        '''
        print(f'{self.name} and {opponent.name} are fighting!')
        while self.is_alive() and opponent.is_alive():
            hero_attack = self.attack()
            opponent_attack = opponent.attack()
            self.take_damage(opponent_attack)
            opponent.take_damage(hero_attack)
            if self.is_alive() == False and opponent.is_alive() == False:
                print('Draw! Both heroes died from their injuries!')
                self.add_kill(1)
                self.add_death(1)
            elif self.is_alive() == False:
                print(f'{opponent.name} won!')
                self.add_death(1)
                opponent.add_kill(1)
            elif opponent.is_alive() == False:
                print(f'{self.name} won!')
                self.add_kill(1)
                opponent.add_death(1)


class Team():
    def __init__(self, name):
        '''
        Initialize the team class with name and heroes properties
            Args:
                name (string): a single word descriptor of the team
                heroes (list): a list for hero objects
            Returns:
                team (object): a new team object
        '''
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        '''A method for adding a new hero to the team'''
        self.heroes.append(hero)

    def remove_hero(self, hero_name):
        '''A method for removing a hero from the team'''
        for index, hero in enumerate(self.heroes):
            if hero.name == hero_name:
                del self.heroes[index]
        return 0

    def view_all_heroes(self):
        '''A method for seeing all the heroes on the team'''
        for hero in self.heroes:
            print(hero.name)

    def heroes_alive(self):
        return [hero for hero in self.heroes if hero.is_alive()]

    def fight_should_continue(self, opponent, team_alive, opponents_alive):
        '''A helper function for checking if a fight should coninue or not'''
        team_abilities = sum(len(hero.abilities) for hero in self.heroes)
        opponent_abilities = sum(len(hero.abilities) for hero in opponent.heroes)
        if len(team_alive) > 0 and len(opponents_alive) > 0:
            if team_abilities > 0 and opponent_abilities > 0:
                return True
            elif team_abilities <= 0 and opponent_abilities > 0:
                return True
            elif team_abilities > 0 and opponent_abilities <= 0:
                return True
            else:
                return False
        else:
            return False

    def attack(self, opponent):
        '''A method for battling the team against another'''
        team_alive = self.heroes_alive()
        opponents_alive = opponent.heroes_alive()
        while self.fight_should_continue(opponent, team_alive, opponents_alive):
            team_hero = random.choice(team_alive)
            opponent_hero = random.choice(opponents_alive)
            team_hero.fight(opponent_hero)
            team_alive = self.heroes_alive()
            opponents_alive = opponent.heroes_alive()

    def revive_heroes(self, health=100):
        '''A method for resetting each heroes health to its starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''A method for printing the teams stats'''
        for hero in self.heroes:
            if hero.deaths == 0:
                kill_death_ratio = hero.kills / 1
            else:
                kill_death_ratio = hero.kills / hero.deaths
            print(f'{hero.name}: {kill_death_ratio}')


class Arena():
    def __init__(self, team_one=None, team_two=None):
        '''Initialate the arena class with a team one and team two properties'''
        self.team_one = team_one
        self.team_two = team_two

    def create(self, type_prompt, type_reference):
        '''
        A geneator method for prompting the user for values to create a specific object
            Args:
                type_prompt (sting): type to enter into the input promts
                type_reference (class): class refrence for the type to create
            Returns:
                object: a new type_reference object
        '''
        print(f'To create an {type_prompt} enter the following:')
        name = valid_str_input('Name: ')
        strength = valid_int_input('Strength: ')
        return type_reference(name, strength)

    def create_hero(self):
        '''A gernator method for prompting the suer for values to create a Hero instance'''
        print('To create a hero follow the steps below:')
        name = valid_str_input('Name: ')
        health = valid_int_input(f'How much health do you want {name} to have? ')
        numb_armors = valid_int_input(f'How much armor do you want {name} to have? ')
        armors = [self.create('Armor', Armor) for index in range(numb_armors)]
        numb_abilities = valid_int_input(f'How may abilities do you want {name} to have? ')
        abilities = [self.create('Ability', Ability) for index in range(numb_abilities)]
        numb_weapons = valid_int_input(f'How may weapons do you want {name} to have? ')
        abilities += [self.create('Weapon', Weapon) for index in range(numb_weapons)]
        hero = Hero(name, health)
        for armor in armors:
            hero.add_armor(armor)
        for ability in abilities:
            hero.add_ability(ability)
        return hero

    def build_team_one(self):
        '''A gernator method for prompting the user for values to create team one for the arena'''
        print('Create the first team by following the steps below: ')
        name = valid_str_input('Team Name: ')
        numb_heroes = valid_int_input('How many heroes are on this team? ')
        self.team_one = Team(name)
        for _ in range(numb_heroes):
            self.team_one.add_hero(self.create_hero())

    def build_team_two(self):
        '''A gernator method for prompting the user for values to create team two for the arena'''
        print('Create the second team by following the steps below: ')
        name = valid_str_input('Team Name: ')
        numb_heroes = valid_int_input('How many heroes are on this team? ')
        self.team_two = Team(name)
        for _ in range(numb_heroes):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        '''A method for making the two teams in the arena fight agianst each other'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''A method for printing out the teams statistics'''
        alive_team_one = self.team_one.heroes_alive()
        alive_team_two = self.team_two.heroes_alive()
        if len(alive_team_one) <= 0 and len(alive_team_two) <= 0:
            print('Draw! No heroes survied the battle.')
        elif len(alive_team_one) <= 0:
            print(f'{self.team_two.name} Won!')
            for hero in alive_team_two:
                print(f'{hero.name} Survived')
        elif len(alive_team_two) <= 0:
            print(f'{self.team_one.name}e Won!')
            for hero in alive_team_one:
                print(f'{hero.name} Survived')
        else:
            print('I\'d tell you what happened but I\'ll let the stats speak for themselves')
            for hero in alive_team_one:
                print(f'{hero.name} survied...')
            for hero in alive_team_two:
                print(f'{hero.nam} survied...')
        team_one_kd_average = adverage_kd(self.team_one.heroes)
        team_two_kd_average = adverage_kd(self.team_two.heroes)

        print('Adverage Kill/Death Ratios')
        print(f'Team One: {team_one_kd_average}',
              f'Team Two: {team_two_kd_average}')


def valid_str_input(prompt):
    user_input = input(prompt)
    while user_input == '' or user_input == ' ':
        user_input = input('Invaled input, try agian: ')
    return user_input

def valid_int_input(prompt):
    user_input = input(prompt)
    while not user_input.isnumeric():
        user_input = input('Positive integer required, try agian: ')
    return int(user_input)

def adverage_kd(heroes):
    team_one_kd_sum = 0
    for hero in heroes:
        if hero.deaths == 0:
            team_one_kd_sum += hero.kills
        else:
            team_one_kd_sum += hero.kills/hero.deaths
    return team_one_kd_sum / len(heroes)

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

## Test Battling ###
# if __name__ == "__main__":
#     ability = Ability('Kick', 15)
#     another_ability = Ability('Punch', 10)
#     armor = Armor('Shirt', 5)
#     another_armor = Armor('Mouth Guard', 8)

#     Bob = Hero('Bob Johson')
#     Bob.add_ability(ability)
#     Bob.add_ability(another_ability)
#     Bob.add_armor(armor)
#     Bob.add_armor(another_armor)

#     Jan_The_Man = Hero('Jan the Man')
#     Jan_The_Man.add_ability(ability)
#     Jan_The_Man.add_ability(another_ability)
#     Jan_The_Man.add_armor(armor)
#     Jan_The_Man.add_armor(another_armor)

#     team_one = Team('Accounting', [Bob])
#     team_two = Team('Marketing', [Jan_The_Man])

#     arena = Arena(team_one, team_two)
#     arena.team_battle()
#     arena.show_stats()