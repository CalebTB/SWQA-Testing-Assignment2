def calculate_bmi(height_feet, height_inches, weight_pounds):
    # Convert height to inches
    total_height_inches = (height_feet * 12) + height_inches

    # Calculate BMI
    bmi = (weight_pounds / (total_height_inches ** 2)) * 703

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
    print("Body Mass Index Calculator")

    # Get user input
    height_feet = float(input("Enter height in feet: "))
    height_inches = float(input("Enter height in inches: "))
    weight_pounds = float(input("Enter weight in pounds: "))

    # Calculate BMI and get category
    bmi, category = calculate_bmi(height_feet, height_inches, weight_pounds)

    # Display the result
    print(f"\nBMI: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()

