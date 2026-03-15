# Simple Expert System Prototype in Python

def expert_system():
    print("Welcome to the Computer Troubleshooting Expert System")
    print("Answer the following questions with yes or no.\n")

    power = input("Does the computer power on? (yes/no): ").lower()

    if power == "no":
        print("Expert Advice: Check the power cable or power supply.")
    else:
        display = input("Is the display visible on the screen? (yes/no): ").lower()

        if display == "no":
            print("Expert Advice: Check the monitor connection or graphics card.")
        else:
            slow = input("Is the computer running very slow? (yes/no): ").lower()

            if slow == "yes":
                print("Expert Advice: Try closing unnecessary programs or scan for viruses.")
            else:
                internet = input("Is the internet not working? (yes/no): ").lower()

                if internet == "yes":
                    print("Expert Advice: Restart the router or check network settings.")
                else:
                    print("Expert Advice: Your computer seems to be working fine!")

# Run the expert system
expert_system()