class Battle:

    def __init__(self, battle_name, winner, attacker, defender, attacker_losses, defender_losses):
        self.battle_name = battle_name
        self.winner = winner
        self.attacker = attacker
        self.defender = defender
        self.attacker_losses = attacker_losses
        self.defender_losses = defender_losses
    
    #losses list structure [men, artillery, machine_guns, anti_tank, tanks, motorized]
    def format_losses(self, losses):
        return(f"{losses[0]} men, {losses[1]} artillery, {losses[2]} machine guns, {losses[3]} anti tank, {losses[4]} tanks, {losses[5]} motorized")
        
    def __str__(self):
        return f"{self.battle_name} \nThe Winner was: {self.winner} \nAttacking Nation(s): {self.attacker} \nDefending Nation(s): {self.defender} \nAttacker Losses: {self.format_losses(self.attacker_losses)} \nDefender Losses: {self.format_losses(self.defender_losses)}"
    