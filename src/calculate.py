from main import Country
import matplotlib.pyplot as plt

country1 = []
country2 = []
country3 = []
country4 = []
country5 = []
country6 = []
country7 = []
country8 = []
country9 = []
simulations = 312

country = Country("Germany", "GER", 867552, 1000, 0.05, 34, 0.000000030, 0.2, 0, 0, 0, 0, 0)

for i in range(114):
        country.spawn_infantry(1)

for i in range(22):
        country.spawn_armored(1)

for i in range(simulations):
        if i >30 and i < 40:
                country.spawn_armored(1)
        if i >0 and i < 100:
                country.spawn_infantry(1)
        country.next_turn()
        equipment_in_stockpile = country.get_surplus_tanks() + country.get_surplus_motorized() + country.get_surplus_anti_tank() + country.get_surplus_artillery() + country.get_surplus_machine_guns()
        country1.append(equipment_in_stockpile)

plt.plot(country1, color='black')

country = Country("Soviet", "SOV", 1685240, 1000, 0.01, 29, 0.000000025, 0.0, 0, 0, 0, 0, 0)

for i in range(199):
        country.spawn_infantry(1)

for i in range(25):
        country.spawn_armored(1)

for i in range(simulations):
        if i >40 and i < 60:
                country.spawn_armored(1)
        if i >0 and i < 100:
                country.spawn_infantry(1)
        country.next_turn()
        equipment_in_stockpile = country.get_surplus_tanks() + country.get_surplus_motorized() + country.get_surplus_anti_tank() + country.get_surplus_artillery() + country.get_surplus_machine_guns()
        country2.append(equipment_in_stockpile)

plt.plot(country2, color='red')

country = Country("UK", "ENG", 477600, 1000, 0.04, 20, 0.000000035, 0.25, 0, 0, 0, 0, 0)

for i in range(34):
        country.spawn_infantry(1)

for i in range(8):
        country.spawn_armored(1)

for i in range(simulations):
        if i >0 and i < 15:
                country.spawn_armored(1)
        if i >0 and i < 80:
                country.spawn_infantry(1)
        country.next_turn()
        equipment_in_stockpile = country.get_surplus_tanks() + country.get_surplus_motorized() + country.get_surplus_anti_tank() + country.get_surplus_artillery() + country.get_surplus_machine_guns()
        country3.append(equipment_in_stockpile)

plt.plot(country3, color='pink')

country = Country("France", "FRA", 420000, 1000, 0.05, 26, 0.00000003, 0.1, 0, 0, 0, 0, 0)

for i in range(72):
        country.spawn_infantry(1)

for i in range(14):
        country.spawn_armored(1)

for i in range(simulations):
        if i >0 and i < 12:
                country.delete_unit(i,"armored")
        if i >0 and i < 60:
                country.delete_unit(i,"infantry")
        country.next_turn()
        equipment_in_stockpile = country.get_surplus_tanks() + country.get_surplus_motorized() + country.get_surplus_anti_tank() + country.get_surplus_artillery() + country.get_surplus_machine_guns()
        country4.append(equipment_in_stockpile)

plt.plot(country4, color='blue')

country = Country("USA", "USA", 1310280, 1000, 0.05, 31, 0.000000025, 0.0, 0, 0, 0, 0, 0)

for i in range(40):
        country.spawn_infantry(1)

for i in range(1):
        country.spawn_armored(1)

for i in range(simulations):
        if i >0 and i < 30:
                country.spawn_armored(1)
        if i >0 and i < 100:
                country.spawn_infantry(1)
        country.next_turn()
        equipment_in_stockpile = country.get_surplus_tanks() + country.get_surplus_motorized() + country.get_surplus_anti_tank() + country.get_surplus_artillery() + country.get_surplus_machine_guns()
        country5.append(equipment_in_stockpile)

plt.plot(country5, color='lightblue')

country = Country("Italy", "ITA", 434000, 1000, 0.05, 27, 0.00000002, 0.2, 0, 0, 0, 0, 0)

for i in range(46):
        country.spawn_infantry(1)

for i in range(8):
        country.spawn_armored(1)

for i in range(simulations):
        if i >0 and i < 10:
                country.spawn_armored(1)
        if i >0 and i < 40:
                country.spawn_infantry(1)
        country.next_turn()
        equipment_in_stockpile = country.get_surplus_tanks() + country.get_surplus_motorized() + country.get_surplus_anti_tank() + country.get_surplus_artillery() + country.get_surplus_machine_guns()
        country6.append(equipment_in_stockpile)

plt.plot(country6, color='green')


country = Country("Hungary", "HUN", 91290, 1000, 0.05, 10, 0.00000003, 0.25, 0, 0, 0, 0, 0)

for i in range(15):
        country.spawn_infantry(1)

for i in range(1):
        country.spawn_armored(1)

for i in range(simulations):
        if i >30 and i < 34:
                country.spawn_armored(1)
        if i >30 and i < 40:
                country.spawn_infantry(1)
        country.next_turn()
        equipment_in_stockpile = country.get_surplus_tanks() + country.get_surplus_motorized() + country.get_surplus_anti_tank() + country.get_surplus_artillery() + country.get_surplus_machine_guns()
        country7.append(equipment_in_stockpile)

plt.plot(country7, color='orange')

country = Country("Romania", "ROM", 199338, 1000, 0.05, 10, 0.00000003, 0.25, 0, 0, 0, 0, 0)

for i in range(25):
        country.spawn_infantry(1)

for i in range(1):
        country.spawn_armored(1)

for i in range(simulations):
        if i >0 and i < 5:
                country.spawn_armored(1)
        if i >30 and i < 40:
                country.spawn_infantry(1)
        country.next_turn()
        equipment_in_stockpile = country.get_surplus_tanks() + country.get_surplus_motorized() + country.get_surplus_anti_tank() + country.get_surplus_artillery() + country.get_surplus_machine_guns()
        country8.append(equipment_in_stockpile)

plt.plot(country8, color='yellow')

country = Country("Netherlands", "HOL", 175338, 1000, 0.05, 9, 0.000000020, 0.2, 0, 0, 0, 0, 0)

for i in range(27):
        country.spawn_infantry(1)

for i in range(simulations):
        if i >0 and i < 20:
                country.delete_unit(i,"infantry")
        country.next_turn()
        equipment_in_stockpile = country.get_surplus_tanks() + country.get_surplus_motorized() + country.get_surplus_anti_tank() + country.get_surplus_artillery() + country.get_surplus_machine_guns()
        country9.append(equipment_in_stockpile)

plt.plot(country9, color='brown')

plt.ylabel('equipment in stockpile')
plt.xlabel('days')
plt.legend(["Germany", "Soviet", "UK", "France", "USA", "Italy", "Hungary", "Romania", "Netherlands"])
plt.grid(True)
plt.show()


print("Germany")
print(f"Surplus tanks: {country.get_surplus_tanks()} Surplus motorized: {country.get_surplus_motorized()} Surplus AntiTank {country.get_surplus_anti_tank()} surplus artillery: {country.get_surplus_artillery()} surplus machineguns {country.get_surplus_machine_guns()}")
print(f"losses tanks: {country.get_tanks_losses()} losses motorized: {country.get_motorized_losses()} losses AntiTank {country.get_anti_tank_losses()} losses artillery: {country.get_artillery_losses()} losses machineguns {country.get_machine_guns_losses()}")

