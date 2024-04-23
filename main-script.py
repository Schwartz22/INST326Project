""" This is where we will have the main script where we implement the script for asking user data, 
and creating a file for the user that contains the analysis of the input using classes and functions. """
import sys
import argparse
from insights import HealthData
# Main function to enter the input cycle for the program
# We all worked on the main script together

def main():
    print("Welcome to HealthTracker!")
    cont = True # Control variable for the main input loop
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
                        cont = False
                        data = HealthData(steps, sleep, height, weight)
                        print(data) # Print the data and calculated BMI using the object's __str__ method
                    else:
                        cont = False # Exit loop if user types 'exit'
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
        



# Statement to call main and start the program

if __name__ == "__main__":
    main()
