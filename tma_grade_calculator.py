#Problem: Calculate the mean of the 3 highest marks that a student got and
        #assign a grade

#Input: list of 4 marks, interger from 0 to 100
tma_marks = [0, 55, 47, 67]

#Sub-problem: find the lowest grade in the list
lowest = tma_marks[0]
for tma_mark in tma_marks:
    if lowest > tma_mark:
        lowest = tma_mark

#Sub-problem: calculate the mean of the 3 highest marks
total = 0
#sum all 4 marks
for tma_mark in tma_marks:
    total = total + tma_mark
#substract the lowest and divide by 3 to get the mean
mean = total - lowest
mean = mean / 3

#Sub-problem: assign a grade based on the mean with nesting
if mean < 30:
    grade = 'Fail'
elif mean < 40:
    grade = 'Resit'
else:
    grade = 'Pass'

#Output
print('Your grade is', grade)
