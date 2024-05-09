from insights import HealthData
import os


def makeFile(data: HealthData) -> bool:
    """
    Creates a text file named 'recommendations.txt' containing health recommendations
    based on the user's health data.

    :param data: HealthData object containing the user's health metrics.
    :return: True if the file was successfully created and written, False otherwise.
    """
    worked = False
    if os.path.exists('recommendations.txt'):
        os.remove('recommendations.txt')
    string = generate_recommendations(data)
    with open('recommendations.txt', 'w') as file:
        file.write(string)
        file.close()
        worked = True
    return worked

def generate_recommendations(data: HealthData) -> str:
    """
    Generates a string of health recommendations based on the user's health data,
    including sleep, steps, and BMI analysis.

    :param data: HealthData object containing the user's health metrics.
    :return: A string containing personalized health recommendations.
    """
    sleep = int(data.sleep)
    steps = int(data.steps)
    bmi = data.calculateBMI()
    age = int(data.age)

    age_rec = ""
    sleep_rec = ""
    steps_rec = ""
    general_rec = ""

    if age < 18:
        age_rec = "Those under 18 should always discuss with their parents/legal guardian before taking any health advice." + "\n"

    calorie_rec = "If you are a man your Basal Metablolic Rate is: " + str(data.calorie_calcM()) + "\n" + "If you are a woman it is: " + str(data.calorie_calcW()) + "\n"

    if steps < 8000:
        steps_rec = ("8,000 steps is usually recommended for all ages to promote a healthy lifestyle."
                     "\nTrying to go on at least one walk a day will help to increase steps and activity.")
    else:
        steps_rec = "You are doing great on steps, staying at around 10,000 steps per day is a great way to keep a healthy lifestyle."

    if sleep < 7:
        sleep_rec = ("The recommended minimum number of sleep is around 7 hours per night, if there is time in your lifestyle, "
                     "more sleep is always very beneficial to overall health.")
    elif sleep > 10:
        sleep_rec = ("The recommended maximum number of sleep is around 10 hours per night, consult with your primary physician about good sleeping habits.")
    else:
        sleep_rec = "The amount of sleep you currently have per night is adequate. Keep up the good work."

    if bmi < 20.0:
        general_rec = ("Your BMI is in the underweight section; this could mean more calories or less activity per day. "
                       "However, everyone is different. Consult your primary physician before making any large lifestyle changes.")
    elif bmi > 25.0:
        general_rec = ("Your BMI is in the overweight section; this could mean more steps or fewer calories per day. "
                       "However, everyone is different. Consult your primary physician before making any large lifestyle changes.")
    else:
        general_rec = "Your BMI is at a good place. Keep up the good work."

    return age_rec + "Sleep Recommendation: " + sleep_rec + "\nSteps Recommendation: " + steps_rec + "\nGeneral Recommendation: " + general_rec + calorie_rec

"""
This file contains classes and functions necessary for organizing and processing the data received from the user.
"""

