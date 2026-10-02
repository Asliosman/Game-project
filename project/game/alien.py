class Alien:
    def __init__(self, name, health=50, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return self.health > 0

    def attack(self, player):
        player.take_damage(self.attack_power)
        print(f"{self.name} attacks {player.name}!")
        print(f"{player.name}'s health: {player.health}")