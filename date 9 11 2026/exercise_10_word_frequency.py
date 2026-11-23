sentence = "to be or not to be"
freq = {}

for word in sentence.split():
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\n10. Word frequency:")
for word in freq:
    print(word, ":", freq[word])
