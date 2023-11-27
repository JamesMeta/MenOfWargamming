from Unit import Unit
class Infantry(Unit):
    def __init__(self, unit_number, veterancy, nationality, country_tag):
        super().__init__(unit_number, veterancy, nationality, country_tag)
        self.manpower = 100
        self.artillery = 3
        self.machine_guns = 2
        self.anti_tank = 2

        self.deployed_artillery = 0
        self.deployed_machine_guns = 0
        self.deployed_anti_tank = 0

        self.unit_type = "infantry"

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

    #override methods from Unit.py
    def set_rear_guard(self):
        self.set_deployed_manpower(self.manpower//5)
        self.set_deployed_artillery(self.artillery//3)
        self.set_deployed_machine_guns(self.machine_guns//2)
        self.set_deployed_anti_tank(self.anti_tank//2)
        self.rear_guard = True
    
    #override methods from Unit.py
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

    #override methods from Unit.py
    def __str__(self):
        return f"{self.nationality}\nInfantry Division {self.unit_number} \nManpower: {self.manpower} \nArtillery: {self.artillery} \nMachine Guns: {self.machine_guns} \nAnti Tank: {self.anti_tank} \nVeterancy: {self.veterancy} \nIncirclement: {self.incirclement}"
  