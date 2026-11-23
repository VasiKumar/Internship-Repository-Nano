s1 = "python"
s2 = "typhoon"
common = ""

for ch in s1:
    if ch in s2 and ch not in common:
        common += ch

print("\n5. Common characters:", common)
