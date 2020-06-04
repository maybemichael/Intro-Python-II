import sys, time, random, textwrap, os
from enum import Enum

class GameHelpers:

    logo = """
     _______  _______  _______  _______ _________ _______             _______  ______            _______  _       _________          _______  _______
    (  ____ \(  ___  )(       )(       )\__   __/(  ____ \|\     /|  (  ___  )(  __  \ |\     /|(  ____ \( (    /|\__   __/|\     /|(  ____ )(  ____ \ 
    | (    \/| (   ) || () () || () () |   ) (   | (    \/| )   ( |  | (   ) || (  \  )| )   ( || (    \/|  \  ( |   ) (   | )   ( || (    )|| (    \/
    | (_____ | (___) || || || || || || |   | |   | |      | (___) |  | (___) || |   ) || |   | || (__    |   \ | |   | |   | |   | || (____)|| (__    
    (_____  )|  ___  || |(_)| || |(_)| |   | |   | |      |  ___  |  |  ___  || |   | |( (   ) )|  __)   | (\ \) |   | |   | |   | ||     __)|  __)   
          ) || (   ) || |   | || |   | |   | |   | |      | (   ) |  | (   ) || |   ) | \ \_/ / | (      | | \   |   | |   | |   | || (\ (   | (      
    /\____) || )   ( || )   ( || )   ( |___) (___| (____/\| )   ( |  | )   ( || (__/  )  \   /  | (____/\| )  \  |   | |   | (___) || ) \ \__| (____/\ 
    \_______)|/     \||/     \||/     \|\_______/(_______/|/     \|  |/     \|(______/    \_/   (_______/|/    )_)   )_(   (_______)|/   \__/(_______/                                                                                                                                                
"""

    # def __init__(self, logo):
        

    def slow_type(t):
        typing_speed = 100
        for line in t:
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(random.random() * 10.0/typing_speed)
                print(end="")

    def display_text(text: list):
        # text_tuple = tuple(lines)
        for line in text:
            GameHelpers.slow_type(line)
            next_line = input(" ")


    def user_input(valid_input: list):
        user_entered = input()
        if user_entered not in valid_input:
            print("Invalid option, please choose from one of these options:\n")
            for option in valid_input:
                print(option)
        else:
            return user_entered

    def start_game(options: list):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n")
        print("\n")
        print(" _______  _______  _______  _______ _________ _______             _______  ______            _______  _       _________          _______  _______  ")
        print("(  ____ \(  ___  )(       )(       )\__   __/(  ____ \|\     /|  (  ___  )(  __  \ |\     /|(  ____ \( (    /|\__   __/|\     /|(  ____ )(  ____ \ ")
        print("| (    \/| (   ) || () () || () () |   ) (   | (    \/| )   ( |  | (   ) || (  \  )| )   ( || (    \/|  \  ( |   ) (   | )   ( || (    )|| (    \/ ")
        print("| (_____ | (___) || || || || || || |   | |   | |      | (___) |  | (___) || |   ) || |   | || (__    |   \ | |   | |   | |   | || (____)|| (__     ")
        print("(_____  )|  ___  || |(_)| || |(_)| |   | |   | |      |  ___  |  |  ___  || |   | |( (   ) )|  __)   | (\ \) |   | |   | |   | ||     __)|  __)    ")
        print("      ) || (   ) || |   | || |   | |   | |   | |      | (   ) |  | (   ) || |   ) | \ \_/ / | (      | | \   |   | |   | |   | || (\ (   | (       ")
        print("/\____) || )   ( || )   ( || )   ( |___) (___| (____/\| )   ( |  | )   ( || (__/  )  \   /  | (____/\| )  \  |   | |   | (___) || ) \ \__| (____/\ ")
        print("\_______)|/     \||/     \||/     \|\_______/(_______/|/     \|  |/     \|(______/    \_/   (_______/|/    )_)   )_(   (_______)|/   \__/(_______/ ")
        print("\n")
        print("\n") 
        text = ["\nWould you like to play?"]
        GameHelpers.slow_type(text)
        print("\n[Y] Yes or [N]?")
        user_input = input(">")
        user_input(user_input, valid_input)

