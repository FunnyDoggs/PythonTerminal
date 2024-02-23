import time;
from fakeSims import *;
variables = ["Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display","Error: variable is unset, cannot display"];
run = True;
passwordCorrect = False;
password = "gr33nb00k";
while(not passwordCorrect):
    passwordInput = input("Input the password to continue: ")
    if(passwordInput == password):
        print("Access Granted")
        passwordCorrect = True
    else:
        print("Incorrect. Access Denied.")
while(run):
    cmdIn = input("C:\\Terminal>>>")
    if (cmdIn == "end"):
        run=False
    elif(cmdIn == "holiday"):
        holiday = True
        while(holiday):
            holidayCmdIn = input("C:\\Termnal\\holiday>>>")
            if(holidayCmdIn == "valentine"):
                print("valentine:\nHello! It is Valentine\'s day!\n");
                done = False
                while (not done):
                    yours = input("Can I be yours?y/n:")
                    if (yours == "y"):
                        print("Thank You!")
                        done = True
                    elif(yours == "n"):
                        print("Thats too bad...")
                        done = True
                    else:
                        print("I don't understand...")
            elif(holidayCmdIn == "end"):
                holiday = False
            #elif(holidayCmdIn == "help"):
            #   print("\thelp:\n\t")
            else:
                print("No such holiday command: " + holidayCmdIn)
    #elif(cmdIn == "help"):
    #    print("help:\nA:\n\t\nB:\n\t\nC:\n\t\nD:\n\t\nE:\n\tend: shutdown terminal\n\t\nF:\n\t\nG:\n\t\nH:\n\thelp: show this list\n\t\nI:\n\t\nJ:\n\t\nJ:\n\t\nK:")
    elif(cmdIn == "repeatMultilineString"):
        lines = []
        currentLine = 0
        ask = True
        while(ask):
            newLine = input("Line " + str(currentLine + 1) + " value(\"end\" to finih line setup): ")
            if(newLine == "end"):
                ask = False
            else:
                lines.append(newLine)
                currentLine = currentLine + 1
        times = input("Input repetition times: ")
        interval = input("Input interval(in seconds) between each line(0 for quickest repetition): ")
        intervalRepeat = input("Input interval(in seconds) between each repetition(0 for quickest repetition): ")
        doNumberStr = input("Do number between repetitions?y/n: ")
        doNumber = False
        if(doNumberStr == "y"):
            doNumber = True
        elif(doNumberStr == "n"):
            doNumber = False
        else:
            print("Value Error!")
            run = False
            break
        i = 1
        while(i<float(times) + 1):
            if(doNumber):
                print(str(i) + ":")
            j = 0
            while(j<currentLine):
                print(lines[j])
                j = j + 1
                time.sleep(float(interval))
            time.sleep(float(intervalRepeat))
            i = i +1
    elif(cmdIn == "varSet"):
        varname = input("Variable number: ")
        if(float(varname) <= 20):
            newvalue = input("New Value:")
            variables[int(float(varname))] = newvalue
        else:
            print("Invalid Variable Number")
    elif(cmdIn == "varDisplay"):
        varname = input("Variable number: ")
        if(float(varname) <= 20):
            print(str(variables[int(float(varname))]))
        else:
            print("Invalid Variable Number")
    elif(cmdIn == "repeatString"):
        string = input("Input string to repeat: ")
        times = input("Input repetition times: ")
        interval = input("Input interval(in seconds) between each repetition(0 for quickest repetition): ")
        doNumberStr = input("Do number between repetitions?y/n: ")
        doNumber = False
        if(doNumberStr == "y"):
            doNumber = True
        elif(doNumberStr == "n"):
            doNumber = False
        else:
            print("Value Error!")
            run = False
            break
        i = 1
        while(i<float(times) + 1):
            if(doNumber):
                print(str(i) + ": " + string)
            else:
                print(string)
            time.sleep(float(interval))
            i = i +1
    elif(cmdIn == "fakeExecute"):
        fakeExecute()
    elif(cmdIn == "fakeInstall"):
        fakeInstall()
    elif(cmdIn == "fakeHack"):
        fakeHack()
    elif(cmdIn == "" or cmdIn == " " or cmdIn == "  " or cmdIn == "  " or cmdIn == "   " or cmdIn == "     " or cmdIn == "      "):
        print("Cannot accept whitespace as a command")
    else:
        print("No such command: " + cmdIn)
