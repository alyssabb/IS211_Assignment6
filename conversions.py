# Part 1

def convert_celsius_to_kelvin(celsius):
    return celsius + 273.15


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


celsius = 25.0
kelvin = convert_celsius_to_kelvin(celsius)
fahrenheit = convert_celsius_to_fahrenheit(celsius)

print(f"{celsius} degrees Celsius is equal to {kelvin} Kelvins")
print(f"{celsius} degrees Celsius is equal to {fahrenheit} Fahrenheit")
