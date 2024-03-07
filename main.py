import random
import time


def calculate_bmi(height_feet, height_inches, weight_pounds):
    # Convert height to inches
    total_height_inches = (height_feet * 12) + height_inches

    # Metric Conversions
    height_metric_meters = total_height_inches * 0.025
    weight_metric_kg = weight_pounds * 0.45

    # Calculate BMI
    bmi = round(weight_metric_kg / (height_metric_meters ** 2), 1)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


def main():
    print(" Welcome to the Body Mass Index Calculator\n")
    print("-------------------------------------------")
    print("What would like to choose from the following options?")
    print("-------------------------------------------\n")
    print("1.) Calculate Own BMI")
    print("2.) Randomly Generated BMI")
    print("3.) Exit the program")

    user_input = ""
    while user_input != "3":
        user_input = input("\nEnter: ")
        match user_input:
            case "1":
                # Get user input
                height_feet_str = input("Enter height in feet: ").strip()
                height_inches_str = input("Enter height in inches: ").strip()
                weight_pounds_str = input("Enter weight in pounds: ").strip()

                # Check if any input is empty
                if not height_feet_str or not height_inches_str or not weight_pounds_str:
                    print("Please enter valid numeric values for height and weight.")
                    continue

                # Convert input to float
                height_feet = float(height_feet_str)
                height_inches = float(height_inches_str)
                weight_pounds = float(weight_pounds_str)

                # Calculate BMI and get category
                bmi, category = calculate_bmi(height_feet, height_inches, weight_pounds)

                # Display the result
                print(f"\nBMI: {bmi:.2f}")
                print(f"Category: {category}")

            case "2":
                height_feet = random.randint(1, 7)
                height_inches = random.randint(1, 11)
                weight_pounds = random.randint(1, 1000)

                print(f"Height in feet: {height_feet}")
                print(f"Height in inches: {height_inches}")
                print(f"Weight in Pounds: {weight_pounds}")

                bmi, category = calculate_bmi(height_feet, height_inches, weight_pounds)
                print(f"\nBMI: {bmi:.2f}")
                print(f"Category: {category}")

            case "3":
                print("EXITING PROGRAM...")
                time.sleep(3)
                break

            case _:
                print("That is not an option. Please pick a number 1-3")


if __name__ == "__main__":
    main()
