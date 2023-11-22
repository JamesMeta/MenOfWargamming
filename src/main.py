from World import World
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    world = World()
    world.start_game("D")
    while True:
        clear()
        print("Possible Commands:\ncountry menu <country>\nstart battle\nstatistics menu\nnext turn\nexit\n")
        command = input("Enter command: ")
        if command.startswith("country menu"):
            world.enter_country_menu(command.split(" ")[2])
        if command == "start battle":
            world.start_battle()
        if command == "statistics menu":
            world.enter_statistics_menu()
        if command == "next turn":
            world.next_turn()
        if command == "exit":
            break

if __name__ == "__main__":
    main()