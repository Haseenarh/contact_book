def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("Convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F)? ")
if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")
