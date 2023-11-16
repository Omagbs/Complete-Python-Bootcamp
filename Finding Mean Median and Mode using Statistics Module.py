# This code illustrates using Mean, median and mode from the statistics module

from statistics import mean, median, mode
from math import ceil

lists = [12, 23, 24, 23, 424, 5, 3, 5, 453, 53, 34, 334, 34, 23, 4, 34, 334, 3, 34, 3, 5, 4, 5, 45, 34, 545, 5]

print(lists)
print("The mean of the lists is: ", mean(lists))
print("Rounded up to whole number", ceil(mean(lists)))
print("The median of the list value is: ", median(lists))
print("The mode of the list value is: ", mode(lists))
