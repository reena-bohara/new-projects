def celsius_to_kelvin(celsius):
     # kelvin is celsius plus 273.15
    return celsius + 273.15
# input: celsius temperature
celsius = float(input("enter temperature in celsius:\n"))
# conversion
kelvin = celsius_to_kelvin(celsius)
#output: kelvin temperature
print("the temperature in kelvin is:\n%.2f" % (kelvin))
