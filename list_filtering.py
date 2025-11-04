#Problem: Given a list of temperatures, construct another list that only records any temperature above 30


# Input: list of temperatures recorded
temperature_record = [28, 33, 29, 32, 27]

# Input: Threshold of temperatures to be filtered
threshold = 30

# Output: list for temperatures above threshold
temperature_above_threshold = []

# List iteration and filter
for temperature in temperature_record:
    if temperature > threshold:
        temperature_above_threshold = temperature_above_threshold + [temperature]

#Print output
print('The hot days had temperatures', temperature_above_threshold)
