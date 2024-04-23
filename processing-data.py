"""
This file will be for processing the data and will contain classes and functions 
neccessary for organization of the data from the user

"""

#Class definitions for 

class HealthData:

    def __init__(self, steps, sleep, height, weight):
        self.steps = steps
        self.sleep = sleep
        self.height = height
        self.weight = weight
    
    def __str__(self):
        print("Steps: " + str(self.steps))
        print("Sleep: " + str(self.sleep))
        print("Height: " + str(self.height))
        print("Weight: " + str(self.weight))

    def calculateBMI(self):
        weightKg = float(self.weight/(2.205))
        height = heigh