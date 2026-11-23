sentence = "the cat and the dog and the bird"
words = sentence.split()
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

most_word = ""
most_count = 0
for word in counts:
    if counts[word] > most_count:
        most_word = word
        most_count = counts[word]

print("\n3. Most frequent word:", most_word, "(", most_count, "times )")
