#ALIEN ATTACK
Asli Osman

Project Structure
project/
├── game/         
   └── main.py           
    ├── player.py    
    ├── room.py      
    ├── item.py      
    ├── alien.py     
    ├── game.py      
    └── menu.py        
    └── save.py 
   ├── instructions.txt        
   └── intro.txt 
         
main.py creates the player, aliens, rooms and items, and runs the main menu.
Player can move to another room and collect the item in the current room.
Room holds a name and possibly an item.
Item holds a name and a weight
save.py writes the game state (health, reward, location, inventory, room items and alien health) to saves/<player name>.txt.


The game saves automatically after moving, collecting an item, each turn of the fight, and when quitting. To continue later, start the game and enter the same name. The game asks if you want to continue your saved game. When a game ends (win or lose), its save file is deleted.