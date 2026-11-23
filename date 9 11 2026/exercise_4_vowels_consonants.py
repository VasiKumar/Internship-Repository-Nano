text = "Hello World"
vowels = ""
consonants = ""

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += ch
        else:
            consonants += ch

print("\n4. Vowels:", vowels)
print("   Consonants:", consonants)
