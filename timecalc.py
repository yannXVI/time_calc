import datetime
import sys


def clock_start():

    now = datetime.datetime.now()

    if (now.hour >= 13):
        twelve_hour = now.hour - 12
    print("Current time:")
    print(twelve_hour, now.minute, now.second, sep=":",)
    conf = input("Please confirm that you would like to start now (Y/N):")
    if (conf.lower() == "y"):
        input("Started Clock. Press Enter to end.")
        print("Ended.")
        after = datetime.datetime.now()
        difference = datetime.timedelta(after, now)
        print(difference)
        sys.exit()

    else:
        input("Invalid Input. Press any key to return to Main Menu.")
        start_menu()






def manual_time():
    print("Enter Current Time:")


def start_menu():
    print("Select option:")
    print("Auto-Clock (A)")
    print("Manual Time Add (B)")
    print("List Worked Hours (C)")
    ask_input = input()
    if ask_input.lower() == "a":
        print("Entering Auto-Clock")
        input("Press any key to continue:")
        clock_start()
    elif ask_input.lower() == "b":
        print("Entering Manual Mode")
        input("Press any key to continue:")
        manual_time()
    else:
        input("Invalid Input. Press any key to exit.")
        sys.exit()


start_menu()
