""" This is where we will have the main script where we implement the script for asking user data, 
and creating a file for the user that contains the analysis of the input using classes and functions. """
import sys
import argparse

# Main function to enter the input cycle for the program

def main():
    print("Welcome to EcoTracker!")
    cont = True
    print("type exit to quit at any time")
    while cont:
        steps = input("Enter average number of steps taken per day: ")
        if steps.strip() != "exit":
            sleep = input("Enter average number of hours of sleep per night: ")
            if sleep.strip() != "exit":
                height = input("Enter height in inches: ")
                if height.strip() != "exit":
                    weight = input("Enter weight in pounds: ")
                    if weight.strip() != "exit":
                        pass
                    else:
                        cont = False
                        print("Exiting")
                else: 
                    cont = False
                    print("Exiting")
            else: 
                cont = False
                print("Exiting")
        else:
            cont = False
            print("Exiting")
        

    # Example user data; in a real app, this would come from user input or a database


# Statement to call main and start the program

if __name__ == "__main__":
    main()
