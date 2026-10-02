class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.reward = 0
        self.inventory = []
        self.location = None

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return self.is_alive()

    def is_alive(self):
        return self.health > 0

    def move(self, destination):
        self.location = destination
        print(f"You moved to the {destination.name}.")

    def collect_item(self):
        room = self.location
        if room.item is None:
            print("There is nothing to collect here.")
        else:
            self.inventory.append(room.item)
            print(f"You collected: {room.item.name}")
            room.item = None