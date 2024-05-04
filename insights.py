#Class definitions for 
# Class to manage and represent health-related data for an individual 
class HealthData:

    # Constructor to initialize the HealthData object with steps, sleep, height, and weight
    def __init__(self, steps, sleep, height, weight, age):
        self.steps = steps
        self.sleep = sleep
        self.height = height
        self.weight = weight
        self.age = age
    
    # Special method to return a string representation of the HealthData object 
    def __str__(self):
        line1 = "Steps: " + str(self.steps)
        line2 = "Sleep: " + str(self.sleep)
        line3 = "Height: " + str(self.height)
        line4 = "Weight: " + str(self.weight)
        line5 = "Age: " + str(self.age)
        line6 = "BMI: " + str(self.calculateBMI())
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6

    # Method to calculate and return the Body Mass Index (BMI) 
    def calculateBMI(self) -> float:
        weightKg = float(float(self.weight)/(2.205))
        heightMeters = float(float(self.height)*0.0254)
        return round(float(weightKg/ (heightMeters ** 2)), 1)

    


