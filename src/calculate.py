from main import Country
import matplotlib.pyplot as plt

artillery_losses = []  # Create an empty list to store the artillery losses
tank_losses = []  # Create an empty list to store the tank losses
motorized_losses = []  # Create an empty list to store the motorized losses
anti_tank_losses = []  # Create an empty list to store the anti tank losses
machine_guns_losses = []  # Create an empty list to store the machine gun losses


for i in range(9, 1, -1):
    country = Country("Germany", "GER", 867552, 1000, 0.05, 34, 1, i/10, 100, 100, 100, 100, 100)

    for _ in range(114):
        country.spawn_infantry(1)

    for _ in range(22):
        country.spawn_armored(1)

    for _ in range(1):
        country.next_turn()

    print(f"Surplus tanks: {country.get_surplus_tanks()} Surplus motorized: {country.get_surplus_motorized()} Surplus AntiTank {country.get_surplus_anti_tank()} surplus artillery: {country.get_surplus_artillery()} surplus machineguns {country.get_surplus_machine_guns()}")
    
    print(f"losses tanks: {country.get_tanks_losses()} losses motorized: {country.get_motorized_losses()} losses AntiTank {country.get_anti_tank_losses()} losses artillery: {country.get_artillery_losses()} losses machineguns {country.get_machine_guns_losses()}")
    
    artillery_losses.append(country.get_artillery_losses())
    tank_losses.append(country.get_tanks_losses())
    motorized_losses.append(country.get_motorized_losses())
    anti_tank_losses.append(country.get_anti_tank_losses())
    machine_guns_losses.append(country.get_machine_guns_losses())


#plot losses against iteration
plt.plot(range(9, 1, -1), artillery_losses)
plt.plot(range(9, 1, -1), tank_losses)
plt.plot(range(9, 1, -1), motorized_losses)
plt.plot(range(9, 1, -1), anti_tank_losses)
plt.plot(range(9, 1, -1), machine_guns_losses)
         
plt.legend(["artillery", "tanks", "motorized", "anti_tank", "machine_guns"])
plt.xlabel("iteration")
plt.ylabel("losses")

plt.show()
