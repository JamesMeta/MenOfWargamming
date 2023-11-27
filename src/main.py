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

    while True:
        print("Possible Commands:\ncountry menu <country>\nstart battle\nstatistics menu\nnext turn\nexit\nsave\n")
        command = input("Enter command: ")
        if command.startswith("country menu"):
            world.enter_country_menu(command.split(" ")[2])
        if command == "start battle":
            world.start_battle()
        if command == "statistics menu":
            world.enter_statistics_menu()
        if command == "next turn":
            world.next_turn()
        if command == "save":
            save(world)
        if command == "exit":
            break
        clear()

if __name__ == "__main__":
    main()