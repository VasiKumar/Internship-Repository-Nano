my_list = [1, 2, 2, 3, 4, 4, 4, 5]
counts = {}

for item in my_list:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print("1. Duplicates:")
for item in counts:
    if counts[item] > 1:
        print(item, "appears", counts[item], "times")
