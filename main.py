run = True
while(run):
    cmdIn = input("Please input your command:")
    if(cmdIn == "end"):
        run = False
    elif(cmdIn == "holiday"):
        holiday = True
        while(holiday):
            holidayCmd = input("\tPlease input your holiday command:")
            if(holidayCmd == "end"):
                holiday=False