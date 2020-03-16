#assistant.py: Contains the actual assistant and its wrapper function

#Speedrun assistant is run in assistant(). assistantWrapper() is called elsewhere in the
#program and is provided with a string describing the current trick. The user is given the
#option to specify extra parameters to track during the session, then assistantWrapper()
#passes control to assistant(), where the actual tracking is done.
from exceptions import ChoiceException

#wrapper function for assistant; takes a string when it is called elsewhere in the program and gives the user the choice to track extra parameters in the assistant
def assistantWrapper(trickName):
    #helper function to build list of extra parameters to assistant if any are input
    def list_Maker(params, keys):
        params.append(keys)
        if len(params) < 2: #if max allowed parameters is reached, stop
            keys = input(f"Type an extra parameter to track or just press enter(Max 2, current {str(len(params))})")
            if keys != "": #if user does not want more parameters, stop
                list_Maker(params, keys)
    
    print(f"====================\n{trickName}\n====================")
    keys = input("Type an extra parameter to track or just press enter(Max 2)")
    params = []
    if keys != "": #if there are extra params, switch to helper function
        list_Maker(params, keys)
    assistant(params)
    print("====================\n")

#base assistant; used by all other assistants
def assistant(params):
    print("====================\nType 'H' for commands")
    attempts = 0
    success = 0
    paramsAttempts = []
    paramsSuccess = []
    keys = None

    if len(params) > 0: #if user created their own parameters, add stat tracking for them
        for param in params:
            paramsAttempts.append(0)
            paramsSuccess.append(0)

    while True:
        keys = input() 
        if keys == "q" or keys == "Q": #user wants to quit
            keys = input("Press enter to confirm, type another key to cancel.\n")
            if keys == "": #if enter, return to main menu. if not, do nothing
                break
        elif keys == "": #successful attempt
            attempts += 1
            success += 1
            print("easy")
        elif keys == "f" or keys =="F": #failed attempt
            attempts += 1
            print("failed")
        elif keys == "1": #attempt at param1
            try:
                params[0]
            except IndexError:
                print("This parameter does not exist.") #can't track what isn't there!
            else:
                error = True
                while error:
                    subkey = input("Did you succeed?")
                    if subkey == "": #success
                        attempts += 1
                        success += 1
                        paramsAttempts[0] += 1
                        paramsSuccess[0] += 1
                        print("easy")
                        error = False
                    elif subkey == "f" or subkey == "F": #fail
                        attempts += 1
                        paramsAttempts[0] += 1
                        print("failed")
                        error = False
                    else:
                        print("Press enter for success, F for failure.")
        elif keys == "2": #attempt at param2
            try:
                params[1]
            except IndexError:
                print("This parameter does not exist.") #can't track what isn't there!
            else:
                error = True
                while error:
                    subkey = input("Did you succeed?")
                    if subkey == "": #success
                        attempts += 1
                        success += 1
                        paramsAttempts[1] += 1
                        paramsSuccess[1] += 1
                        print("easy")
                        error = False
                    elif subkey == "f" or subkey == "F": #fail
                        attempts += 1
                        paramsAttempts[1] += 1
                        print("failed")
                        error = False
                    else:
                        print("Press enter for success, F for failure.")
        elif keys == "s" or keys == "S": #show statistics
            if attempts == 0: #can't divide by zero!
                print("No stats to show yet. Do some attempts!")
            else:
                print(f"====================\nTotal attempts: {str(attempts)} | Success rate: {str(round(success/attempts*100, 2))}%")
                #show stats for params
                try:
                    if paramsAttempts[0] == 0: #can't divide by zero!
                        pass
                    else:
                        print(f"{params[0]}: {str(paramsAttempts[0])} | Success rate: {str(round(paramsSuccess[0]/paramsAttempts[0]*100, 2))}%")
                    if paramsAttempts[1] == 0: #can't divide by zero!
                        pass
                    else:
                        print(f"{params[1]}: {str(paramsAttempts[1])} | Success rate: {str(round(paramsSuccess[1]/paramsAttempts[1]*100, 2))}%")
                except IndexError:
                    pass
                print("====================")
        elif keys == "h" or keys == "H": #help menu
            print("Success: just press enter!\nFailure: F\nShow current stats: S")
            try:
                print(f"Attempt with {params[0]}: 1")
                print(f"Attempt with {params[1]}: 2")
            except IndexError:
                pass
            print("Quit and return to region select: Q")
        else:
            print("Bad input, try again.")
