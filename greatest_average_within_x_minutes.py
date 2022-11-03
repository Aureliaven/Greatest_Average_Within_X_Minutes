def average(x):
    sum = 0
    for i in x:
        sum += i
    return sum / len(x)

file = open(input("Enter file to read data from, separated by lines\n"), "r")

values = file.readlines()

file.close()

avg_range = int(input("Enter range\n"))

while avg_range > len(values):
    print("Range is greater than length of column data\n")
    avg_range = int(input("Enter range\n"))

for i in range(0, len(values)):
    values[i] = int(values[i])

avg = 0
greatest_avg = 0
greatest_avg_start = 0
greatest_avg_stop = 0

for i in range(0, len(values) - avg_range):
    avg = average(values[i:i+avg_range])
    if avg > greatest_avg:
        greatest_avg = avg
        greatest_avg_start = i
        greatest_avg_stop = i+avg_range

print("The greatest average is between indexes " + str(greatest_avg_start) + " and " + str(greatest_avg_stop) + "\n")
print(str(greatest_avg) + "\n")