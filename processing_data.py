"""This will contain the functions and classes neccessary for creating a file 
for the user containing the corresponding health insights based on the info given."""
from insights import HealthData
def makeFile():

    """
    Calculates the estimated carbon footprint based on user input data.
    Args:
        transport_data (dict): User transportation habits.
        energy_data (dict): User home energy consumption.
        diet_data (dict): User dietary preferences.
    Returns:
        float: Estimated carbon footprint in kilograms of CO2 equivalent.
    """
    # Placeholder for simplicity; implement actual calculations based on data
    return 1000.0


def generate_recommendations(data: HealthData):
    sleep = int(data.sleep)
    steps = int(data.steps)
    bmi = data.calculateBMI()
    
    sleep_rec = ""
    steps_rec = ""
    general_rec = ""

    if steps < 8000:
        steps_rec = "8,000 steps is usually recommended for all ages to promote a healthy lifestyle." + "\n" + "Trying to go on at least one walk a day will help to increase steps and activity."
    else: 
        steps_rec = "You are doing great on steps, staying at around 10,000 steps per day is a great way to keep a healthy lifestyle."
    if sleep < 7:
        sleep_rec = "The recommended minimum number of sleep is around 7 hours per night, if there is time in your lifestyle, more sleep is always very beneficial to overall health."
    elif sleep > 10:
        sleep_rec = "The recommended maximum number of sleep is around 10 hours per night, consult with your primary physician about good sleeping habits."
    else:
        sleep_rec = "The amount of sleep you currently have per night is adequate keep up the good work."
    if bmi < 20.0:
        general_rec = "Your BMI is in the under section, this could mean more calories or less activity per day, however everyone is different consult your primary physician before making any large lifestyle changes."
    elif bmi > 25.0:
        general_rec = "Your BMI is in the overweight section, this could mean more steps or less calories per day, however everyone is different consult your primary physician before making any large lifestyle changes."
    else:
        general_rec = "Your BMI is at a good place keep up the good work."
    

    return "Sleep Recommendation: " + sleep_rec + "\n" + "Steps Recommendation: " + steps_rec + "\n" + "General Recommendation: " + general_rec


"""
This file will be for processing the data and will contain classes and functions 
neccessary for organization of the data from the user

"""

