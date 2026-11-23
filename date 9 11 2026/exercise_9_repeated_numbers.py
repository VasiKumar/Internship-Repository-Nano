numbers = [1, 2, 3, 2, 4, 3, 5, 3]
repeated = []

for n in numbers:
    if numbers.count(n) > 1 and n not in repeated:
        repeated.append(n)

print("\n9. Numbers occurring more than once:", repeated)
