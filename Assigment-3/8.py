# 8. Vowel or Consonant
char = input("Enter a character: ")
if 'A' <= char <= 'Z':  # Convert to lowercase manually
    char = chr(ord(char) + 32)

if char in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")
