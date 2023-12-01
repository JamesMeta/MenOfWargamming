import matplotlib.pyplot as plt
from Battle import Battle

class Statistics:

    def __init__(self, country_map):
        
        self.total_battles = 0
        self.total_losses = [0,0,0,0,0,0]

        self.battle_list = []
        self.country_map = country_map
        self.country_manpower_losses_map = {}
        self.country_equipment_losses_map = {}
        self.country_stockpile_map = {}

        for country_tag in self.country_map:
            self.country_manpower_losses_map[country_tag] = []
            self.country_equipment_losses_map[country_tag] = []
            self.country_stockpile_map[country_tag] = []
    
    def new_battle(self, battle_name, winner, attacker, defender, attacker_losses, defender_losses):
        battle = Battle(battle_name, winner, attacker, defender, attacker_losses, defender_losses)
        self.battle_list.append(battle)
        self.total_battles += 1
        self.total_losses[0] += attacker_losses[0] + defender_losses[0]
        self.total_losses[1] += attacker_losses[1] + defender_losses[1]
        self.total_losses[2] += attacker_losses[2] + defender_losses[2]
        self.total_losses[3] += attacker_losses[3] + defender_losses[3]
        self.total_losses[4] += attacker_losses[4] + defender_losses[4]
        self.total_losses[5] += attacker_losses[5] + defender_losses[5]

        return battle

    def get_battle(self, battle_name):
        for battle in self.battle_list:
            if battle.battle_name == battle_name:
                return battle

    def next_turn(self):
        for country_tag in self.country_map:
            self.country_manpower_losses_map[country_tag].append(self.country_map[country_tag].manpower_losses)
            self.country_equipment_losses_map[country_tag].append(self.country_map[country_tag].artillery_losses + self.country_map[country_tag].anti_tank_losses + self.country_map[country_tag].machine_guns_losses + self.country_map[country_tag].tanks_losses + self.country_map[country_tag].motorized_losses)
            self.country_stockpile_map[country_tag].append(self.country_map[country_tag].surplus_artillery + self.country_map[country_tag].surplus_anti_tank + self.country_map[country_tag].surplus_machine_guns + self.country_map[country_tag].surplus_tanks + self.country_map[country_tag].surplus_motorized)
        
    def graph_equipment_losses_for_country(self, country_tag):
        losses_array = self.country_equipment_losses_map[country_tag]
        country = self.country_map[country_tag]
        plt.plot(losses_array, color=country.country_colour, label=country.country_name)
        plt.xlabel('Weeks')
        plt.show()

    def graph_manpower_losses_for_country(self, country_tag):
        losses_array = self.country_manpower_losses_map[country_tag]
        country = self.country_map[country_tag]
        plt.plot(losses_array, color=country.country_colour, label=country.country_name)
        plt.xlabel('Weeks')
        plt.show()

    def graph_equipment_losses_for_all(self):
        for country_tag in self.country_map.keys():
            losses_array = self.country_equipment_losses_map[country_tag]
            country = self.country_map[country_tag]
            plt.plot(losses_array, color=country.country_colour, label=country.country_name)
        plt.xlabel('Weeks')
        plt.show()

    def graph_manpower_losses_for_all(self):
        for country_tag in self.country_map.keys():
            losses_array = self.country_manpower_losses_map[country_tag]
            country = self.country_map[country_tag]
            plt.plot(losses_array, color=country.country_colour, label=country.country_name)
        plt.xlabel('Weeks')
        plt.show()

    def graph_stockpile_for_country(self, country_tag):
        stockpile_array = self.country_stockpile_map[country_tag]
        country = self.country_map[country_tag]
        plt.plot(stockpile_array, color=country.country_colour, label=country.country_name)
        plt.xlabel('Weeks')
        plt.show()

    def graph_stockpile_for_all_countries(self):
        for country_tag in self.country_map.keys():
            stockpile_array = self.country_stockpile_map[country_tag]
            country = self.country_map[country_tag]
            plt.plot(stockpile_array, color=country.country_colour, label=country.country_name)
        plt.legend()
        plt.xlabel('Weeks')
        plt.show()
  