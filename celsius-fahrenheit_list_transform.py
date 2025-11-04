#Problem: Convert a list of temperatures in Celsius to a list in Fahrenheit

# Input: a possibly empty list of temperatures in Celsius
celsius_temperature = [28, 33, 29, 32, 27]

#Output: list to hold the temperatures in fahrenheit
fahrenheit_temperature = []

#iteration and transformation of the list celsius to fahrenheit
for celsius in celsius_temperature:
    fahrenheit = celsius * 1.8 + 32
    fahrenheit_temperature = fahrenheit_temperature + [fahrenheit]
#print the final list (output)
print('The temperatures in Fahrenheit are', fahrenheit_temperature)
