### Tracking your BMI is a useful way of checking if you're maintaining a healthy weight. It's calculated using a persons' weight and height using the formula (weight/height^2).
### The resulting number indicates one of the following categories:
# Underweight = less than 18.5
# Normal = Greater/equal to 18.5 but less than 25
# Overweight = Greater/equal to 25 but less than 30
# Obesity = 30 or more
## Create a program that takes a person's weight and height as input and output corresponding BMI category.



def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        bmi = calculate_bmi(weight, height)
        category = determine_bmi_category(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Your BMI category is: {category}")

    except ValueError:
        print("Invalid input. Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()



