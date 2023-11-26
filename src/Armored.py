from Unit import Unit
class Armored(Unit):
    def __init__(self, unit_number, veterancy, nationality, country_tag):
        super().__init__(unit_number, veterancy, nationality, country_tag)
        self.manpower = 60
        self.tanks = 6
        self.motorized = 5

        self.deployed_tanks = 0
        self.deployed_motorized = 0

        self.unit_type = "Armored"
    
    def set_deployed_tanks(self, deployed_tanks):
        self.deployed_tanks = deployed_tanks
        self.tanks -= deployed_tanks

    def set_deployed_motorized(self, deployed_motorized):
        self.deployed_motorized = deployed_motorized
        self.motorized -= deployed_motorized
    
    #override methods from Unit.py
    def set_rear_guard(self):
        self.set_deployed_manpower(self.manpower//5)
        self.set_deployed_tanks(self.tanks//4)
        self.set_deployed_motorized(self.motorized//4)
        self.rear_guard = True
    
    #override methods from Unit.py
    def set_full_deployment(self):
        self.set_deployed_manpower(self.manpower)
        self.set_deployed_tanks(self.tanks)
        self.set_deployed_motorized(self.motorized)

    #override methods from Unit.py
    def after_action_update(self):

        self.deployed_manpower = 0
        self.deployed_tanks = 0
        self.deployed_motorized = 0
        self.rear_guard = False
    
    #override methods from Unit.py
    def __str__(self):
            return f"{self.nationality} \nArmor Division {self.unit_number} \nManpower: {self.manpower} \nTanks: {self.tanks} \nMotorized: {self.motorized} \nVeterancy: {self.veterancy} \nIncirclement: {self.incirclement}"
    