from Country import Country
from Statistics import Statistics

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
            country_names.append(self.country_map[country_tag].get_country_name())

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
            country = self.country_map[unit.get_country_tag()]
            unit_number = unit.get_unit_number()
            unit_type = unit.get_unit_type()

            print(f"For the {unit.get_nationality()} {unit.get_unit_number()}{self.get_suffix(unit_number)} {unit.get_unit_type()} Division")
            remaining_men=int(input("how many men remain: "))
            total_losses[0]+= unit.get_deployed_manpower()-remaining_men
            if unit.get_unit_type().upper() == "ARMORED":
                remaining_tanks=int(input("how many tanks remain: "))
                remaining_motorized=int(input("how many motorized remain: "))

                
                total_losses[4]+= unit.get_deployed_tanks()-remaining_tanks
                total_losses[5]+= unit.get_deployed_motorized()-remaining_motorized


                equipment_list = (remaining_men, 0, 0, 0, remaining_tanks, remaining_motorized)
                country.take_casualties(unit_number, unit_type, equipment_list)
                             

            if unit.get_unit_type().upper() == "INFANTRY":
                remaining_artillery=int(input("how many artillery remain: "))
                remaining_machine_guns=int(input("how many machine guns remain: "))
                remaining_anti_tank=int(input("how many anti tank remain: "))

                total_losses[1]+= unit.get_deployed_artillery()-remaining_artillery
                total_losses[2]+= unit.get_deployed_machine_guns()-remaining_machine_guns
                total_losses[3]+= unit.get_deployed_anti_tank()-remaining_anti_tank

                equipment_list = (remaining_men, remaining_artillery, remaining_machine_guns, remaining_anti_tank, 0, 0)
                country.take_casualties(unit_number, unit_type, equipment_list)
            
            if defending:
                incirclement = input("Is this unit now encircled? (Y/N): ")
                if incirclement == "Y":
                    unit.set_incirclement()
            
        return total_losses
            
    def display_involved_units(self, unit_list):

        for unit in unit_list:
            print(f"{unit.get_nationality()} {unit.get_unit_number()}{self.get_suffix(unit.get_unit_number())} {unit.get_unit_type()} Division",end=" ")

            if unit.get_rear_guard():
                print("Performing Rear Guard Action", end=" ")
            
            print("with the following equipment:")

            if unit.get_unit_type().upper() == "INFANTRY":
                print(f"Manpower: {unit.get_deployed_manpower()}")
                print(f"Artillery: {unit.get_deployed_artillery()}")
                print(f"Machine Guns: {unit.get_deployed_machine_guns()}")
                print(f"Anti Tank: {unit.get_deployed_anti_tank()}")
            
            if unit.get_unit_type().upper() == "ARMORED":
                print(f"Manpower: {unit.get_deployed_manpower()}")
                print(f"Tanks: {unit.get_deployed_tanks()}")
                print(f"Motorized: {unit.get_deployed_motorized()}")

            print(f"Veterancy: {unit.get_veterancy()}")

            if unit.get_incirclement():
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

    ##TODO:
    def enter_country_menu(self, country_tag):
        
        while True:   
            country = self.country_map[country_tag]
            print(f"[{country.get_country_name()}]\n\n1. View Units\n2. View Production\n3. View Country Statistics\n4. View Stockpile\n5. View Losses\n6. Return to Main Menu\n")
            choice = input("Enter choice: ")
            if choice == "1":
                self.enter_unit_menu(country)
            elif choice == "2":
                self.enter_production_menu(country)
            elif choice == "3":
                self.enter_statistics_menu(country)
            elif choice == "4":
                self.enter_stockpile_menu(country)
            elif choice == "5":
                self.enter_losses_menu(country)
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
            print(f"[{country.get_country_name()} Unit Menu]")
            print("1. View Infantry\n2. View Armored\n3. Make New Unit\n4. Delete unit\n5. Return to Country Menu\n")
            choice = input("Enter choice: ")
            if choice.startswith("1"):
                infantry = country.get_infantry_divisions()
                for unit in infantry:
                    print(infantry[unit],"\n")
                if choice == "1d":
                    self.developer_settings(infantry, "infantry")
                    
            elif choice.startswith("2"):
                armored = country.get_armored_divisions()
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
            unit.set_manpower(int(input("Enter manpower: ")))
            unit.set_artillery(int(input("Enter artillery: ")))
            unit.set_machine_guns(int(input("Enter machine guns: ")))
            unit.set_anti_tank(int(input("Enter anti tank: ")))
            unit.set_veterancy(int(input("Enter veterancy: ")))
        elif type == "armored":
            unit.set_manpower(int(input("Enter manpower: ")))
            unit.set_tanks(int(input("Enter tanks: ")))
            unit.set_motorized(int(input("Enter motorized: ")))
            unit.set_veterancy(int(input("Enter veterancy: ")))

    ##TODO:
    def enter_production_menu(self, country):
        pass

    ##TODO:
    def enter_statistics_menu(self, country):
        while True:
            print(f"""[{country.get_country_name()}]\n\nCountry Name:{country.get_country_name()}\nCountry Tag:{country.get_country_tag()}\n
                Population: {country.get_population()}\nNumber of Cities: {country.get_num_of_cities()}\nPopulation per City:{country.get_population_per_city()}
                Production Coefficient: {country.get_production_coefficient()} Attrition Coefficient: {country.get_attrition_coefficient()}
                Surplus Artillery: {country.get_surplus_artillery()}\nSurplus Anti Tank: {country.get_surplus_anti_tank()}\nSurplus Machine Guns: {country.get_surplus_machine_guns()}\nSurplus Tanks: {country.get_surplus_tanks()}\nSurplus Motorized: {country.get_surplus_motorized()}
                Conscription Law: {country.get_conscription_law()}\nTrained Men: {country.get_trained_men()}\nEligible Men: {country.get_eligible_men()}
                """)
            print("1. Modify City Count\n2. Modify Production Coefficent\n3. Modify Attrition Coefficent\n4. Modify Conscription Law\n5. Return to Country Menu\n")
            choice=input("Enter Command: ")
            if choice == "1":
                country.set_num_of_cities(country.get_num_of_cities()-int(input("Enter number of cities lost: ")))
                print(f"New number of cities: {country.get_num_of_cities()}")
            elif choice == "2":
                country.set_production_coefficient(float(input("Enter new production coefficient as a decimal [0,10]: "))//(10**8))
            elif choice == "3":
                country.set_attrition_coefficient(float(input("Enter new attrition coefficient as a decimal [0,1]: ")))
            elif choice == "4":
                country.set_conscription_law(float(input("Enter new conscription law as a decimal [0,1]: ")))
            elif choice == "5":
                break
            

    ##TODO:
    def enter_stockpile_menu(self, country):
        pass

    ##TODO:
    def enter_losses_menu(self, country):
        pass

    ##TODO:
    def next_turn(self):
        pass

    ##TODO:
    def save_game(self):
        pass
