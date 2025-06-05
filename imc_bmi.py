# Create the Function BMI = weight / height²
# BMI = IMC
def bmi(w, h):
    result = w / (h * h)
    return result

# Get the User Weight
weight = float(input('Type your weight in kilograms: '))

# Get the User Height
height = float(input('Type your height in meters: '))

# Calculate BMI using the function bmi()
bmi_result = bmi(weight, height)

# If BMI < 16 show the result "Severe Thinness"
if bmi_result < 16:
    print('Severe Thinness')

# If BMI >= 16 and BMI <= 17 show the result "Moderate Thinness"
elif bmi_result >= 16 and bmi_result <= 17:
    print('Moderate Thinness')

# If BMI > 17 and BMI <= 18.5 show the result "Mild Thinness"
elif bmi_result > 17 and bmi_result <= 18.5:
    print('Mild Thinness')

# If BMI > 18.5 and BMI <= 25 show the result "Normal"
elif bmi_result > 18.5 and bmi_result <= 25:
    print('Normal')

# If BMI > 25 and BMI <= 30 show the result "Overweight"
elif bmi_result > 25 and bmi_result <= 30:
    print('Overweight')

# If BMI > 30 and BMI <= 35 show the result "Obese Class I"
elif bmi_result > 30 and bmi_result <= 35:
    print('Obese Class I')

# If BMI > 35 and BMI <= 40 show the result "Obese Class II"
elif bmi_result > 35 and bmi_result <= 40:
    print('Obese Class II')

# If BMI > 40 show the result "Obese Class III"
elif bmi_result > 40:
    print('Obese Class III')

print(f'Your BMI is: {bmi_result}')