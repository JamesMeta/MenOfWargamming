class Unit:
    def __init__(self, unit_number, veterancy, nationality, country_tag):
        self.unit_number = unit_number
        self.veterancy = veterancy
        self.incirclement = False
        self.unit_losses = 0

        self.deployed_manpower = 0
        self.rear_guard = False

        self.nationality = nationality
        self.country_tag = country_tag

    def set_deployed_manpower(self, deployed_manpower):
        self.deployed_manpower = deployed_manpower
        self.manpower -= deployed_manpower
    
    def set_rear_guard(self):
        pass
    
    def set_full_deployment(self):
        pass

    def after_action_update(self):
        pass
    
    def sum_unit_losses(self, unit_losses):
        self.unit_losses += unit_losses

    def __str__(self):
        pass
    