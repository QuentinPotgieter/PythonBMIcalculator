#python 33361908_Practical_6.py

#Assignment
print("BMI Calculator\n")

#Print Choices
print("1. Weight in pounds, height in inches")
print("2. Weight in kilograms, height in meters\n")

#Input Choice
choice = int(input("Choice: "))

#Assign Correct Measurement Text
if choice == 1:
    stringWeight = "pounds"
    stringHeight = "inches"
elif choice == 2:
    stringWeight = "kilograms"
    stringHeight = "meters"
else:
    print("Choice not accepted!")
    exit()

#Data Input
Weight = float(input("\nWeight in " + str(stringWeight) + "?: "))
Height = float(input("\nHeight in " + str(stringHeight) + "?: "))

#Calculate BMI
if choice == 1:
    float(Weight)*2.20462
    float(Height)*39.3701
    BMI = float(Weight/(Height**2)*703)
elif choice == 2:
    BMI = float(Weight/(Height**2))

#Assign Status
if BMI <= 18.5:
    Status = "Underweight"
elif 18.5 < BMI <= 25:
    Status = "Normal"
elif 25 < BMI <= 29:
    Status = "Overweight"
elif BMI >= 30:
    Status = "Obese"

#Output Data
print("\n\nResult..............\n")
print("Weight:\t\t" + str(round(Weight, 1)) + " " + stringWeight)
print("Height:\t\t" + str(round(Height, 4)) + " " + stringHeight)
print("BMI:\t\t" + str(round(BMI,1)))
print("Status:\t\t" + Status)
