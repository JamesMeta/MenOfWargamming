import random
import matplotlib.pyplot as plt

class Infantry:

    def __init__(self, unit_number, veterancy, nationality, country_tag):
        self.unit_number = unit_number
        self.manpower = 100
        self.artillery = 3
        self.machine_guns = 2
        self.anti_tank = 2
        self.veterancy = veterancy
        self.incirclement = False
        self.unit_losses = 0

        self.deployed_manpower = 0
        self.deployed_artillery = 0
        self.deployed_machine_guns = 0
        self.deployed_anti_tank = 0

        self.rear_guard = False

        self.nationality = nationality
        self.country_tag = country_tag

        self.type = "Infantry"
        
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
    
    def get_deployed_manpower(self):
        return self.deployed_manpower
    
    def get_deployed_artillery(self):
        return self.deployed_artillery
    
    def get_deployed_machine_guns(self):
        return self.deployed_machine_guns
    
    def get_deployed_anti_tank(self):
        return self.deployed_anti_tank
    
    def get_nationality(self):
        return self.nationality
    
    def get_unit_type(self):
        return self.type
    
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

    def set_deployed_manpower(self, deployed_manpower):
        if deployed_manpower > 0:
            self.deployed_manpower = deployed_manpower
            self.manpower -= deployed_manpower

    def set_deployed_artillery(self, deployed_artillery):
        if deployed_artillery > 0:
            self.deployed_artillery = deployed_artillery
            self.artillery -= deployed_artillery
    
    def set_deployed_machine_guns(self, deployed_machine_guns):
        if deployed_machine_guns > 0:
            self.deployed_machine_guns = deployed_machine_guns
            self.machine_guns -= deployed_machine_guns
    
    def set_deployed_anti_tank(self, deployed_anti_tank):
        if deployed_anti_tank > 0:
            self.deployed_anti_tank = deployed_anti_tank
            self.anti_tank -= deployed_anti_tank

    def set_rear_guard(self):
        self.set_deployed_manpower(self.manpower//5)
        self.set_deployed_artillery(self.artillery//3)
        self.set_deployed_machine_guns(self.machine_guns//2)
        self.set_deployed_anti_tank(self.anti_tank//2)
        self.rear_guard = True
    
    def set_full_deployment(self):
        self.set_deployed_manpower(self.manpower)
        self.set_deployed_artillery(self.artillery)
        self.set_deployed_machine_guns(self.machine_guns)
        self.set_deployed_anti_tank(self.anti_tank)

    def after_action_update(self):

        self.deployed_manpower = 0
        self.deployed_artillery = 0
        self.deployed_machine_guns = 0
        self.deployed_anti_tank = 0

        self.rear_guard = False

    def sum_unit_losses(self, unit_losses):
        self.unit_losses += unit_losses

    def __str__(self):
        return f"Infantry Division {self.unit_number} \nManpower: {self.manpower} \nArtillery: {self.artillery} \nMachine Guns: {self.machine_guns} \nAnti Tank: {self.anti_tank} \nVeterancy: {self.veterancy} \nIncirclement: {self.incirclement}"
      
class Armored:
    def __init__(self, unit_number, veterancy, nationality, country_tag):
        self.unit_number = unit_number
        self.manpower = 60
        self.tanks = 6
        self.motorized = 5
        self.veterancy = veterancy
        self.incirclement = False
        self.unit_losses = 0

        self.deployed_manpower = 0
        self.deployed_tanks = 0
        self.deployed_motorized = 0

        self.rear_guard = False

        self.nationality = nationality
        self.country_tag = country_tag

        self.type = "Armored"

    
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
    
    def get_deployed_manpower(self):
        return self.deployed_manpower
    
    def get_deployed_tanks(self):
        return self.deployed_tanks
    
    def get_deployed_motorized(self):
        return self.deployed_motorized

    def get_nationality(self):
        return self.nationality
    
    def get_unit_type(self):
        return self.type
    
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

    def set_deployed_manpower(self, deployed_manpower):
        self.deployed_manpower = deployed_manpower
        self.manpower -= deployed_manpower
    
    def set_deployed_tanks(self, deployed_tanks):
        self.deployed_tanks = deployed_tanks
        self.tanks -= deployed_tanks

    def set_deployed_motorized(self, deployed_motorized):
        self.deployed_motorized = deployed_motorized
        self.motorized -= deployed_motorized
    
    def set_rear_guard(self):
        self.set_deployed_manpower(self.manpower//5)
        self.set_deployed_tanks(self.tanks//4)
        self.set_deployed_motorized(self.motorized//4)
        self.rear_guard = True
    
    def set_full_deployment(self):
        self.set_deployed_manpower(self.manpower)
        self.set_deployed_tanks(self.tanks)
        self.set_deployed_motorized(self.motorized)

    def after_action_update(self):

        self.deployed_manpower = 0
        self.deployed_tanks = 0
        self.deployed_motorized = 0

        self.rear_guard = False
    
    def sum_unit_losses(self, unit_losses):
        self.unit_losses += unit_losses

class Statistics:

    def __init__(self, country_map):
        
        self.total_battles = 0
        self.total_losses = 0

        self.battle_list = []
        self.country_map = country_map
        self.country_manpower_losses_map = {}
        self.country_equipment_losses_map = {}
        self.country_stockpile_map = {}

        for country_tag in self.country_map:
            self.country_manpower_losses_map[country_tag] = []
            self.country_equipment_losses_map[country_tag] = []
            self.country_stockpile_map[country_tag] = []
    
    def get_total_battles(self):
        return self.total_battles
    
    def get_total_losses(self):
        return self.total_losses
    
    def add_battle(self, battle):
        self.battle_list.append(battle)
        self.total_battles += 1
        self.total_losses += battle.get_total_losses()

    def next_turn(self):
        for country_tag in self.country_map:
            self.country_manpower_losses_map[country_tag].append(self.country_map[country_tag].get_manpower_losses())
            self.country_equipment_losses_map[country_tag].append(self.country_map[country_tag].get_artillery_losses() + self.country_map[country_tag].get_anti_tank_losses() + self.country_map[country_tag].get_machine_guns_losses() + self.country_map[country_tag].get_tanks_losses() + self.country_map[country_tag].get_motorized_losses())
            self.country_stockpile_map[country_tag].append(self.country_map[country_tag].get_surplus_artillery() + self.country_map[country_tag].get_surplus_anti_tank() + self.country_map[country_tag].get_surplus_machine_guns() + self.country_map[country_tag].get_surplus_tanks() + self.country_map[country_tag].get_surplus_motorized())
        
    def graph_equipment_losses_for_country(self, country_tag):
        losses_array = self.country_equipment_losses_map[country_tag]
        country = self.country_map[country_tag]
        plt.plot(losses_array, color=country.get_country_colour(), label=country.get_country_name())
        plt.xlabel('Weeks')
        plt.show()

    def graph_manpower_losses_for_country(self, country_tag):
        losses_array = self.country_manpower_losses_map[country_tag]
        country = self.country_map[country_tag]
        plt.plot(losses_array, color=country.get_country_colour(), label=country.get_country_name())
        plt.xlabel('Weeks')
        plt.show()

    def graph_equipment_losses_for_all(self):
        for country_tag in self.country_map:
            losses_array = self.country_equipment_losses_map[country_tag]
            country = self.country_map[country_tag]
            plt.plot(losses_array, color=country.get_country_colour(), label=country.get_country_name())

    def graph_manpower_losses_for_all(self):
        for country_tag in self.country_map:
            losses_array = self.country_manpower_losses_map[country_tag]
            country = self.country_map[country_tag]
            plt.plot(losses_array, color=country.get_country_colour(), label=country.get_country_name())

    def graph_stockpile_for_country(self, country_tag):
        stockpile_array = self.country_stockpile_map[country_tag]
        country = self.country_map[country_tag]
        plt.plot(stockpile_array, color=country.get_country_colour(), label=country.get_country_name())
        plt.xlabel('Weeks')
        plt.show()

    def graph_stockpile_for_all_countries(self):
        for country_tag in self.country_map:
            stockpile_array = self.country_stockpile_map[country_tag]
            country = self.country_map[country_tag]
            plt.plot(stockpile_array, color=country.get_country_colour(), label=country.get_country_name())
            

class Battle:

    def __init__(self, battle_name, winner, attacker, defender):
        self.battle_name = battle_name
        self.winner = winner
        self.attacker = attacker
        self.defender = defender
        self.attacker_losses = 0
        self.defender_losses = 0

    def get_total_losses(self):
        return self.attacker_losses + self.defender_losses

    def __str__(self):
        return f"{self.battle_name} \nWinner: {self.winner} \nAttacker: {self.attacker} \nDefender: {self.defender} \nAttacker Losses: {self.attacker_losses} \nDefender Losses: {self.defender_losses}"
    
class Country:
 
    def __init__(self, country_name, country_tag, nationality, population, trained_men, conscription_law, num_of_cities, production_coefficient, attrition_coefficient, surplus_artillery, surplus_anti_tank, surplus_machine_guns, surplus_tanks, surplus_motorized, colour):
        self.country_name = country_name
        self.country_tag = country_tag
        self.nationality = nationality
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

        self.internal_round_counter = 0

        self.country_colour = colour

    def get_country_name(self):
        return self.country_name
    
    def get_conscription_law(self):
        return self.conscription_law

    def get_country_tag(self):
        return self.country_tag
    
    def get_population(self):
        return self.population
    
    def get_country_colour(self):
        return self.country_colour

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
        self.infantry_divisions[unit_number] = Infantry(unit_number, veterancy, self.nationality, self.country_tag)
        print(f"Spawned Infantry Division {unit_number} for {self.country_name}")
    
    def spawn_armored(self, veterancy):
        unit_number = self.find_avaliable_unit_number("armored")
        self.armored_divisions[unit_number] = Armored(unit_number, veterancy, self.nationality, self.country_tag)
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
                if self.infantry_divisions[unit_number].get_manpower() < 100 or self.infantry_divisions[unit_number].get_artillery() < 3 or self.infantry_divisions[unit_number].get_machine_guns() < 2 or self.infantry_divisions[unit_number].get_anti_tank() < 2:
                    return True
            return False
        elif unit_type == "armored":
            for unit_number in self.armored_divisions:
                if self.armored_divisions[unit_number].get_manpower() < 60 or self.armored_divisions[unit_number].get_tanks() < 6 or self.armored_divisions[unit_number].get_motorized() < 5:
                    return True
            return False

    def resupply_is_possible(self, men, artillery, anti_tank, machine_gun, tanks, motorized):
        men_gap = 0
        artillery_gap = 0
        anti_tank_gap = 0
        machine_gun_gap = 0
        tanks_gap = 0
        motorized_gap = 0

        for unit in self.infantry_divisions.values():
            if unit.get_incirclement() == False:
                men_gap += 100 - unit.get_manpower()
                artillery_gap += 3 - unit.get_artillery()
                anti_tank_gap += 2 - unit.get_anti_tank()
                machine_gun_gap += 2 - unit.get_machine_guns()
        
        for unit in self.armored_divisions.values():
            if unit.get_incirclement() == False:
                men_gap += 60 - unit.get_manpower()
                tanks_gap += 6 - unit.get_tanks()
                motorized_gap += 5 - unit.get_motorized()

        if (men_gap>0 and men>0) or (artillery_gap>0 and artillery>0) or (anti_tank_gap>0 and anti_tank>0) or (machine_gun_gap>0 and machine_gun>0) or (tanks_gap>0 and tanks>0) or (motorized_gap>0 and motorized>0):
            return True
        
        else:
            return False

    def resupply_all_units(self):

        replacement_manpower = self.trained_men
        replacement_artillery = self.surplus_artillery
        replacement_anti_tank = self.surplus_anti_tank
        replacement_machine_guns = self.surplus_machine_guns
        replacement_tanks = self.surplus_tanks
        replacement_motorized = self.surplus_motorized

        self.trained_men = 0
        self.surplus_artillery = 0
        self.surplus_anti_tank = 0
        self.surplus_machine_guns = 0
        self.surplus_tanks = 0
        self.surplus_motorized = 0

        guaranteed_infantry_replacements = round(replacement_manpower * 0.25)

        while self.understrength_units_exist("armored") and self.resupply_is_possible(replacement_manpower,replacement_artillery, replacement_anti_tank, replacement_machine_guns, replacement_tanks, replacement_motorized):
            for unit in self.armored_divisions.values():
                if unit.get_incirclement() == False:
                    if unit.get_manpower() < 60:
                        unit.set_manpower(unit.get_manpower()+1)
                        replacement_manpower -= 1

                    if unit.get_tanks() < 6:
                        unit.set_tanks(unit.get_tanks()+1)
                        replacement_tanks -= 1

                    if unit.get_motorized() < 5:
                        unit.set_motorized(unit.get_motorized()+1)
                        replacement_motorized -= 1
        
        replacement_manpower += guaranteed_infantry_replacements

        while replacement_manpower > 0 and self.understrength_units_exist("infantry"):
            for unit in self.infantry_divisions.values():
                if unit.get_incirclement() == False:
                    if unit.get_manpower() < 100:
                        unit.set_manpower(unit.get_manpower()+1)
                        replacement_manpower -= 1
                    
                    if unit.get_artillery() < 3:
                        unit.set_artillery(unit.get_artillery()+1)
                        replacement_artillery -= 1

                    if unit.get_machine_guns() < 2:
                        unit.set_machine_guns(unit.get_machine_guns()+1)
                        replacement_machine_guns -= 1
                    
                    if unit.get_anti_tank() < 2:
                        unit.set_anti_tank(unit.get_anti_tank()+1)
                        replacement_anti_tank -= 1

        self.trained_men = replacement_manpower
        self.surplus_artillery = replacement_artillery
        self.surplus_anti_tank = replacement_anti_tank
        self.surplus_machine_guns = replacement_machine_guns
        self.surplus_tanks = replacement_tanks
        self.surplus_motorized = replacement_motorized

    def find_army_size(self):
        army_size = 0
        for unit in self.infantry_divisions.values():
            army_size += unit.get_manpower()
        for unit in self.armored_divisions.values():
            army_size += unit.get_manpower()
        return army_size

    def train_men(self):
        army_size = self.find_army_size()
        new_trainees = round(army_size/208)
        if new_trainees>self.eligible_men:
            print(f"Manpower pool dry for {self.country_name}")
            new_trainees=self.eligible_men
        
        self.eligible_men -= new_trainees
        self.population -= new_trainees

    def take_attrition(self):
        
        for unit in self.infantry_divisions.values():
            random_number = random.randint(1,round((1-self.attrition_coefficient)*100))
            if random_number > 60:
                random_number = random.randint(1,10)
                if random_number<2:
                    unit.set_artillery(unit.get_artillery()-1)
                    unit.set_machine_guns(unit.get_machine_guns()-1)
                    unit.set_anti_tank(unit.get_anti_tank()-1)

                    self.artillery_losses+=1
                    self.machine_guns_losses+=1
                    self.anti_tank_losses+=1
                
                elif random_number<4 and random_number >=2:
                    unit.set_machine_guns(unit.get_machine_guns()-1)
                    unit.set_anti_tank(unit.get_anti_tank()-1)

                    self.machine_guns_losses+=1
                    self.anti_tank_losses+=1
                
                elif random_number<6 and random_number >=4:
                    unit.set_artillery(unit.get_artillery()-1)
                    unit.set_machine_guns(unit.get_machine_guns()-1)

                    self.artillery_losses+=1
                    self.machine_guns_losses+=1

                elif random_number<8 and random_number >=6:
                    unit.set_artillery(unit.get_artillery()-1)

                    self.artillery_losses+=1

                elif random_number<10 and random_number >=8:
                    pass
        
        for unit in self.armored_divisions.values():
            random_number = random.randint(1,round((1-self.attrition_coefficient)*100))
            if random_number > 60:
                random_number = random.randint(1,10)
                if random_number<2:
                    unit.set_tanks(unit.get_tanks()-2)
                    unit.set_motorized(unit.get_motorized()-2)

                    self.tanks_losses+=2
                    self.motorized_losses+=2
                
                elif random_number<4 and random_number >=2:
                    unit.set_tanks(unit.get_tanks()-2)
                    unit.set_motorized(unit.get_motorized()-1)

                    self.tanks_losses+=2
                    self.motorized_losses+=1
                
                elif random_number<6 and random_number >=4:
                    unit.set_tanks(unit.get_tanks()-1)
                    unit.set_motorized(unit.get_motorized()-1)

                    self.tanks_losses+=1
                    self.motorized_losses+=1

                elif random_number<8 and random_number >=6:
                    unit.set_tanks(unit.get_tanks()-1)

                    self.tanks_losses+=1

                elif random_number<10 and random_number >=8:
                    pass

    def run_production(self):
        random_number = random.randint(1,3)
        self.surplus_artillery += round(24 * self.population * self.production_coefficient * self.num_of_cities *(1-self.conscription_law)) * random_number
        self.surplus_anti_tank += round(19 * self.population * self.production_coefficient * self.num_of_cities*(1-self.conscription_law)) * random_number
        self.surplus_machine_guns += round(27 * self.population * self.production_coefficient * self.num_of_cities*(1-self.conscription_law)) * random_number
        self.surplus_tanks += round(14 * self.population * self.production_coefficient * self.num_of_cities*(1-self.conscription_law)) * random_number
        self.surplus_motorized += round(10 * self.population * self.production_coefficient * self.num_of_cities*(1-self.conscription_law)) * random_number            

    def next_turn(self):

        self.internal_round_counter += 1

        self.take_attrition()
        self.train_men()
        self.run_production()

        if self.internal_round_counter % 2 == 0:
            self.resupply_all_units()

class World:
    def __init__(self):
        self.country_map = {}
        self.statistics = None

    def start_game(self):
        print("Welcome to the game!")
        print("This calculator has a default setup and a custom setup.")
        setup=input("Enter D for default setup or C for custom setup: ")
        if setup == "D":
            self.create_country("United Kingdom", "ENG","British", 607600, 2000, 0.015, 20, 0.000000035, 0.25, 120, 95, 135, 70, 50)
            self.create_country("France", "FRA", "French", 420000, 3000, 0.025, 26, 0.00000003, 0.1, 100, 80, 120, 60, 40)
            self.create_country("United States", "USA", "American", 1310000, 300, 0.005, 31, 0.000000025, 0.0, 200, 160, 240, 120, 80)
            self.create_country("Netherlands", "HOL", "Dutch", 170000, 800, 0.025, 9, 0.000000020, 0.2, 40, 32, 48, 24, 16)
            self.create_country("Germany", "GER", "German", 690000, 4000, 0.05, 34, 0.000000030, 0.2, 160, 128, 192, 96, 64)
            self.create_country("Italy", "ITA", "Italian", 440000, 1000, 0.05, 27, 0.00000002, 0.2, 80, 64, 96, 48, 32)
            self.create_country("Romania", "ROM", "Romanian", 200000, 500, 0.05, 10, 0.00000003, 0.25, 40, 32, 48, 24, 16)
            self.create_country("Hungary", "HUN", "Hungarian", 100000, 500, 0.05, 10, 0.00000003, 0.25, 40, 32, 48, 24, 16)
            self.create_country("Soviet Union", "SOV", "Russian", 1700000, 10000, 0.05, 29, 0.000000025, 0.0, 400, 320, 480, 240, 160)
            self.create_statistics()
        else:
            print("Custom setup not implemented yet!")
    
    def create_country(self, country_name, country_tag, population, trained_men, conscription_law, num_of_cities, production_coefficient, attrition_coefficient, surplus_artillery, surplus_anti_tank, surplus_machine_guns, surplus_tanks, surplus_motorized):
        country = Country(country_name, country_tag, population, trained_men, conscription_law, num_of_cities, production_coefficient, attrition_coefficient, surplus_artillery, surplus_anti_tank, surplus_machine_guns, surplus_tanks, surplus_motorized)
        self.country_map[country_tag] = country

    def create_statistics(self):
        statistics = Statistics(self.country_map)
        self.statistics = statistics
    
    def get_suffix(self, number):
        if number % 100 in [11, 12, 13]:
            suffix = "th"
        else:
            last_digit = number % 10
            if last_digit == 1:
                suffix = "st"
            elif last_digit == 2:
                suffix = "nd"
            elif last_digit == 3:
                suffix = "rd"
            else:
                suffix = "th"
        return suffix

    ##TODO:
    def start_battle(self):

        print("For items with multiple values, separate them with a comma.")
        print("When entering units type their number followed by a period and then the type of unit followed by another period and then its country tag. For example: 1.infantry.ENG, 2.armored.GER\n")

        name = input("Enter battle name: ")

        print()
        
        attacker_units = input("Enter attacker units: ")
        defender_units = input("Enter defender units: ")

        attacker_units_list = attacker_units.split(",")
        defender_units_list = defender_units.split(",")

        attacking_countries = []
        defending_countries = []
        attacking_units_object_list = []
        defending_units_object_list = []

        for unit in attacker_units_list:

            unit_number = int(unit.split(".")[0])
            unit_type = unit.split(".")[1]
            country_tag = unit.split(".")[2]

            attacking_countries.append(country_tag)

            unit = self.country_map[country_tag].get_unit(unit_number, unit_type)
            attacking_units_object_list.append(unit)

            print(unit)
            fit_for_battle = input("Is this unit fit for battle? (Y/N): ")

            if fit_for_battle == "Y":
                rear_guard = input("Is this unit a rear guard? (Y/N): ")

                if rear_guard == "Y":
                    unit.set_rear_guard()
                else:
                    unit.set_full_deployment()

            else:
                attacking_units_object_list.remove(unit)

        for unit in defender_units_list:

            unit_number = int(unit.split(".")[0])
            unit_type = unit.split(".")[1]
            country_tag = unit.split(".")[2]

            defending_countries.append(country_tag)

            unit = self.country_map[country_tag].get_unit(unit_number, unit_type)
            defending_units_object_list.append(unit)

            print(unit)
            fit_for_battle = input("Is this unit fit for battle? (Y/N): ")

            if fit_for_battle == "Y":
                rear_guard = input("Is this unit a rear guard? (Y/N): ")

                if rear_guard == "Y":
                    unit.set_rear_guard()
                else:
                    unit.set_full_deployment()

            else:
                defending_units_object_list.remove(unit)

        print(f"The Battle of {name} has begun with",end=" ")
        for country in attacking_countries:
            print(self.country_map[country].get_country_name(),end=" ")
        print("on the offensive",end=" ")
        for country in defending_countries:
            print(self.country_map[country].get_country_name(),end=" ")
        print("on the defensive")

        print("Here we will see",end=" ")
        for country in attacking_countries:
            print(self.country_map[country].get_country_name(),end=" ")
        print("attacking with the units:\n")
        for unit in attacking_units_object_list:
            print(f"{unit.get_nationality()} {unit.get_unit_number()}{self.get_suffix(unit_number)} {unit.get_unit_type()} Division",end=" ")


            print("with the following equipment:")

            if unit.get_unit_type().upper() == "INFANTRY":
                print(f"Manpower: {unit.get_manpower()}")
                print(f"Artillery: {unit.get_artillery()}")
                print(f"Machine Guns: {unit.get_machine_guns()}")
                print(f"Anti Tank: {unit.get_anti_tank()}")

            if unit.get_unit_type().upper() == "ARMOURED":
                print(f"Manpower: {unit.get_manpower()}")
                print(f"Tanks: {unit.get_tanks()}")
                print(f"Motorized: {unit.get_motorized()}")

            print(f"Veterancy: {unit.get_veterancy()}")
            print()

        print("Here we will also see",end=" ")
        for country in defending_countries:
            print(self.country_map[country].get_country_name(),end=" ")
        print("defending with the units:\n")
        for unit in defending_units_object_list:
            print(f"{unit.get_nationality()} {unit.get_unit_number()}{self.get_suffix(unit_number)} {unit.get_unit_type()} Division",end=" ")

            if unit.get_rear_guard():
                print("Performing Rear Guard Action", end=" ")
            
            print("with the following equipment:")

            if unit.get_unit_type().upper() == "INFANTRY":
                print(f"Manpower: {unit.get_manpower()}")
                print(f"Artillery: {unit.get_artillery()}")
                print(f"Machine Guns: {unit.get_machine_guns()}")
                print(f"Anti Tank: {unit.get_anti_tank()}")
            
            if unit.get_unit_type().upper() == "ARMOURED":
                print(f"Manpower: {unit.get_manpower()}")
                print(f"Tanks: {unit.get_tanks()}")
                print(f"Motorized: {unit.get_motorized()}")

            print(f"Veterancy: {unit.get_veterancy()}")

            if unit.get_incirclement():
                print("This unit is encircled, upon defeat it will be its final battle")
            
            print()
        
        print("The battle will now begin!")
        input("Press enter to continue and enter battle casualties...")
        
        for unit in attacking_units_object_list:
            print(f"For the {unit.get_nationality()} {unit.get_unit_number()}{self.get_suffix(unit_number)} {unit.get_unit_type()} Division")
            if unit.get_unit_type().upper() == "ARMOURED":
                remaining_men=input("how many men remain: ")
                remaining_tanks=input("how many tanks remain: ")
                remaining_motorized=input("how many motorized remain: ")

                manpower_losses = unit.get_deployed_manpower() - remaining_men
                tanks_losses = unit.get_deployed_tanks() - remaining_tanks
                motorized_losses = unit.get_deployed_motorized() - remaining_motorized

                unit.sum_unit_losses(manpower_losses + tanks_losses + motorized_losses)

                unit.set_manpower(remaining_men)
                unit.set_tanks(remaining_tanks)
                unit.set_motorized(remaining_motorized)

                #::TODO:: add losses to statistics

            if unit.get_unit_type().upper() == "INFANTRY":
                remaining_men=input("how many men remain: ")
                remaining_artillery=input("how many artillery remain: ")
                remaining_machine_guns=input("how many machine guns remain: ")
                remaining_anti_tank=input("how many anti tank remain: ")

                manpower_losses = unit.get_deployed_manpower() - remaining_men
                artillery_losses = unit.get_deployed_artillery() - remaining_artillery
                machine_guns_losses = unit.get_deployed_machine_guns() - remaining_machine_guns
                anti_tank_losses = unit.get_deployed_anti_tank() - remaining_anti_tank

                unit.sum_unit_losses(manpower_losses + artillery_losses + machine_guns_losses + anti_tank_losses)

                unit.set_manpower(remaining_men)
                unit.set_artillery(remaining_artillery)
                unit.set_machine_guns(remaining_machine_guns)
                unit.set_anti_tank(remaining_anti_tank)

                #::TODO:: add losses to statistics
            
            


            

            
        



    ##TODO:
    def enter_country_menu(self, country_tag):
        pass

    ##TODO:
    def enter_statistics_menu(self):
        pass

    ##TODO:
    def next_turn(self):
        pass

    ##TODO:
    def save_game(self):
        pass



    