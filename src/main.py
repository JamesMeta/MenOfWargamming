from World import World
from World import clear
import os
import pickle

def save(world):

    serialized = pickle.dumps(world)

    with open('game_data.pkl', 'wb') as file:
        file.write(serialized)
    
    print("save complete")

def on_load():
    with open('game_data.pkl', 'rb') as file:
        world = pickle.load(file)
    return world

def main():

    if os.path.exists('game_data.pkl'):
        choice = input("Save file found, would you like to load it? (y/n): ")
        if choice == "y":
            print("Save file found, loading...")
            world = on_load()
        else:
            world = World()
            world.start_game("D")
            clear()
    else:    
        world = World()
        world.start_game("D")
        clear()

    while True:
        print("Possible Commands:\n1. Country Menu (1.country_tag)\n2. Start Battle\n3. Statistics Menu\n4. Next Turn\n5. Save\n6. Exit\n")
        command = input("Enter command: ")
        if command.startswith("1"):
            world.enter_country_menu(command.split(".")[1])
        if command == "2":
            world.start_battle()
        if command == "3":
            world.enter_statistics_menu()
        if command == "4":
            world.next_turn()
        if command == "5":
            save(world)
        if command == "6":
            break
        clear()

if __name__ == "__main__":
    main()