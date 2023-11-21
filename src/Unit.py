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

    def get_unit_number(self):
        return self.unit_number
    
    def get_country_tag(self):
        return self.country_tag

    def get_manpower(self):
        return self.manpower
    
    def get_veterancy(self):
        return self.veterancy
    
    def get_incirclement(self):
        return self.incirclement
    
    def get_unit_losses(self):
        return self.unit_losses
    
    def get_deployed_manpower(self):
        return self.deployed_manpower
    
    def get_nationality(self):
        return self.nationality
    
    def get_unit_type(self):
        pass

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
    