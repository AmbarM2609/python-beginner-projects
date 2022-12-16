'''To convert temperatures from Fahrenheit to Celsius, or vice versa, you can use the following formulas
 Celsius = (Fahrenheit - 32) * (5 / 9)
 Fahrenheit = Celsius * (9 / 5) + 32'''
 
 # Get the temperature and the unit (F or C)
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (F or C): ")

# Convert the temperature to the opposite unit
if unit == "F":
    temp_converted = (temp - 32) * (5 / 9)
    print(temp, "F =", temp_converted, "C")
elif unit == "C":
    temp_converted = temp * (9 / 5) + 32
    print(temp, "C =", temp_converted, "F")
else:
    print("Invalid unit")
