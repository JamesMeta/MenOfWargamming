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
    
    def get_country_tag(self):
        return self.country_tag
    
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

    def get_rear_guard(self):
        return self.rear_guard
    
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
        return f"{self.nationality}\nInfantry Division {self.unit_number} \nManpower: {self.manpower} \nArtillery: {self.artillery} \nMachine Guns: {self.machine_guns} \nAnti Tank: {self.anti_tank} \nVeterancy: {self.veterancy} \nIncirclement: {self.incirclement}"
  