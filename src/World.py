from Country import Country
from Statistics import Statistics
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    pass

class World:
    def __init__(self):
        self.country_map = {}
        self.statistics = None

    def start_game(self, setup):
        print("Welcome to the game!")
        print("This calculator has a default setup and a custom setup.")
        #setup=input("Enter D for default setup or C for custom setup: ")
        if setup == "D":
            self.create_country("United Kingdom", "ENG","British", 607600, 2000, 0.015, 20, 0.000000035, 0.25, 120, 95, 135, 70, 50, "pink",34,8)
            self.create_country("France", "FRA", "French", 420000, 3000, 0.025, 26, 0.00000003, 0.1, 100, 80, 120, 60, 40, "blue",72,14)
            self.create_country("United States", "USA", "American", 1310000, 300, 0.005, 31, 0.000000025, 0.0, 200, 160, 240, 120, 80, "lightblue",40,1)
            self.create_country("Netherlands", "HOL", "Dutch", 170000, 800, 0.025, 9, 0.000000020, 0.2, 40, 32, 48, 24, 16, "brown",27,0)
            self.create_country("Germany", "GER", "German", 690000, 4000, 0.05, 34, 0.000000030, 0.2, 160, 128, 192, 96, 64, "black",114,22)
            self.create_country("Italy", "ITA", "Italian", 440000, 1000, 0.05, 27, 0.00000002, 0.2, 80, 64, 96, 48, 32, "green",46,8)
            self.create_country("Romania", "ROM", "Romanian", 200000, 500, 0.05, 10, 0.00000003, 0.25, 40, 32, 48, 24, 16, "yellow",15,1)
            self.create_country("Hungary", "HUN", "Hungarian", 100000, 500, 0.05, 10, 0.00000003, 0.25, 40, 32, 48, 24, 16, "orange",15,1)
            self.create_country("Soviet Union", "SOV", "Russian", 1700000, 10000, 0.05, 29, 0.000000025, 0.0, 400, 320, 480, 240, 160, "red",199,25)
            self.create_statistics()
        else:
            print("Custom setup not implemented yet!")
    
    def create_country(self, country_name, country_tag, nationality, population, trained_men, conscription_law, num_of_cities, production_coefficient, attrition_coefficient, surplus_artillery, surplus_anti_tank, surplus_machine_guns, surplus_tanks, surplus_motorized, color, infantry, armored):
        country = Country(country_name, country_tag, nationality, population, trained_men, conscription_law, num_of_cities, production_coefficient, attrition_coefficient, surplus_artillery, surplus_anti_tank, surplus_machine_guns, surplus_tanks, surplus_motorized, color)
        for i in range(infantry):
            country.spawn_infantry_free(1)
        for i in range(armored):
            country.spawn_armored_free(1)
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
    
    def process_units(self, unit_list, defending):

        units_object_list = []
        country_names = []

        for unit in unit_list:
            unit_number = int(unit.split(".")[0])
            unit_type_tag = unit.split(".")[1]
            country_tag = unit.split(".")[2]
            if unit_type_tag == "inf":
                unit_type = "infantry"
            elif unit_type_tag == "arm":
                unit_type = "armored"


            unit = self.country_map[country_tag].get_unit(unit_number, unit_type)
            units_object_list.append(unit)
            country_names.append(self.country_map[country_tag].country_name)

            print(unit)
            fit_for_battle = input("Is this unit fit for battle? (Y/N): ")

            if fit_for_battle.upper() == "N":
                print(f"Removing unit from battle\n")
                units_object_list.remove(unit)
                continue

            if defending:
                rear_guard = input("Is this unit a rear guard? (Y/N): ")
                if rear_guard == "Y":
                    unit.set_rear_guard()
                else:
                    unit.set_full_deployment()
            else:
                unit.set_full_deployment()
            print()
            

        return units_object_list, country_names

    def process_casualties(self, unit_list, defending):
        total_losses = [0,0,0,0,0,0]
        for unit in unit_list:
            country = self.country_map[unit.country_tag]
            unit_number = unit.unit_number
            unit_type = unit.unit_type

            print(f"For the {unit.nationality} {unit.unit_number}{self.get_suffix(unit_number)} {unit.unit_type} Division")
            remaining_men=int(input("how many men remain: "))
            total_losses[0]+= unit.deployed_manpower-remaining_men
            if unit.unit_type.upper() == "ARMORED":
                remaining_tanks=int(input("how many tanks remain: "))
                remaining_motorized=int(input("how many motorized remain: "))

                
                total_losses[4]+= unit.deployed_tanks-remaining_tanks
                total_losses[5]+= unit.deployed_motorized-remaining_motorized


                equipment_list = (remaining_men, 0, 0, 0, remaining_tanks, remaining_motorized)
                country.take_casualties(unit_number, unit_type, equipment_list)
                             

            if unit.unit_type.upper() == "INFANTRY":
                remaining_artillery=int(input("how many artillery remain: "))
                remaining_machine_guns=int(input("how many machine guns remain: "))
                remaining_anti_tank=int(input("how many anti tank remain: "))

                total_losses[1]+= unit.deployed_artillery-remaining_artillery
                total_losses[2]+= unit.deployed_machine_guns-remaining_machine_guns
                total_losses[3]+= unit.deployed_anti_tank-remaining_anti_tank

                equipment_list = (remaining_men, remaining_artillery, remaining_machine_guns, remaining_anti_tank, 0, 0)
                country.take_casualties(unit_number, unit_type, equipment_list)
            
            if defending:
                incirclement = input("Is this unit now encircled? (Y/N): ")
                if incirclement == "Y":
                    unit.incirclement = True
            
        return total_losses
            
    def display_involved_units(self, unit_list):

        for unit in unit_list:
            print(f"{unit.nationality} {unit.unit_number}{self.get_suffix(unit.unit_number)} {unit.unit_type} Division",end=" ")

            if unit.rear_guard:
                print("Performing Rear Guard Action", end=" ")
            
            print("with the following equipment:")

            if unit.unit_type.upper() == "INFANTRY":
                print(f"Manpower: {unit.deployed_manpower}")
                print(f"Artillery: {unit.deployed_artillery}")
                print(f"Machine Guns: {unit.deployed_machine_guns}")
                print(f"Anti Tank: {unit.deployed_anti_tank}")
            
            if unit.unit_type.upper() == "ARMORED":
                print(f"Manpower: {unit.deployed_manpower}")
                print(f"Tanks: {unit.deployed_tanks}")
                print(f"Motorized: {unit.deployed_motorized}")

            print(f"Veterancy: {unit.veterancy}")

            if unit.incirclement:
                print("This unit is encircled, upon defeat it will be its final battle")
            
            print()

    def check_validity_unit_list(self, unit_list):
        for unit in unit_list:
            try:
                unit_number = int(unit.split(".")[0])
            except:
                print(f"Invalid unit number: {unit}")
                return False
            try:
                unit_type_tag = unit.split(".")[1]
                country_tag = unit.split(".")[2]
            except:
                print(f"Invalid unit: {unit}")
                return False
            if unit_type_tag not in ["inf", "arm"]:
                print(f"Invalid unit type: {unit}")
                return False
            else:
                if unit_type_tag == "inf":
                    unit_type_tag = "infantry"
                elif unit_type_tag == "arm":
                    unit_type_tag = "armored"
            if country_tag not in self.country_map:
                print(f"Invalid country tag: {unit}")
                return False
            if self.country_map[country_tag].get_unit(unit_number, unit_type_tag) == None:
                print(f"Invalid unit number: {unit}")
                return False
            if len(unit.split(".")) != 3:
                print(f"Invalid unit: {unit}")
                return False
        return True
    
    def end_of_battle_update(self, attacker_units_object_list, defender_units_object_list):
        for unit in attacker_units_object_list:
            unit.after_action_update()
        for unit in defender_units_object_list:
            unit.after_action_update()

    def start_battle(self):

        print("For items with multiple values, separate them with a space.")
        print("When entering units type their number followed by a period and then the type of unit followed by another period and then its country tag. For example: 1.inf.ENG 2.arm.GER\n")

        name = input("Enter battle name: ")

        print()
            
        while True:
            attacker_units = input("Enter attacker units: ")
            defender_units = input("Enter defender units: ")

            attacker_units_list = attacker_units.split(" ")
            defender_units_list = defender_units.split(" ")
            if self.check_validity_unit_list(attacker_units_list) and self.check_validity_unit_list(defender_units_list):
                break
            else:
                print("Invalid unit list, try again\n")

        attacking_countries = []
        defending_countries = []
        attacking_units_object_list = []
        defending_units_object_list = []

        try:
            attacking_units_object_list, attacking_countries = self.process_units(attacker_units_list, False)
            defending_units_object_list, defending_countries = self.process_units(defender_units_list, True)
        except:
            print("Something went wrong with the processing of units")
            

        print(f"The Battle of {name} has begun with",end=" ")
        for country in attacking_countries:
            print(country,end=" ")
        print("on the offensive",end=" ")
        for country in defending_countries:
            print(country,end=" ")
        print("on the defensive")

        print("Here we will see",end=" ")
        for country in attacking_countries:
            print(country,end=" ")
        print("attacking with the units:\n")
        self.display_involved_units(attacking_units_object_list)

        print("Here we will also see",end=" ")
        for country in defending_countries:
            print(country,end=" ")
        print("defending with the units:\n")
        self.display_involved_units(defending_units_object_list)
            
        print("The battle will now begin!")
        input("Press enter to continue and enter battle casualties...")
            
        try:
            attacker_total_losses = self.process_casualties(attacking_units_object_list, False)
            defender_total_losses = self.process_casualties(defending_units_object_list, True)
        except:
            print("Something went wrong with the processing of casualties")

            
        winner = input("Who won the battle?: ")

        battle = self.statistics.new_battle(name, winner, attacking_countries, defending_countries, attacker_total_losses, defender_total_losses)

        print("The battle has ended!")
        print("Post battle statistics:")
        print(battle)
        self.end_of_battle_update(attacking_units_object_list, defending_units_object_list)
        input("Press enter to continue...")


    def enter_country_menu(self, country_tag):
        
        while True:   
            country = self.country_map[country_tag]
            print(f"[{country.country_name}]\n\n1. View Unit Menu\n2. View Production Menu\n3. View Country Statistics Menu\n4. View Stockpile Menu\n5. View Losses Menu\n6. Return to Main Menu\n")
            choice = input("Enter choice: ")
            if choice == "1":
                self.enter_unit_menu(country)
                clear()
            elif choice == "2":
                self.enter_production_menu(country)
                clear()
            elif choice == "3":
                self.enter_country_statistics_menu(country)
                clear()
            elif choice == "4":
                self.enter_stockpile_menu(country)
                clear()
            elif choice == "5":
                self.enter_losses_menu(country)
                clear()
            elif choice == "6":
                break

    def developer_settings(self, units, type):
        while True:
            print("Would you like to modify any units? (enter 0 to return to unit menu)")
            modify = input("Enter Y/N: ")
            if modify.upper() == "Y":
                unit_num = int(input("Enter unit number: "))
                unit = units[unit_num]
                self.modify_unit(unit, "infantry")
            elif modify == "0":
                break

    def enter_unit_menu(self, country):
        while True:
            print(f"[{country.country_name} Unit Menu]")
            print("1. View Infantry\n2. View Armored\n3. Make New Unit\n4. Delete unit\n5. Return to Country Menu\n")
            choice = input("Enter choice: ")
            if choice.startswith("1"):
                infantry = country.infantry_divisions
                for unit in infantry:
                    print(infantry[unit],"\n")
                if choice == "1d":
                    self.developer_settings(infantry, "infantry")
                    
            elif choice.startswith("2"):
                armored = country.armored_divisions
                for unit in armored:
                    print(armored[unit],"\n")
                if choice == "2d":
                    self.developer_settings(armored, "armored")
                
            elif choice == "3":
                print(f"Currently we can build {country.find_new_infantry_availability()} new infantry units and {country.find_new_armored_availability()} new armored units\n")
                while True:
                    print("1. Build Infantry\n2. Build Armored\n3. Return to Unit Menu\n")
                    choice = input("Enter choice: ")
                    if choice == "1":
                        country.spawn_infantry(1)
                    elif choice == "2":
                        country.spawn_armored(1)
                    elif choice == "3":
                        break
            elif choice == "4":
                while True:
                    print("Enter the unit you want to delete in the format: unit number.unit type ----> 5.inf")
                    print("Enter 0 to return to unit menu\n")
                    unit = input("Enter unit: ")
                    if unit == "0":
                        break
                    else:
                        unit_number = int(unit.split(".")[0])
                        unit_type_tag = unit.split(".")[1]
                        if unit_type_tag == "inf":
                            unit_type = "infantry"
                        elif unit_type_tag == "arm":
                            unit_type = "armored"
                        country.delete_unit(unit_number, unit_type)
            elif choice == "5":
                break
    
    def modify_unit(self, unit, type):
        if type == "infantry":
            unit.manpower = (int(input("Enter manpower: ")))
            unit.artillery = (int(input("Enter artillery: ")))
            unit.machine_guns = (int(input("Enter machine guns: ")))
            unit.anti_tank = (int(input("Enter anti tank: ")))
            unit.veterancy = (int(input("Enter veterancy: ")))
        elif type == "armored":
            unit.manpower = (int(input("Enter manpower: ")))
            unit.tanks = (int(input("Enter tanks: ")))
            unit.motorized = (int(input("Enter motorized: ")))
            unit.veterancy = (int(input("Enter veterancy: ")))

    def enter_production_menu(self, country):
        while True:
            print(f"[{country.country_name} Production Menu]\n\n1. View Production\n2. Modify Production\n3. Return to Country Menu\n")
            choice = input("Enter choice: ")
            if choice == "1":
                print("Estimated Production of Equipment: (proportion --> estimated production))")
                print(f"Artillery: {country.porportions['artillery']} ---> {self.calculate_estimated_production_of_equipment('artillery', country)}")
                print(f"Machine Guns: {country.porportions['machine_guns']} ---> {self.calculate_estimated_production_of_equipment('machine guns', country)}")
                print(f"Anti Tank: {country.porportions['anti_tank']} ---> {self.calculate_estimated_production_of_equipment('anti tank', country)}")
                print(f"Tanks: {country.porportions['tanks']} ---> {self.calculate_estimated_production_of_equipment('tanks', country)}")
                print(f"Motorized: {country.porportions['motorized']} ---> {self.calculate_estimated_production_of_equipment('motorized', country)}\n")
            elif choice == "2":
                print("Enter the proportion of production you want to reallocate to an equipment type and where you want to reallocate it from. ex. 1-artillery-machine_guns where 1 is the proportion of production you want to reallocate to artillery from machine guns")
                change = input("Enter change: ")
                change = change.split("-")
                proportion = float(change[0])
                equipment_to = change[1]
                equipment_from = change[2]
                country.porportions[equipment_to] += proportion
                country.porportions[equipment_from] -= proportion


            elif choice == "3":
                break

    def calculate_estimated_production_of_equipment(self, equipment, country):
        population = country.population
        production_coefficient = country.production_coefficient
        num_of_cities = country.num_of_cities
        conscription_law = country.conscription_law

        if equipment == "artillery":
            return round(24 * population * production_coefficient * num_of_cities *(1-conscription_law)) * 2
        elif equipment == "machine guns":
            return round(20 * population * production_coefficient * num_of_cities *(1-conscription_law)) * 2
        elif equipment == "anti tank":
            return round(28 * population * production_coefficient * num_of_cities *(1-conscription_law)) * 2
        elif equipment == "tanks":
            return round(15 * population * production_coefficient * num_of_cities *(1-conscription_law)) * 2
        elif equipment == "motorized":
            return round(11 * population * production_coefficient * num_of_cities *(1-conscription_law)) * 2

    def enter_country_statistics_menu(self, country):
        while True:
            print(f"""[{country.country_name}]\n\n
Country Name:{country.country_name}
Country Tag:{country.country_tag}
Population: {country.population}
Number of Cities: {country.num_of_cities}
Population per City:{country.population_per_city}
Production Coefficient: {country.production_coefficient} 
Attrition Coefficient: {country.attrition_coefficient}
Conscription Law: {country.conscription_law}
Trained Men: {country.trained_men}
Eligible Men: {country.eligible_men}
                """)
            print("1. Modify City Count\n2. Modify Production Coefficent\n3. Modify Attrition Coefficent\n4. Modify Conscription Law\n5. Return to Country Menu\n")
            choice=input("Enter Command: ")
            if choice == "1":
                country.set_num_of_cities(country.num_of_cities-int(input("Enter number of cities lost: ")))
                print(f"New number of cities: {country.num_of_cities}")
            elif choice == "2":
                country.production_coefficient = (float(input("Enter new production coefficient as a decimal [0,10]: "))*(10**-8))
            elif choice == "3":
                country.attrition_coefficient = (float(input("Enter new attrition coefficient as a decimal [0,1]: ")))
            elif choice == "4":
                country.set_conscription_law(float(input("Enter new conscription law as a decimal [0,1]: ")))
            elif choice == "5":
                break
            

    def enter_stockpile_menu(self, country):
        while True:
            print(f"""[Stockpile Menu]\n\n
Surplus Artillery: {country.surplus_artillery}
Surplus Anti Tank: {country.surplus_anti_tank}
Surplus Machine Guns: {country.surplus_machine_guns}
Surplus Tanks: {country.surplus_tanks}
Surplus Motorized: {country.surplus_motorized}              
            """)
            print("To send equipment to another country enter the equipment type, amount, and the country tag. ex. artillery.100.ENG")
            print("1. Send Equipment\n2. Return to Country Menu\n")
            choice = input("Enter choice: ")
            if choice == "1":
                equipment = input("Enter equipment: ")
                equipment = equipment.split(".")
                equipment_type = equipment[0]
                equipment_amount = int(equipment[1])
                equipment_country_tag = equipment[2]
                if equipment_type == "artillery":
                    country.surplus_artillery = (country.surplus_artillery-equipment_amount)
                    self.country_map[equipment_country_tag].surplus_artillery = (self.country_map[equipment_country_tag].surplus_artillery+equipment_amount)
                elif equipment_type == "anti_tank":
                    country.surplus_anti_tank = (country.surplus_anti_tank-equipment_amount)
                    self.country_map[equipment_country_tag].surplus_anti_tank = (self.country_map[equipment_country_tag].surplus_anti_tank+equipment_amount)
                elif equipment_type == "machine_guns":
                    country.surplus_machine_guns = (country.surplus_machine_guns-equipment_amount)
                    self.country_map[equipment_country_tag].surplus_machine_guns = (self.country_map[equipment_country_tag].surplus_machine_guns+equipment_amount)
                elif equipment_type == "tanks":
                    country.surplus_tanks = (country.surplus_tanks-equipment_amount)
                    self.country_map[equipment_country_tag].surplus_tanks = (self.country_map[equipment_country_tag].surplus_tanks+equipment_amount)
                elif equipment_type == "motorized":
                    country.surplus_motorized = (country.surplus_motorized-equipment_amount)
                    self.country_map[equipment_country_tag].surplus_motorized = (self.country_map[equipment_country_tag].get_surplus_motorized+equipment_amount)
            elif choice == "2":
                break
        
    def enter_losses_menu(self, country):
        while True:
            print(f"""[Losses Menu]\n\n
Manpower Losses: {country.manpower_losses}
Artillery Losses: {country.artillery_losses}
Anti Tank Losses: {country.anti_tank_losses}
Machine Guns Losses: {country.machine_guns_losses}
Tanks Losses: {country.tanks_losses}
Motorized Losses: {country.motorized_losses}
            """)
            print("1. Return to Country Menu\n")
            choice = input("Enter choice: ")
            if choice == "1":
                break

    def enter_statistics_menu(self):
        while True:
            print(f"""[Statistics Menu]\n\n
1. View Battles\n2. View Graphs\n3. Return to Main Menu\n
            """)
            choice = input("Enter choice: ")
            
            if choice == "1":
                battle_list = self.statistics.battle_list

                for battle in battle_list:
                    print(battle.battle_name)

                battle_name = input("Enter battle name: ")
                battle = self.statistics.get_battle(battle_name)

                print(battle)
                input("Press enter to continue...")

            elif choice == "2":
                while True:
                    print(f"""[Graphs Menu]\n\n
1. View Stockpile Graphs for all Countries\n2. View Equipment Losses for all Countries\n3. View Manpower Losses for all Countries\n4. Return to Statistics Menu
                            """)
                    choice = input("Enter choice: ")
                    if choice == "1":
                        self.statistics.graph_stockpile_for_all_countries()
                    elif choice == "2":
                        self.statistics.graph_equipment_losses_for_all()
                    elif choice == "3":
                        self.statistics.graph_manpower_losses_for_all()
                    elif choice == "4":
                        break

            elif choice == "3":
                break

    def next_turn(self):
        self.statistics.next_turn()
        for country_tag in self.country_map:
            self.country_map[country_tag].next_turn()

