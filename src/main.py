from World import World

def main():
    world = World()
    world.start_game("D")
    while True:
        command = input("Enter command: ")
        if command.startswith("unit_menu"):
            world.enter_country_menu(command.split(" ")[1])

if __name__ == "__main__":
    main()