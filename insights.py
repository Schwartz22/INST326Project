class HealthData:
    """
    Manages and stores health information for a person, such as steps taken, 
    hours slept, height, weight, and age. Also, calculates the person's Body 
    Mass Index (BMI).
    """

    def __init__(self, steps: int, sleep: float, height: float, weight: float, age: int):
        """
        Sets up the health data for a person with their steps, sleep, height,
        weight, and age.

        :param steps: How many steps the person has taken.
        :param sleep: How many hours the person has slept.
        :param height: How tall the person is, in inches.
        :param weight: How much the person weighs, in pounds.
        :param age: The age of the person.
        """
        self.steps = steps
        self.sleep = sleep
        self.height = height
        self.weight = weight
        self.age = age

    def __str__(self) -> str:
        """
        Makes a detailed description of the person's health data into a text format,
        including steps, sleep, height, weight, age, and BMI.

        :return: A text summary of the health data.
        """
        line1 = "Steps: " + str(self.steps)
        line2 = "Sleep: " + str(self.sleep)
        line3 = "Height: " + str(self.height)
        line4 = "Weight: " + str(self.weight)
        line5 = "Age: " + str(self.age)
        line6 = "BMI: " + str(self.calculateBMI())
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6

    def calculateBMI(self) -> float:
        """
        Figures out and returns the Body Mass Index (BMI), a health number based 
        on height and weight.

        :return: The BMI, rounded to one decimal.
        """
        weightKg = float(float(self.weight)/(2.205))  # Convert pounds to kilograms
        heightMeters = float(float(self.height)*0.0254)  # Convert inches to meters
        return round(float(weightKg / (heightMeters ** 2)), 1)
