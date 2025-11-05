#Problem: compute the mean daily temperature over a week and print it

#input: daily temperature over a week,non-empty list, 7 list numbers, can be
#float and negative
temperatures = [5, 0, -3, 7, 8, 5, 0]

#sub-problem: sum the list items
total = 0
for temperature in temperatures:
    total = total + temperature

#sub-problem: length of the list (redundant as the list is always has 7 items)
length = 0
for temperature in temperatures:
    length = length + 1

#Output: mean, a number
mean = total / length

print('The mean of', temperatures, 'is', mean)
