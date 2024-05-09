from insights import HealthData
import re
import processing_data as process

def test_bmi():
    """
    Tests the BMI calculation for a predefined set of health data to ensure the
    calculateBMI function returns the correct value. Uses a test case with a known
    BMI to validate correctness.
    """
    data = HealthData(steps=5000, sleep=7, height=69, weight=160, age=17)
    calculated_bmi = 23.6
    bmi = data.calculateBMI()
    assert calculated_bmi == bmi, f"Test Failed: Expected BMI {calculated_bmi}, but got {bmi}"

def test_bmi2():
    """
    Another BMI test with a different set of health data parameters to ensure the
    calculateBMI function handles varied inputs correctly. This test uses a taller and
    heavier individual to verify BMI calculations.
    """
    data = HealthData(steps=50, sleep=7, height=82, weight=240, age=24)
    calculated_bmi = 25.1
    bmi = data.calculateBMI()
    assert calculated_bmi == bmi, f"Test Failed: Expected BMI {calculated_bmi}, but got {bmi}"

def test_generate_recommendations():
    """
    Tests the generate_recommendations function to ensure it returns the correct
    recommendation string based on specific health data inputs. Validates the content
    of the recommendations to ensure accuracy and appropriateness.
    """
    data = HealthData(steps=50, sleep=7, height=82, weight=240, age=24)
    expected_rec = "Sleep Recommendation: The amount of sleep you currently have per night is adequate keep up the good work. " \
                   "Steps Recommendation: You are doing great on steps, staying at around 10,000 steps per day is a great way to keep a healthy lifestyle. " \
                   "General Recommendation: Your BMI is at a good place keep up the good work."
    actual_rec = process.generate_recommendations(data)
    assert expected_rec == actual_rec, "Test Failed: Recommendations did not match expected output."
    
# Additional unit tests for processing-data.py can be added below as needed.
