#menus.py: contains generic functions used for menu navigation throughout the assistant
from exceptions import ChoiceException
from assistant import assistantWrapper

#future use; area menu uses values in this list, values used as keys for trickDict, trick menu uses key to display values from trickDict
regionList = ["Kokiri Forest", "Hyrule Field", "Kakariko Village"]
trickDict = {
    "Kokiri Forest": ["Escape"],
    "Hyrule Field": ["Kak Owl Skip"],
    "Kakariko Village": ["Chickens", "SoS skip"]
}

#top level options; handles exceptions caused by submenus
def topLevelMenu():
    while True:
        keys = input("===== Speedrun practice assistant =====\n1. Legend of Zelda: OoT\n0. Quit\n")
        if keys == "1": #OOT
            error = True
            while error:
                try:
                    areaMenu()
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

#in-game region menu
def areaMenu():
    while True:
        listNo = 1
        print("Choose an in-game region:")
        for region in regionList:
            print(f"{listNo}. {region}")
            listNo += 1
        print("0. Go back")
        error = True
        keys = input()
        while error:
            if keys == "0": #return to previous menu
                return
            else: #go to specified trick menu or catch error if value doesn't exist
                try:
                    trickMenu(regionList[int(keys) - 1])
                    error = False
                except ChoiceException:
                    print("Invalid option.")
                except (IndexError, ValueError):
                    raise ChoiceException

#tricks menu for specified region in regionList
def trickMenu(region):
    error = True
    while error:
        trickList = trickDict[region]
        listNo = 1
        print("Choose a trick to practise:")
        for trick in trickList:
            print(f"{listNo}. {trick}")
            listNo += 1
        print("0. Go back")
        keys = input()
        if keys == "0": #return to previous menu
            error = False
        else:
            try:
                assistantWrapper(trickList[int(keys) - 1])
                error = False
            except (IndexError, ValueError):
                raise ChoiceException

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
