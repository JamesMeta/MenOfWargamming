from Infantry import Infantry
from Armored import Armored
import random 


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

        self.porportions = {"artillery": 24, "anti_tank": 19, "machine_guns": 27, "tanks": 14, "motorized": 10}

        self.internal_round_counter = 0

        self.country_colour = colour
    
    def set_conscription_law(self, conscription_law):
        if conscription_law >= 0 and conscription_law <= 1:
            self.conscription_law = conscription_law
            self.eligible_men = self.population * self.conscription_law
        else:
            self.conscription_law = 0

    def set_num_of_cities(self, num_of_cities):
        if num_of_cities > 0:
            self.num_of_cities = num_of_cities
            self.population = self.population_per_city * self.num_of_cities
            
        else:
            self.num_of_cities = 0

    def find_avaliable_unit_number(self, unit_type):
        if unit_type == "infantry":

            for i in range(1,len(self.infantry_divisions)):
                unit_number = i
                if unit_number not in self.infantry_divisions:
                    return unit_number
            
            return len(self.infantry_divisions)+1
        
        elif unit_type == "armored":

            for i in range(1,len(self.armored_divisions)):
                unit_number = i
                if unit_number not in self.armored_divisions:
                    return unit_number
            
            return len(self.armored_divisions)+1
            
    def get_unit(self,unit_number, unit_type):
        if unit_type == "infantry":
            return self.infantry_divisions[unit_number]
        elif unit_type == "armored":
            return self.armored_divisions[unit_number]
        

    def spawn_infantry_free(self, veterancy):
        unit_number = self.find_avaliable_unit_number("infantry")
        self.infantry_divisions[unit_number] = Infantry(unit_number, veterancy, self.nationality, self.country_tag)
        print(f"Spawned Infantry Division {unit_number} for {self.country_name}")
    
    def spawn_armored_free(self, veterancy):
        unit_number = self.find_avaliable_unit_number("armored")
        self.armored_divisions[unit_number] = Armored(unit_number, veterancy, self.nationality, self.country_tag)
        print(f"Spawned Armored Division {unit_number} for {self.country_name}")

    def spawn_infantry(self, veterancy):
        if self.surplus_artillery < 3 or self.surplus_machine_guns < 2 or self.surplus_anti_tank < 2 or self.trained_men < 100:
            print(f"Insufficient equipment for {self.country_name} to spawn Infantry Division")
            return
        else:
            unit_number = self.find_avaliable_unit_number("infantry")
            self.infantry_divisions[unit_number] = Infantry(unit_number, veterancy, self.nationality, self.country_tag)
            self.surplus_artillery -= 3
            self.surplus_machine_guns -= 2
            self.surplus_anti_tank -= 2
            self.trained_men -= 100
            print(f"Spawned Infantry Division {unit_number} for {self.country_name}")
    
    def spawn_armored(self, veterancy):
        if self.surplus_tanks < 6 or self.surplus_motorized < 5 or self.trained_men < 60:
            print(f"Insufficient equipment for {self.country_name} to spawn Armored Division")
            return
        else:
            unit_number = self.find_avaliable_unit_number("armored")
            self.armored_divisions[unit_number] = Armored(unit_number, veterancy, self.nationality, self.country_tag)
            self.surplus_tanks -= 6
            self.surplus_motorized -= 5
            self.trained_men -= 60
    
    def delete_unit(self, unit_number, unit_type):
        if unit_type == "infantry":
            del self.infantry_divisions[unit_number]
        elif unit_type == "armored":
            del self.armored_divisions[unit_number]
        
        print(f"Deleted {unit_type} Division {unit_number} for {self.country_name}")
        input("Press Enter to continue...")

    #remaining equipment list structure [men, artillery, machine_guns, anti_tank, tanks, motorized]
    def take_casualties(self, unit_number, unit_type, remaining_equipment_list):
        if unit_type == "infantry":

            unit = self.infantry_divisions[unit_number]

            previous_manpower = unit.deployed_manpower
            previous_artillery = unit.deployed_artillery
            previous_anti_tank = unit.deployed_anti_tank
            previous_machine_guns = unit.deployed_machine_guns

            current_manpower = remaining_equipment_list[0]
            current_artillery = remaining_equipment_list[1]
            current_machine_guns = remaining_equipment_list[2]
            current_anti_tank = remaining_equipment_list[3]

            self.manpower_losses += previous_manpower - current_manpower
            self.anti_tank_losses += previous_anti_tank - current_anti_tank
            self.artillery_losses += previous_artillery - current_artillery
            self.machine_guns_losses += previous_machine_guns - current_machine_guns


            unit.manpower = (unit.manpower + current_manpower)
            unit.artillery = (unit.artillery + current_artillery)
            unit.anti_tank = (unit.anti_tank + current_anti_tank)
            unit.machine_guns = (unit.machine_guns + current_machine_guns)

            if unit.manpower == 0:
                self.delete_unit(unit_number, unit_type)

        elif unit_type == "armored":
            
            unit = self.armored_divisions[unit_number]

            previous_manpower = unit.deployed_manpower
            previous_tanks = unit.deployed_tanks
            previous_motorized = unit.deployed_motorized

            current_manpower = remaining_equipment_list[0]
            current_tanks = remaining_equipment_list[4]
            current_motorized = remaining_equipment_list[5]

            self.manpower_losses+= previous_manpower - current_manpower
            self.tanks_losses+= previous_tanks - current_tanks
            self.motorized_losses+= previous_motorized - current_motorized


            unit.manpower = (unit.manpower + current_manpower)
            unit.tanks = (unit.tanks + current_tanks)
            unit.motorized = (unit.motorized + current_motorized)

            if unit.manpower == 0:
                self.delete_unit(unit_number, unit_type)

    def change_unit_status(self, unit_number, unit_type):
        if unit_type == "infantry":
            unit = self.infantry_divisions[unit_number]
            unit.incirclement(not unit.incirclement)
        elif unit_type == "armored":
            unit = self.armored_divisions[unit_number]
            unit.incirclement(not unit.incirclement)
    
    def understrength_units_exist(self, unit_type):
        if unit_type == "infantry":
            for unit_number in self.infantry_divisions:
                if self.infantry_divisions[unit_number].manpower < 100 or self.infantry_divisions[unit_number].artillery < 3 or self.infantry_divisions[unit_number].machine_guns < 2 or self.infantry_divisions[unit_number].anti_tank < 2:
                    return True
            return False
        elif unit_type == "armored":
            for unit_number in self.armored_divisions:
                if self.armored_divisions[unit_number].manpower < 60 or self.armored_divisions[unit_number].tanks < 6 or self.armored_divisions[unit_number].motorized < 5:
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
            if unit.incirclement == False:
                men_gap += 100 - unit.manpower
                artillery_gap += 3 - unit.artillery
                anti_tank_gap += 2 - unit.anti_tank
                machine_gun_gap += 2 - unit.machine_guns
        
        for unit in self.armored_divisions.values():
            if unit.incirclement == False:
                men_gap += 60 - unit.manpower
                tanks_gap += 6 - unit.tanks
                motorized_gap += 5 - unit.motorized

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
                if unit.incirclement == False:
                    if unit.manpower < 60:
                        unit.manpower=(unit.manpower+1)
                        replacement_manpower -= 1

                    if unit.tanks < 6:
                        unit.tanks = (unit.tanks+1)
                        replacement_tanks -= 1

                    if unit.motorized < 5:
                        unit.motorized = (unit.motorized+1)
                        replacement_motorized -= 1
        
        replacement_manpower += guaranteed_infantry_replacements

        while replacement_manpower > 0 and self.understrength_units_exist("infantry"):
            for unit in self.infantry_divisions.values():
                if unit.incirclement == False:
                    if unit.manpower < 100:
                        unit.manpower = (unit.manpower+1)
                        replacement_manpower -= 1
                    
                    if unit.artillery < 3:
                        unit.artillery = (unit.artillery+1)
                        replacement_artillery -= 1

                    if unit.machine_guns < 2:
                        unit.machine_guns = (unit.machine_guns+1)
                        replacement_machine_guns -= 1
                    
                    if unit.anti_tank < 2:
                        unit.anti_tank = (unit.anti_tank+1)
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
            army_size += unit.manpower
        for unit in self.armored_divisions.values():
            army_size += unit.manpower
        return army_size

    def train_men(self):
        army_size = self.find_army_size()
        new_trainees = (army_size//208)
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
                    unit.artillery = (unit.artillery-1)
                    unit.machine_guns = (unit.machine_guns-1)
                    unit.anti_tank = (unit.anti_tank-1)

                    self.artillery_losses+=1
                    self.machine_guns_losses+=1
                    self.anti_tank_losses+=1
                
                elif random_number<4 and random_number >=2:
                    unit.machine_guns = (unit.machine_guns-1)
                    unit.anti_tank = (unit.anti_tank-1)

                    self.machine_guns_losses+=1
                    self.anti_tank_losses+=1
                
                elif random_number<6 and random_number >=4:
                    unit.artillery = (unit.artillery-1)
                    unit.machine_guns = (unit.machine_guns-1)

                    self.artillery_losses+=1
                    self.machine_guns_losses+=1

                elif random_number<8 and random_number >=6:
                    unit.artillery = (unit.artillery-1)

                    self.artillery_losses+=1

                elif random_number<10 and random_number >=8:
                    pass
        
        for unit in self.armored_divisions.values():
            random_number = random.randint(1,round((1-self.attrition_coefficient)*100))
            if random_number > 60:
                random_number = random.randint(1,10)
                if random_number<2:
                    unit.tanks = (unit.tanks-2)
                    unit.motorized = (unit.motorized-2)

                    self.tanks_losses+=2
                    self.motorized_losses+=2
                
                elif random_number<4 and random_number >=2:
                    unit.tanks = (unit.tanks-2)
                    unit.motorized = (unit.motorized-1)

                    self.tanks_losses+=2
                    self.motorized_losses+=1
                
                elif random_number<6 and random_number >=4:
                    unit.tanks = (unit.tanks-1)
                    unit.motorized = (unit.motorized-1)

                    self.tanks_losses+=1
                    self.motorized_losses+=1

                elif random_number<8 and random_number >=6:
                    unit.tanks = (unit.tanks-1)

                    self.tanks_losses+=1

                elif random_number<10 and random_number >=8:
                    pass

    def run_production(self):
        random_number = random.randint(1,3)
        self.surplus_artillery += round(self.porportions['artillery'] * self.population * self.production_coefficient * self.num_of_cities *(1-self.conscription_law)) * random_number
        self.surplus_anti_tank += round(self.porportions['anti_tank'] * self.population * self.production_coefficient * self.num_of_cities*(1-self.conscription_law)) * random_number
        self.surplus_machine_guns += round(self.porportions['machine_guns'] * self.population * self.production_coefficient * self.num_of_cities*(1-self.conscription_law)) * random_number
        self.surplus_tanks += round(self.porportions['tanks'] * self.population * self.production_coefficient * self.num_of_cities*(1-self.conscription_law)) * random_number
        self.surplus_motorized += round(self.porportions['motorized'] * self.population * self.production_coefficient * self.num_of_cities*(1-self.conscription_law)) * random_number            

    def next_turn(self):

        self.internal_round_counter += 1

        self.take_attrition()
        self.train_men()
        self.run_production()

        if self.internal_round_counter % 2 == 0:
            self.resupply_all_units()

    def find_new_infantry_availability(self):
        trained_men = self.trained_men//100
        surplus_artillery = self.surplus_artillery//3
        surplus_machine_guns = self.surplus_machine_guns//2
        surplus_anti_tank = self.surplus_anti_tank//2

        lowest = min(trained_men, surplus_artillery, surplus_machine_guns, surplus_anti_tank)
        return lowest
    
    def find_new_armored_availability(self):
        trained_men = self.trained_men//60
        surplus_tanks = self.surplus_tanks//6
        surplus_motorized = self.surplus_motorized//5
        surplus_anti_tank = self.surplus_anti_tank//2

        lowest = min(trained_men, surplus_tanks, surplus_motorized, surplus_anti_tank)
        return lowest


