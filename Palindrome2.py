word = "cat"

reversed_word = ""

for index in range(len(word)-1,-1,-1):
    reversed_word = reversed_word + word[index]

print(reversed_word)

if word.lower() == reversed_word:
    print("PALINDROME")
else:
    print("NOT PALINDROME")