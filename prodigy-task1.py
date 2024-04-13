def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

# Prompt user for input
print("Temperature Converter")
print("Options: 1 - Celsius to Fahrenheit, 2 - Celsius to Kelvin, 3 - Fahrenheit to Celsius, 4 - Fahrenheit to Kelvin, 5 - Kelvin to Celsius, 6 - Kelvin to Fahrenheit")
option = int(input("Enter option number: "))
temperature = float(input("Enter temperature value: "))

if option == 1:
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temperature))
elif option == 2:
    print("Temperature in Kelvin:", celsius_to_kelvin(temperature))
elif option == 3:
    print("Temperature in Celsius:", fahrenheit_to_celsius(temperature))
elif option == 4:
    print("Temperature in Kelvin:", fahrenheit_to_kelvin(temperature))
elif option == 5:
    print("Temperature in Celsius:", kelvin_to_celsius(temperature))
elif option == 6:
    print("Temperature in Fahrenheit:", kelvin_to_fahrenheit(temperature))
else:
    print("Invalid option. Please enter a number between 1 and 6.")