sentence = "Python programming is wonderful"
longest = ""

for word in sentence.split():
    if len(word) > len(longest):
        longest = word

print("\n7. Longest word:", longest)
