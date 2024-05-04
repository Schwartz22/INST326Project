"""This is the file where we will conduct all of the unit tests for the functions"""
from insights import HealthData
# Unit Test functions for insights.py 
def test_bmi():
  data = HealthData(steps = 5000, sleep = 7, height = 69, weight = 160, age = 17)
  calculated_bmi = 23.6
  bmi = data.calculateBMI()

  assert calculated_bmi == bmi, f"Test Failed"

def test_bmi2():
  data = HealthData(steps = 50, sleep = 7, height = 82, weight = 240, age = 24)
  calculated_bmi = 25.1
  bmi = data.calculateBMI()

  assert calculated_bmi == bmi, f"Test Failed"



# Unit Test functions for processing-data.py

