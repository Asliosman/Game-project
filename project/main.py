from game.player import Player
from game.alien import Alien
from game.game import Game
from game.room import Room
from game.item import Item
from game.menu import show_menu, show_action_menu


print("=======================")
print("   ALIEN ATTACK GAME")
print("=======================")
print("welcome to Alien Attack")
print("Aliens have taken the village's clean water. Defeat them to get it back!")

name = input("Enter your name: ")
age = input("Enter your age: ")
while not age.isdigit():
    print("Please enter a number for your age.")
    age = input("Enter your age: ")
age = int(age)

print(f"Name: {name}, Age: {age}")
if age < 12:
    print("You are a minor. You cannot play this game.")
    raise SystemExit
print(f"Hello {name}, good luck!")

player = Game_player = Player(name, age)
game = Game(player)

alien = Alien("Zorg")
game.add_aliens(alien)
game.add_aliens(Alien("Blip"))
game.add_aliens(Alien("Krax"))

village = Room("Village", Item("Bucket", 2.5))
forest = Room("Forest", Item("Torch", 1.0))
cave = Room("Cave", Item("Map", 0.2))
rooms = [village, forest, cave]
player.location = village


def move_player():
    print("Where do you want to go?")
    number = 1
    for room in rooms:
        print(f"{number}. {room.name}")
        number += 1
    room_choice = input("Choose a room: ")
    if room_choice.isdigit() and 1 <= int(room_choice) <= len(rooms):
        player.move(rooms[int(room_choice) - 1])
    else:
        print("Invalid room.")


def collect_item():
    player.collect_item()


def show_inventory():
    if len(player.inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("You are carrying:")
        for item in player.inventory:
            print(f"- {item.name} ({item.weight} kg)")


def look_around():
    print(f"You are in the {player.location.name}.")
    if player.location.item is None:
        print("You see nothing useful.")
    else:
        print(f"You see a {player.location.item.name} on the ground.")


while True:
    choice = show_menu()

    if choice == "1":
        print("starting game...")

        while not game.is_over():
            action = show_action_menu()
            game.handle_action(action)

        if game.has_won():
            result = "WIN"
            print("You defeated the aliens! You win!")
            print("Your prize:", player.reward)
        else:
            result = "LOSE"
            print("The aliens got you. You lose.")

        with open("results.txt", "a") as f:
            f.write(f"{player.name}, {player.age}, {result}\n")
        break

    elif choice == "2":
        game.show_aliens()

    elif choice == "3":
        print("Goodbye!")
        break

    elif choice == "4":
        move_player()

    elif choice == "5":
        collect_item()

    elif choice == "6":
        show_inventory()

    elif choice == "7":
        look_around()