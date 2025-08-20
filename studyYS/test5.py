sentence = input("Enter the sentence: ")
words = sentence.split()

longest_word = ""
max_legnth = 0

for word in words:
    if len(word) > max_legnth:
        longest_word = word
        max_legnth = len(word)

print("Longest word:", longest_word)
print("Length:", max_legnth)