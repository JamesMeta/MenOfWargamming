class Infantry:

    def __init__(self, unit_number, veterancy):
        self.unit_number = unit_number
        self.manpower = 100
        self.artillery = 3
        self.machine_guns = 2
        self.anti_tank = 2
        self.veterancy = veterancy
        self.incirclement = False

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
    
    def __init__(self, country_name, country_tag, population, trained_men, conscription_law, num_of_cities, production_coefficient, attrition_coefficient, surplus_artillery, surplus_anti_tank, surplus_machine_guns, surplus_tanks, surplus_motorized):
        self.country_name = country_name
        self.country_tag = country_tag
        self.population = population
        self.num_of_cities = num_of_cities
        self.production_coefficient = production_coefficient
        self.attrition_coefficient = attrition_coefficient
        self.population_per_city = self.population // self.num_of_cities

        self.conscription_law = conscription_law

        self.eligible_men = self.population * self.conscription_law
        self.trained_men = trained_men

        self.infantry_divisions = {}
        self.armored_divisions = {}

        self.surplus_artillery = surplus_artillery
        self.surplus_anti_tank = surplus_anti_tank
        self.surplus_machine_guns = surplus_machine_guns
        self.surplus_tanks = surplus_tanks
        self.surplus_motorized = surplus_motorized

        self.manpower_losses = 0
        self.artillery_losses = 0
        self.anti_tank_losses = 0
        self.machine_guns_losses = 0
        self.tanks_losses = 0
        self.motorized_losses = 0

        
         

    def get_country_name(self):
        return self.country_name
    
    def get_conscription_law(self):
        return self.conscription_law

    def get_country_tag(self):
        return self.country_tag
    
    def get_population(self):
        return self.population
    
    def get_num_of_cities(self):
        return self.num_of_cities
    
    def get_production_coefficient(self):
        return self.production_coefficient
    
    def get_attrition_coefficient(self):
        return self.attrition_coefficient
    
    def get_population_per_city(self):
        return self.population_per_city
    
    def get_manpower_losses(self):
        return self.manpower_losses
    
    def get_artillery_losses(self):
        return self.artillery_losses
    
    def get_anti_tank_losses(self):
        return self.anti_tank_losses
    
    def get_machine_guns_losses(self):
        return self.machine_guns_losses
    
    def get_tanks_losses(self):
        return self.tanks_losses
    
    def get_motorized_losses(self):
        return self.motorized_losses

    def get_surplus_artillery(self):
        return self.surplus_artillery
    
    def get_surplus_anti_tank(self):
        return self.surplus_anti_tank
    
    def get_surplus_machine_guns(self):
        return self.surplus_machine_guns
    
    def get_surplus_tanks(self):
        return self.surplus_tanks
    
    def get_surplus_motorized(self):
        return self.surplus_motorized
    
    def get_trained_men(self):
        return self.trained_men

    def set_country_name(self, country_name):
        self.country_name = country_name

    def set_country_tag(self, country_tag):
        self.country_tag = country_tag
    
    def set_population(self, population):
        if population > 0:
            self.population = population
        else:
            self.population = 0
    
    def set_consription_law(self, conscription_law):
        if conscription_law >= 0 and conscription_law <= 5:
            self.conscription_law = conscription_law
        else:
            self.conscription_law = 0

    def set_num_of_cities(self, num_of_cities):
        if num_of_cities > 0:
            self.num_of_cities = num_of_cities
        else:
            self.num_of_cities = 0
    
    def set_production_coefficient(self, production_coefficient):
        if production_coefficient > 0:
            self.production_coefficient = production_coefficient
        else:
            self.production_coefficient = 0
    
    def set_attrition_coefficient(self, attrition_coefficient):
        if attrition_coefficient > 0:
            self.attrition_coefficient = attrition_coefficient
        else:
            self.attrition_coefficient = 0
    
    def set_population_per_city(self, population_per_city):
        if population_per_city > 0:
            self.population_per_city = population_per_city
        else:
            self.population_per_city = 0

    def find_avaliable_unit_number(self, unit_type):
        if unit_type == "infantry":

            for i in range(len(self.infantry_divisions)):
                unit_number = i
                if unit_number not in self.infantry_divisions:
                    return unit_number
            
            return len(self.infantry_divisions)+1
        
        elif unit_type == "armored":

            for i in range(len(self.armored_divisions)):
                unit_number = i
                if unit_number not in self.armored_divisions:
                    return unit_number
            
            return len(self.armored_divisions)+1
            
    def get_unit(self,unit_number, unit_type):
        if unit_type == "infantry":
            return self.infantry_divisions[unit_number]
        elif unit_type == "armored":
            return self.armored_divisions[unit_number]

    def spawn_infantry(self, veterancy):
        unit_number = self.find_avaliable_unit_number("infantry")
        self.infantry_divisions[unit_number] = Infantry(unit_number, veterancy)
        print(f"Spawned Infantry Division {unit_number} for {self.country_name}")
    
    def spawn_armored(self, veterancy):
        unit_number = self.find_avaliable_unit_number("armored")
        self.armored_divisions[unit_number] = Armored(unit_number, veterancy)
        print(f"Spawned Armored Division {unit_number} for {self.country_name}")
    
    def delete_unit(self, unit_number, unit_type):
        if unit_type == "infantry":
            del self.infantry_divisions[unit_number]
        elif unit_type == "armored":
            del self.armored_divisions[unit_number]
        
        print(f"Deleted {unit_type} Division {unit_number} for {self.country_name}")

    #remaining equipment list structure [men, artillery, machine_guns, anti_tank, tanks, motorized]
    def take_casualties(self, unit_number, unit_type, remaining_equipment_list):
        if unit_type == "infantry":

            unit = self.infantry_divisions[unit_number]

            previous_manpower = unit.get_manpower()
            previous_artillery = unit.get_artillery()
            previous_anti_tank = unit.get_anti_tank()
            previous_machine_guns = unit.get_machine_guns()

            current_manpower = remaining_equipment_list[0]
            current_artillery = remaining_equipment_list[1]
            current_machine_guns = remaining_equipment_list[2]
            current_anti_tank = remaining_equipment_list[3]

            self.manpower_losses+= previous_manpower - current_manpower
            self.anti_tank_losses+= previous_anti_tank - current_anti_tank
            self.artillery_losses+= previous_artillery - current_artillery
            self.machine_guns_losses+= previous_machine_guns - current_machine_guns

            self.population -= previous_manpower - current_manpower

            unit.set_manpower(current_manpower)
            unit.set_artillery(current_artillery)
            unit.set_anti_tank(current_anti_tank)
            unit.set_machine_guns(current_machine_guns)

            if unit.get_manpower() == 0:
                self.delete_unit(unit_number, unit_type)

        elif unit_type == "armored":
            
            unit = self.armored_divisions[unit_number]

            previous_manpower = unit.get_manpower()
            previous_tanks = unit.get_tanks()
            previous_motorized = unit.get_motorized()

            current_manpower = remaining_equipment_list[0]
            current_tanks = remaining_equipment_list[4]
            current_motorized = remaining_equipment_list[5]

            self.manpower_losses+= previous_manpower - current_manpower
            self.tanks_losses+= previous_tanks - current_tanks
            self.motorized_losses+= previous_motorized - current_motorized

            self.population -= previous_manpower - current_manpower

            unit.set_manpower(current_manpower)
            unit.set_tanks(current_tanks)
            unit.set_motorized(current_motorized)

            if unit.get_manpower() == 0:
                self.delete_unit(unit_number, unit_type)

    def change_unit_status(self, unit_number, unit_type):
        if unit_type == "infantry":
            unit = self.infantry_divisions[unit_number]
            unit.set_incirclement(not unit.get_incirclement())
        elif unit_type == "armored":
            unit = self.armored_divisions[unit_number]
            unit.set_incirclement(not unit.get_incirclement())
    
    def understrength_units_exist(self, unit_type):
        if unit_type == "infantry":
            for unit_number in self.infantry_divisions:
                if self.infantry_divisions[unit_number].get_manpower() < 100:
                    return True
            return False
        elif unit_type == "armored":
            for unit_number in self.armored_divisions:
                if self.armored_divisions[unit_number].get_manpower() < 60:
                    return True
            return False

    def resupply_all_units(self):

        replacement_manpower = self.trained_men
        self.trained_men = 0

        guaranteed_infantry_replacements = round(replacement_manpower * 0.25)

        while replacement_manpower > 0 and self.understrength_units_exist("armored"):
            for unit in self.armored_divisions:
                if unit.get_manpower() < 60:
                    unit.set_manpower(unit.get_manpower()+1)
                    replacement_manpower -= 1
        
        replacement_manpower += guaranteed_infantry_replacements

        while replacement_manpower > 0 and self.understrength_units_exist("infantry"):
            for unit in self.infantry_divisions:
                if unit.get_manpower() < 100:
                    unit.set_manpower(unit.get_manpower()+1)
                    replacement_manpower -= 1

        self.trained_men = replacement_manpower
        
        #TODO: resupply equipment for all units


    def next_turn():
        pass