#menus.py: contains generic functions used for menu navigation throughout the assistant
from exceptions import ChoiceException
from OOTmenus import ootAreaMenu

#top level options; handles exceptions caused by submenus
def topLevelMenu():
    while True:
        keys = input("===== Speedrun practice assistant =====\n1. Legend of Zelda: OoT\n0. Quit\n")
        if keys == "1": #OOT
            error = True
            while error:
                try:
                    ootAreaMenu()
                    error = False
                except ChoiceException:
                    print("Invalid option.")
        elif keys == "0": #quit after confirmation
            error = True
            while error:
                try:
                    quitMenu()
                    error = False
                except ChoiceException:
                    print("Choice is Y or N.")
        else: #all other cases; will print error message and loop back to menu
            print("Invalid option.")

#quit confirmation; returns a string so that different callers can perform different actions
def quitMenu():  
    keys = input("Are you sure you want to quit? Y/N\n")
    if keys == "y" or keys == "Y":
        print("Goodbye!")
        exit()
    elif keys == "n" or keys == "N":
        pass
    else:
        raise ChoiceException
