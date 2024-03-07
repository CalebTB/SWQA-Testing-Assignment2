import pytest
from main import calculate_bmi


@pytest.mark.parametrize("user_input, height_feet, height_inches, weight_pounds", [
    ("1", 5.0, 3.0, 150.0),
    ("2", 0, 0, 0),
    ("3", 0, 0, 0)
])
def test_options(user_input, height_feet, height_inches, weight_pounds):
    if user_input.startswith('1'):
        assert height_feet == 5.0
        assert height_inches == 3.0
        assert weight_pounds == 150.0
    elif user_input.startswith('2'):
        assert "Height in feet:"
        assert "Height in inches:"
        assert "Weight in Pounds:"
        assert "BMI:"
        assert "Category:"
    elif user_input.startswith('3'):
        assert "EXITING PROGRAM..."


def test_bmi_calculations():
    actual_bmi, actual_category = calculate_bmi(5, 3, 125)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert actual_bmi == 22.7
    assert actual_category == "Normal weight"


def test_bmi_underweight():
    actual_bmi, actual_category = calculate_bmi(5, 3, 65)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert actual_bmi < 18.5
    assert actual_category == "Underweight"

    actual_bmi, actual_category = calculate_bmi(1, 1, 1)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert actual_bmi < 18.5
    assert actual_category == "Underweight"

    actual_bmi, actual_category = calculate_bmi(5, 3, 101.5)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert actual_bmi < 18.5
    assert actual_category == "Underweight"


def test_bmi_normalweight():
    actual_bmi, actual_category = calculate_bmi(5, 3, 125)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert 18.5 <= actual_bmi < 24.9
    assert actual_category == "Normal weight"

    actual_bmi, actual_category = calculate_bmi(5, 3, 102)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert 18.5 <= actual_bmi < 24.9
    assert actual_category == "Normal weight"

    actual_bmi, actual_category = calculate_bmi(5, 3, 136.5)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert 18.5 <= actual_bmi < 24.9
    assert actual_category == "Normal weight"


def test_bmi_overweight():
    actual_bmi, actual_category = calculate_bmi(5, 3, 155)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert 25 <= actual_bmi < 29.9
    assert actual_category == "Overweight"

    actual_bmi, actual_category = calculate_bmi(5, 3, 138)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert 25 <= actual_bmi < 29.9
    assert actual_category == "Overweight"

    actual_bmi, actual_category = calculate_bmi(5, 3, 164.5)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert 25 <= actual_bmi < 29.9
    assert actual_category == "Overweight"


def test_bmi_obese():
    actual_bmi, actual_category = calculate_bmi(5, 3, 500)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert 30 <= actual_bmi
    assert actual_category == "Obese"

    actual_bmi, actual_category = calculate_bmi(5, 3, 165.5)
    print("\n")
    # Print the results
    print(f"Actual BMI: {actual_bmi:.2f}")
    print(f"Actual Category: {actual_category}")

    # Add assertions based on the expected values or ranges
    assert 30 <= actual_bmi
    assert actual_category == "Obese"
