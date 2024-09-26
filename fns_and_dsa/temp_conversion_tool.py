
FAHRENHEIT_TO_CELSIUS_RATIO = 5 / 9
CELSIUS_TO_FAHRENHEIT_RATIO = 9 / 5

def fahrenheit_to_celsius(fahrenheit_temp):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit_temp (float): The temperature in Fahrenheit to be converted.

    Returns:
        float: The corresponding temperature in Celsius.
    """
    celsius_temp = (fahrenheit_temp - 32) * FAHRENHEIT_TO_CELSIUS_RATIO
    return celsius_temp


def celsius_to_fahrenheit(celsius_temp):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius_temp (float): The temperature in Celsius to be converted.

    Returns:
        float: The corresponding temperature in Fahrenheit.
    """
    fahrenheit_temp = (celsius_temp * CELSIUS_TO_FAHRENHEIT_RATIO) + 32
    return fahrenheit_temp


temperature_input = input("Enter the temperature value to convert: ")
scale = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

# Check if the temperature input is a valid number
try:
    temperature_value = float(temperature_input)
    
    if scale == "C":
        # Convert Celsius to Fahrenheit
        converted_temp = celsius_to_fahrenheit(temperature_value)
        print(f"{temperature_value}°C is equal to {converted_temp}°F.")
    elif scale == "F":
        # Convert Fahrenheit to Celsius
        converted_temp = fahrenheit_to_celsius(temperature_value)
        print(f"{temperature_value}°F is equal to {converted_temp}°C.")
    else:
        print("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
except ValueError:
    print("Invalid input. Please enter a valid numeric temperature value.")
