from exceptions import ChoiceException

#top level options; returns an int
def menuTopLevel():
    print("===== Speedrun practice assistant =====\n1. Start new session\n2. Quit")
    keys = input()
    if keys != "1" and keys != "2":
        raise ChoiceException
    return int(keys)

#practice menu options; returns an int
def menuPracticeChoice():
    print("What are you practising?\n1. Forest escape\n2. Kak owl skip\n3. Chickens\n4. Bottom of the Well\n0. Go back")
    keys = input()
    if keys != "1" and keys != "2" and keys != "0":
        raise ChoiceException
    return int(keys)

#quit confirmation; returns a string
def quitChoice():
    print("Are you sure you want to quit? Y/N")    
    keys = input()
    if keys != "y" and keys != "Y" and keys != "n" and keys != "N":
        raise ChoiceException
    return keys

