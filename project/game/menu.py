def show_menu():
    while True:
        print("\n--- Alien Attack ---")
        print("1.start game")
        print("2.show aliens")
        print("3.quit")
        print("4.move to another room")
        print("5.collect item")
        print("6.show inventory")
        print("7.look around")
        choice = input("choose an option: ")
        if choice in ("1", "2", "3", "4", "5", "6", "7"):
            return choice
        print("Invalid choice, please try again.")


def show_action_menu():
    while True:
        print("\n--- Choose your move ---")
        print("1.Attack")
        print("2.Hide")
        print("3.Run")
        choice = input("choose an action: ")
        if choice in ("1", "2", "3"):
            return choice
        print("Invalid choice, please try again.")