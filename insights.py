#Class definitions for 

class HealthData:

    def __init__(self, steps, sleep, height, weight):
        self.steps = steps
        self.sleep = sleep
        self.height = height
        self.weight = weight
    
    def __str__(self):
        line1 = "Steps: " + str(self.steps)
        line2 = "Sleep: " + str(self.sleep)
        line3 = "Height: " + str(self.height)
        line4 = "Weight: " + str(self.weight)
        line5 = "BMI: " + str(self.calculateBMI())
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5

    def calculateBMI(self) -> float:
        weightKg = float(float(self.weight)/(2.205))
        heightMeters = float(float(self.height)*0.0254)
        return float(weightKg/ (heightMeters ** 2))

    


