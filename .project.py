discoveries=[]
def explore():
    place=input("enter a place to explore")
    discoveries.append(place)
    print("you explore:",place)
def show_discoverie():
    print("your discoveries:")
    for place in discoveries:
        print(place)
def fight():
    print("you fight an allien!")
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
    print("explore")
    print("fight")
    print("treasure")
    print("show")
    print("lopeta")
    command=input("enter command")
    
    if command=="lopeta":
        print("game ended")
        break
    elif command=="explore":
        explore()
    elif command=="fight":
        fight()
    elif command=="treasure":
        print("you found an allien treasure")
    elif command=="show":
        show_discoveries()
    else:
        print("unknown command")


