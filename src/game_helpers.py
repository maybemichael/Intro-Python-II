import sys
import time
import random
import os


class GameHelpers:

    is_playing: bool = False

    def type_out(t):
        typing_speed = 100
        for char in t:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.random() * 10.0/typing_speed)
            print(end="")

    def display_text(text: list):
        for line in text:
            time.sleep(0.8)
            GameHelpers.type_out(line)

    def is_choice_valid(valid_input: list):
        user_entered = input(">")
        choice = user_entered
        is_valid = False
        while is_valid is False:
            if choice not in valid_input:
                if len(valid_input) == 3:
                    print("Invalid option, Press [Y] for yes, or [N] for no...\n")
                    GameHelpers.type_out("Please try again...\n")
                    user_choice = input(">")
                    choice = user_choice.lower()
                elif len(valid_input) == 5:
                    print("Invalid option, Press [N] to move north, [S] to move south, [E] to move east, or [W] to move west...")
                    GameHelpers.type_out("Please try again...\n")
                    user_choice = input(">")
                    choice = user_choice.lower()
            elif choice == "q":
                GameHelpers.type_out("Thanks for playing... Goodbye!")
                is_valid = True
                sys.exit()
            else:
                is_valid = True
                return choice

    def play(choice: str):
        if choice == "n":
            GameHelpers.type_out("Thanks for playing... Goodbye!")
            GameHelpers.is_playing = False
        elif choice == "y":
            GameHelpers.type_out("I knew you looked like the adventuring type! Let's go!\n")
            GameHelpers.is_playing = True

    def create_player():
        if GameHelpers.is_playing:
            line = "\nBy the way stranger, what's your name?\n"
            GameHelpers.type_out(line)
            player_name = input(">")
            lines = [f"\nNice to meet you {player_name}!\n", "\nYou look famished, and you know I could eat!\n", "\nLets grab some grub.\n" "\nBoy a sammich sure sounds nice right about now!\n", "\n...Hey, I know!!! Let's go on an adventure to find one!\n", "\nThe names Munchies, by the way...\n"]
            GameHelpers.display_text(lines)
            return player_name

    def prompt_to_play():
        os.system("cls" if os.name == "nt" else "clear")
        os_name = os.name
        print(os_name)
        print("\n")
        print("\n")
        print("***************************************************************************************************************************************************")
        print(" _______  _______  _______  _______ _________ _______             _______  ______            _______  _       _________          _______  _______  ")
        print("(  ____ \(  ___  )(       )(       )\__   __/(  ____ \|\     /|  (  ___  )(  __  \ |\     /|(  ____ \( (    /|\__   __/|\     /|(  ____ )(  ____ \ ")
        print("| (    \/| (   ) || () () || () () |   ) (   | (    \/| )   ( |  | (   ) || (  \  )| )   ( || (    \/|  \  ( |   ) (   | )   ( || (    )|| (    \/ ")
        print("| (_____ | (___) || || || || || || |   | |   | |      | (___) |  | (___) || |   ) || |   | || (__    |   \ | |   | |   | |   | || (____)|| (__     ")
        print("(_____  )|  ___  || |(_)| || |(_)| |   | |   | |      |  ___  |  |  ___  || |   | |( (   ) )|  __)   | (\ \) |   | |   | |   | ||     __)|  __)    ")
        print("      ) || (   ) || |   | || |   | |   | |   | |      | (   ) |  | (   ) || |   ) | \ \_/ / | (      | | \   |   | |   | |   | || (\ (   | (       ")
        print("/\____) || )   ( || )   ( || )   ( |___) (___| (____/\| )   ( |  | )   ( || (__/  )  \   /  | (____/\| )  \  |   | |   | (___) || ) \ \__| (____/\ ")
        print("\_______)|/     \||/     \||/     \|\_______/(_______/|/     \|  |/     \|(______/    \_/   (_______/|/    )_)   )_(   (_______)|/   \__/(_______/ ")
        print("\n")
        print("***************************************************************************************************************************************************")
        print("\n")
        print("\n")
        print("\nWould you like to play?\nPlease choose [Y] for Yes or [N] for no...")
        # GameHelpers.type_out(text)
        yes_or_no = ["y", "n", "q"]
        valid_choice = GameHelpers.is_choice_valid(yes_or_no)
        return valid_choice

    def munchies_speaks(text: str):
        print("\nMunchies:\n")
        GameHelpers.type_out(text)

    def munchies_random():
        line1 = "If oranges are orange, why are limes not called “greens”?\n"
        line2 = "If life is unfair to everyone, does that mean life is actually fair?\n"
        line3 = "If tomatoes are a fruit, does that mean ketchup is a smoothie?\n"
        line4 = "Being “up” for something means the same thing as being “down” for something.\n"
        line5 = "If you try to fail, but end up succeeding, which did you actually do?\n"
        line6 = "Do pets name their owners?\n"
        line7 = "Why is a pizza box square if the pizza is a circle and a slice is a triangle?\n"
        line8 = "Who closes the bus door after the bus driver gets off?\n"
        random_lines = [line1, line2, line3, line4, line5, line6, line7, line8]
        random_num = random.randint(0, 7)
        GameHelpers.munchies_speaks(random_lines[random_num])
