def convert_temperature(value, from_unit, to_unit):
    conversion_dict = {
        'C': {'F': lambda c: (c * 9/5) + 32, 'K': lambda c: c + 273.15},
        'F': {'C': lambda f: (f - 32) * 5/9, 'K': lambda f: (f - 32) * 5/9 + 273.15},
        'K': {'C': lambda k: k - 273.15, 'F': lambda k: (k - 273.15) * 9/5 + 32}
    }

    if from_unit == to_unit:
        return f"{value} {from_unit} is already the desired unit."

    if from_unit not in conversion_dict or to_unit not in conversion_dict[from_unit]:
        return "Invalid unit conversion requested."

    conversion_function = conversion_dict[from_unit][to_unit]
    converted_value = conversion_function(value)
    return f"{value} {from_unit} = {converted_value:.2f} {to_unit}"

def main():
    print("Temperature Converter")
    try:
        value = float(input("Enter the temperature value: "))
        from_unit = input("Enter the unit to convert from (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
        to_unit = input("Enter the unit to convert to (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

        result = convert_temperature(value, from_unit, to_unit)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid number for the temperature.")

if __name__ == "__main__":
    main()
