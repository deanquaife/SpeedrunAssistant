#OOTmenus.py: OOT specific menu functions
from exceptions import ChoiceException
from assistant import assistantWrapper

#future use; area menu uses values in this list, values used as keys for trickDict, trick menu uses key to display values from trickDict
regionList = ["Kokiri Forest"]
trickDict = {
    "Kokiri Forest": ["Escape"],
    "Kakariko Village": ["Chickens", "SoS skip"]
}

#OOT in-game region menu
def ootAreaMenu():
    while True:
        keys = input("Choose an in-game region:\n1. Kokiri Forest\n0. Go back\n")
        if keys == "1":
            error = True
            while error:
                try:
                    ootForestMenu()
                    error = False
                except ChoiceException:
                    print("Invalid option.")
        elif keys == "0":
            break
        else:
            raise ChoiceException

#tricks menu for Kokiri Forest
def ootForestMenu():
    keys = input("Choose a trick to practise:\n1. Escape\n0. Go back\n")
    if keys == "1":
        assistantWrapper("Kokiri Forest Escape")
    elif keys == "0":
        pass
    else:
        raise ChoiceException