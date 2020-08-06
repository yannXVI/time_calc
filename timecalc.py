import datetime
import sys
import os
import time

work_time = []

def clock_start():

    minutes = 0
    hours = 0
    start_time = datetime.datetime.now()
    var1 = []

    if (start_time.hour >= 13):
        twelve_hour = start_time.hour - 12
        print("Current time (PM):")
        var1 = [twelve_hour, start_time.minute]
        print(':'.join(str(x) for x in list(var1)))
    else:
        print("Current time (AM):")
        var1 = [start_time.hour, start_time.minute]
        print(':'.join(str(x) for x in list(var1)))


    conf = input("Please confirm that you would like to start now (Y/N):")
    if (conf.lower() == "y"):
        os.system('cls')
        print("Started Clock at " + ':'.join(str(x) for x in list(var1)) + "." + " Press Enter to end.")
        input("Press any key to end.")
        os.system('cls')
        end_time = datetime.datetime.now()
        difference = end_time - start_time
        difference_in_seconds = difference.total_seconds()
        while (difference_in_seconds > 60):
            minutes += 1
            difference_in_seconds =- 60
        while (minutes > 60):
            hours += 1
            minutes =- 60

        print("Ended. You worked for: " + str(hours) + " hour(s) and " + str(minutes) + " minutes.")
        input("Press any key to exit.")
        sys.exit()

    elif (conf.lower() == "n"):
        print("Alright, returning to main menu.")
        time.sleep(3)
        os.system('cls')
        start_menu()

    else:
        input("Invalid Input. Press any key to return to Main Menu.")
        os.system('cls')
        start_menu()






def manual_time():
    print("Enter Current Time:")
    input("HH:MM :")



def start_menu():
    print("Select option:")
    print("Auto-Clock (A)")
    print("Manual Time Add (B)")
    print("List Worked Hours (C)")
    ask_input = input()
    if ask_input.lower() == "a":
        print("Entering Auto-Clock")
        input("Press any key to continue:")
        os.system('cls')
        clock_start()
    elif ask_input.lower() == "b":
        print("Entering Manual Mode")
        input("Press any key to continue:")
        os.system('cls')
        manual_time()
    else:
        input("Invalid Input. Exiting..")
        exit()


start_menu()
