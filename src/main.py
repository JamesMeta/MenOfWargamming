class Infantry:

    def __init__(self, unit_number, veterancy):
        self.unit_number = unit_number
        self.manpower = 100
        self.artillery = 3
        self.machine_guns = 2
        self.anti_tank = 2
        self.veterancy = veterancy
        self.incirclement = False
        self.unit_losses = 0

    def get_unit_number(self):
        return self.unit_number
    
    def get_manpower(self):
        return self.manpower
    
    def get_artillery(self):
        return self.artillery
    
    def get_machine_guns(self):
        return self.machine_guns
    
    def get_anti_tank(self):
        return self.anti_tank
    
    def get_veterancy(self):
        return self.veterancy
    
    def get_incirclement(self):
        return self.incirclement
    
    def get_unit_losses(self):
        return self.unit_losses
    
    def set_unit_number(self, unit_number):
        if unit_number > 0:
            self.unit_number = unit_number
        else:
            self.unit_number = 0
    
    def set_manpower(self, manpower):
        if manpower > 0:
            self.manpower = manpower
        else:
            self.manpower = 0

    def set_artillery(self, artillery):
        if artillery > 0:
            self.artillery = artillery
        else:
            self.artillery = 0
    
    def set_machine_guns(self, machine_guns):
        if machine_guns > 0:
            self.machine_guns = machine_guns
        else:
            self.machine_guns = 0
    
    def set_anti_tank(self, anti_tank):
        if anti_tank > 0:
            self.anti_tank = anti_tank
        else:
            self.anti_tank = 0

    def set_veterancy(self, veterancy):
        if veterancy > 0:
            self.veterancy = veterancy
        else:
            self.veterancy = 0
    
    def set_incirclement(self, incirclement):
        self.incirclement = incirclement
    
    def sum_unit_losses(self, unit_losses):
        self.unit_losses += unit_losses
    

class Armored:
    def __init__(self, unit_number, veterancy):
        self.unit_number = unit_number
        self.manpower = 60
        self.tanks = 6
        self.motorized = 5
        self.veterancy = veterancy
        self.incirclement = False
        self.unit_losses = 0
    
    def get_unit_number(self):
        return self.unit_number
    
    def get_manpower(self):
        return self.manpower
    
    def get_tanks(self):
        return self.tanks
    
    def get_motorized(self):
        return self.motorized
    
    def get_veterancy(self):
        return self.veterancy
    
    def get_incirclement(self):
        return self.incirclement
    
    def get_unit_losses(self):
        return self.unit_losses
    
    def set_unit_number(self, unit_number):
        if unit_number > 0:
            self.unit_number = unit_number
        else:
            self.unit_number = 0
    
    def set_manpower(self, manpower):
        if manpower > 0:
            self.manpower = manpower
        else:
            self.manpower = 0

    def set_tanks(self, tanks):
        if tanks > 0:
            self.tanks = tanks
        else:
            self.tanks = 0

    def set_motorized(self, motorized):
        if motorized > 0:
            self.motorized = motorized
        else:
            self.motorized = 0

    def set_veterancy(self, veterancy):
        if veterancy > 0:
            self.veterancy = veterancy
        else:
            self.veterancy = 0
    
    def set_incirclement(self, incirclement):
        self.incirclement = incirclement
    
    def sum_unit_losses(self, unit_losses):
        self.unit_losses += unit_losses


class Battle:

    def __init__(self, battle_name, winner, attacker, defender):
        self.battle_name = battle_name
        self.winner = winner
        self.attacker = attacker
        self.defender = defender
        self.attacker_losses = 0
        self.defender_losses = 0

    def __str__(self):
        return f"{self.battle_name} \nWinner: {self.winner} \nAttacker: {self.attacker} \nDefender: {self.defender} \nAttacker Losses: {self.attacker_losses} \nDefender Losses: {self.defender_losses}"
    

class Country:
    
    def __init__(self, country_name, country_tag, population, num_of_cities, production_coefficent, attrition_coefficent):
        self.country_name = country_name
        self.country_tag = country_tag
        self.population = population
        self.num_of_cities = num_of_cities
        self.production_coefficent = production_coefficent
        self.attrition_coefficent = attrition_coefficent
        self.population_per_city = self.population // self.num_of_cities
        self.infantry_divisions = []
        self.armored_divisions = []
