from menus import menuPracticeChoice, menuTopLevel, quitChoice
from exceptions import ChoiceException
from assistant import escapeAssistant, kakOwlSkipAssistant

#main method; passes choice values from menu to assistant
def main():
    while True:
        error = True
        while error:
            try:
                choice = menuTopLevel()
                error = False
            except ChoiceException:
                print("Please enter a valid choice.\n====================")

        error = True
        if choice == 1: #go to practice menu
            while error:
                try:
                    choice = menuPracticeChoice()
                    error = False
                except ChoiceException:
                    print("Please enter a valid choice.\n====================")

            if choice == 0: #return to top level menu
                pass
            elif choice == 1: #kokiri forest escape
                escapeAssistant()
            elif choice == 2: #kak owl skip
                kakOwlSkipAssistant()
            else: #where assistant options go in future
                print("assistant not implemented yet\n====================")
        elif choice == 2: #confirm to quit
            while error:
                try:
                    choice = quitChoice()
                    error = False
                except ChoiceException:
                    print("Please enter a valid choice.\n====================")
            
            if choice == "y" or choice == "Y":
                print("Goodbye!\n")
                exit()
            else:
                pass

if __name__ == "__main__":
    main()