# BMI Calculator

try:
    # User input
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters): "))

    # Validation
    if weight <= 0 or height <= 0:
        print("Error: Weight and Height must be greater than 0.")
    else:
        # BMI Calculation
        bmi = weight / (height ** 2)

        # Display BMI
        print("\n----- BMI RESULT -----")
        print(f"Your BMI is: {round(bmi, 2)}")

        # BMI Category
        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal Weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Error: Please enter valid numeric values only!")