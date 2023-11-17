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

    def __str__(self):
            return f"Armor Division {self.unit_number} \nManpower: {self.manpower} \nTanks: {self.tanks} \nMotorized: {self.motorized} \nVeterancy: {self.veterancy} \nIncirclement: {self.incirclement}"
    