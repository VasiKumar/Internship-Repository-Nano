sentence = "this is is a test test sentence"
result = []

for word in sentence.split():
    if word not in result:
        result.append(word)

print("\n6. Without duplicates:", " ".join(result))
