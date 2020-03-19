#assistant.py: Contains the actual assistant and its wrapper function
#Author: Dean Quaife
#last edited: 2020/03/17

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
        if len(params) < 5: #if max allowed parameters is reached, stop
            keys = input(f"Type an extra parameter to track or just press enter(Max 5, current {str(len(params))})")
            if keys != "": #if user does not want more parameters, stop
                list_Maker(params, keys)
    
    print(f"====================\n{trickName}\n====================")
    keys = input("Type an extra parameter to track or just press enter(Max 5)")
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
            index = 0
            while index < len(params): #on a success, assume each section was attempted and completed
                paramsAttempts[index] += 1
                paramsSuccess[index] += 1
                index += 1
            print("easy")
        elif keys == "f" or keys =="F": #failed attempt; user can specify which part using params
            attempts += 1
            try:
                params[0] #check whether params exist
            except IndexError: #there are no params to track
                print("failed")
            else:
                error = True
                while error:
                    try:
                        paramNo = 1
                        print("Where did you fail?")
                        for param in params:
                            print(f"{paramNo}. {param}")
                            paramNo += 1
                        subkey = input()
                        params[int(subkey) - 1] #sanitises input
                        if int(subkey) == 0: #params[-1] won't raise an IndexError
                            print("Number must be one of the parameters displayed.")
                        else:
                            error = False
                    except ValueError:
                        print("Input must be a number.")
                    except IndexError:
                        print("Number must be one of the parameters displayed.")
                index = 0
                while (index < int(subkey) - 1):
                    paramsAttempts[index] += 1
                    paramsSuccess[index] += 1
                    index += 1
                paramsAttempts[index] += 1
                print(f"failed {params[index]}")
        elif keys == "s" or keys == "S": #show statistics
            if attempts == 0: #can't divide by zero!
                print("No stats to show yet. Do some attempts!")
            else:
                print(f"============================================================\nTotal attempts: {str(attempts)} | Success rate: {str(round(success/attempts*100, 2))}%")
                index = 0
                for param in params: #show stats for params if they exist
                    if paramsAttempts[index] > 0:
                        print(f"{param} has been attempted {paramsAttempts[index]} times | Success rate: {str(round(paramsSuccess[index]/paramsAttempts[index]*100, 2))}%")
                    else:
                        print(f"{param} has not been attempted yet.")
                    index += 1
                print("============================================================")
        elif keys == "h" or keys == "H": #help menu
            print("Success: just press enter!\nFailure: F\nShow current stats: S\nShow/edit paramaters: P")
            print("Quit and return to region select: Q")
        else:
            print("Bad input, try again.")
