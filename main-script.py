"""
This script is the main entry point for the HealthTracker application. It interacts
with the user to collect health data and provides options to display health
recommendations directly or save them to a file. It also triggers some unit tests to
ensure functionality is correct.
"""

import sys
import argparse
from insights import HealthData
import unit_tests
from processing_data import generate_recommendations, makeFile

def contains_str(input_string):
    """
    Checks if the given input string contains any non-digit characters.

    :param input_string: String to check.
    :return: True if there is any non-digit character, False otherwise.
    """
    return any(not char.isdigit() for char in input_string)

def main():
    """
    Main function that runs an input loop to collect user's health data and 
    processes it either by printing recommendations to the console or saving 
    them to a file based on the user's choice.

    It continuously prompts the user to input health metrics such as steps,
    sleep, height, weight, and age until valid inputs are provided or the user
    exits. After collecting the data, it either displays health recommendations
    or writes them to a file.
    """
    print("Welcome to HealthTracker!")
    cont = True  # Control variable for the main input loop
    print("type exit to quit at any time, if input is not valid program will exit automatically. No commas, nothing besides number should be inputted.")
    while cont:
        steps = input("Enter average number of steps taken per day: ")
        if steps.strip() != "exit" and not (contains_str(steps)):
            sleep = input("Enter average number of hours of sleep per night rounded to a whole number: ")
            if sleep.strip() != "exit" and not (contains_str(sleep)):
                height = input("Enter height in inches: ")
                if height.strip() != "exit" and not (contains_str(height)):
                    weight = input("Enter weight in pounds: ")
                    if weight.strip() != "exit" and not (contains_str(weight)):
                        age = input("Enter age in years: ")
                        if age.strip() != "exit" and not (contains_str(age)):
                            cont = False
                            data = HealthData(steps, sleep, height, weight, age)
                            print(data)  # Print the data and calculated BMI using the object's __str__ method
                            option = input("Enter 1 for printing recommendations here, or enter 2 to make a file in the current directory containing the recommendations: ")
                            
                            if option.strip() != "exit":
                                if option == "1":
                                    print(generate_recommendations(data))
                                elif option == "2":
                                    makeFile(data)
                                    print("Recommendations saved to file.")
                                else:
                                    cont = False
                                    print("invalid command")

                            else:
                                cont = False
                                print("Exiting")
                        else:
                            cont = False # Exit loop if user types 'exit'
                            print("Exiting")
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
    unit_tests.test_bmi()
    unit_tests.test_bmi2()
    unit_tests.test_generate_recommendations()
