import os 

from game.player import Player
from game.alien import Alien
from game.game import Game
from game.room import Room
from game.item import Item
from game.menu import show_menu, show_action_menu
from game.save import save_game, load_game, save_exists, delete_save 
 
#find the exact folder where the file is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  


def show_file(filename):  
    
    try:
        with open(os.path.join(BASE_DIR, filename), "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"({filename} was not found)")


print("=======================")
print("   ALIEN ATTACK GAME")
print("=======================")
print("welcome to Alien Attack")
show_file("intro.txt")  #background text

#collect player details
name = input("Enter your name: ")
age = input("Enter your age: ")

#Keep asking until the age is made of digits only.
while not age.isdigit():
    print("Please enter a number for your age.")
    age = input("Enter your age: ")
age = int(age)

#age restriction
print(f"Name: {name}, Age: {age}")
if age < 12:
    print("You are a minor. You cannot play this game.")
    raise SystemExit
print(f"Hello {name}, good luck!")
show_file("instructions.txt")  

player = Game_player = Player(name, age)
game = Game(player)

#aliens inside the game
alien = Alien("Zorg")
game.add_aliens(alien)
game.add_aliens(Alien("Blip"))
game.add_aliens(Alien("Krax"))

#rooms and items inside the game
village = Room("Village", Item("Bucket", 2.5))
forest = Room("Forest", Item("Torch", 1.0))
cave = Room("Cave", Item("Map", 0.2))
rooms = [village, forest, cave]
player.location = village

#resume a saved game
if save_exists(name):
    answer = input("A saved game was found for you. Continue it? (y/n): ").strip().lower()
    if answer == "y":
        #restore the player game and rooms
        if load_game(player, game, rooms):
            print("Game loaded. Welcome back!")
        else:
            print("The save file could not be read. Starting a new game.")
    else:
        print("Starting a new game.")


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
         # Option 1: start the fight against the aliens.
        print("starting game...")

# Keep playing turns until the player wins or loses.
        while not game.is_over():
            action = show_action_menu()
            game.handle_action(action)
            save_game(player, game, rooms)  
        #announce the outcome.
        if game.has_won():
            result = "WIN"
            print("You defeated the aliens! You win!")
            print("Your prize:", player.reward)
        else:
            result = "LOSE"
            print("The aliens got you. You lose.")
  # The game is finished, so the save is no longer needed.
            delete_save(player.name)

# Append this game's outcome to the results file.
        with open("results.txt", "a") as f:
            f.write(f"{player.name}, {player.age}, {result}\n")
        break

    elif choice == "2":
        # Option 2: list the aliens in the game.
        game.show_aliens()

    elif choice == "3":
        # Option 3: save and quit.
        save_game(player, game, rooms)  
        print("Game saved.")  
        print("Goodbye!")
        break

    elif choice == "4":
        # Option 4: move to another room, then save.
        move_player()
        save_game(player, game, rooms)  

    elif choice == "5":
        # Option 5: pick up the item in this room, then save.
        collect_item()
        save_game(player, game, rooms)  

    elif choice == "6":
        # Option 6: view inventory (so no save needed).
        show_inventory()

    elif choice == "7":
        # Option 7: look around the current room.
        look_around()