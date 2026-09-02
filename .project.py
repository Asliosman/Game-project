player=(input("what is the player`s name"))
age=int(input("what is the player`s age"))
print(player)
print(age)
if age<12:
    print("minor;the game is shutting down")
else:
    print("hello")
while True:
    print("main menu")
    command=input("enter command")
    
    if command=="lopeta":
        print("game ended")
        break
    elif command=="explore":
        print("you explore the allien planet")
    elif command=="fight":
        print("you fight an allien")
    elif command=="treasure":
        print("you found an allien treasure")
    else:
        print("unknown command")


