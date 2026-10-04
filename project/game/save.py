import json
import os

from .item import Item

SAVE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "saves")


def _save_path(name):
    # Turn the player's name into a safe file name
    safe_name = "".join(c if c.isalnum() else "_" for c in name.lower())
    return os.path.join(SAVE_DIR, f"{safe_name}.txt")


def save_exists(name):
    return os.path.exists(_save_path(name))


def _item_to_dict(item):
    if item is None:
        return None
    return {"name": item.name, "weight": item.weight}


def save_game(player, game, rooms):
    #Write the current state of the game to a text file named after the player.
    state = {
        "health": player.health,
        "reward": player.reward,
        "location": player.location.name,
        "inventory": [_item_to_dict(item) for item in player.inventory],
        "rooms": {room.name: _item_to_dict(room.item) for room in rooms},
        "aliens": [
            {"name": a.name, "health": a.health, "attack_power": a.attack_power}
            for a in game.aliens
        ],
    }
    os.makedirs(SAVE_DIR, exist_ok=True)
    with open(_save_path(player.name), "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def load_game(player, game, rooms):
    #Restore the saved state into the existing objects. Returns True if it worked.
    try:
        with open(_save_path(player.name), "r", encoding="utf-8") as f:
            state = json.load(f)

        rooms_by_name = {room.name: room for room in rooms}

        player.health = state["health"]
        player.reward = state["reward"]
        player.location = rooms_by_name[state["location"]]
        player.inventory = [Item(d["name"], d["weight"]) for d in state["inventory"]]

        for room_name, item_data in state["rooms"].items():
            if item_data is None:
                rooms_by_name[room_name].item = None
            else:
                rooms_by_name[room_name].item = Item(item_data["name"], item_data["weight"])

        for saved in state["aliens"]:
            for alien in game.aliens:
                if alien.name == saved["name"]:
                    alien.health = saved["health"]
                    alien.attack_power = saved["attack_power"]
        return True
    except (OSError, ValueError, KeyError):
        return False


def delete_save(name):
    #Remove the save file used when a game has ended.
    path = _save_path(name)
    if os.path.exists(path):
        os.remove(path)