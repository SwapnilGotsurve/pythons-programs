arr  = [11,22,9,44,55,66,77,88,99]
min = arr[0]
max = arr[0]
for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i
print("Minimum value is:", min)
print("Maximum value is:", max)