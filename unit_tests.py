"""This is the file where we will conduct all of the unit tests for the functions"""
from insights import HealthData
import re
import processing_data as process
# Unit Test functions for insights.py 
def test_bmi():
  data = HealthData(steps = 5000, sleep = 7, height = 69, weight = 160, age = 17)
  calculated_bmi = 23.6
  bmi = data.calculateBMI()

  assert calculated_bmi == bmi, f"Test Failed: BMI1"

def test_bmi2():
  data = HealthData(steps = 50, sleep = 7, height = 82, weight = 240, age = 24)
  calculated_bmi = 25.1
  bmi = data.calculateBMI()

  assert calculated_bmi == bmi, f"Test Failed: BMI2"

def test_generate_recommendations():
  data = HealthData(steps = 50, sleep = 7, height = 82, weight = 240, age = 24)
  correctstr = "Sleep Recommendation: The amount of sleep you currently have per night is adequate keep up the good work. Steps Recommendation: You are doing great on steps, staying at around 10,000 steps per day is a great way to keep a healthy lifestyle. General Recommendation: Your BMI is at a good place keep up the good work."
  




# Unit Test functions for processing-data.py

