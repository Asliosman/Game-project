import random
from .player import Player
from .alien import Alien

class Game:
    def __init__(self,player):
        self.player=player
        self.aliens=[]

    def add_aliens(self,alien):
        self.aliens.append(alien)

    def show_aliens (self):
        for alien in self.aliens:
            print(f"Alien: {alien.name}")

    def alien_attack(self):
        for alien in self.aliens:
            if alien.health > 0:
                alien.attack(self.player)
                break

    def all_aliens_defeated(self):
        return all(alien.health <= 0 for alien in self.aliens)

    def handle_action(self, action):
        target = next((a for a in self.aliens if a.health > 0), None)
        if target is None:
            return

        if action == "1":
            print("you attack the alien!")
            target.take_damage(25)
            if target.health <= 0:
                print(f"{target.name} is defeated!")
                self.player.reward += 10
            else:
                self.alien_attack()

        elif action == "2":
            print("you hide from the alien")
            if random.random() < 0.5:
                print("the alien cannot find you")
            else:
                print("the alien found you!")
                self.alien_attack()

        elif action == "3":
            print("you run away!")
            print("you dropped some of your reward while running...")
            if self.player.reward >= 5:
                self.player.reward -= 5

    def has_won(self):
        return self.player.is_alive() and self.all_aliens_defeated()

    def is_over(self):
        return not self.player.is_alive() or self.all_aliens_defeated()