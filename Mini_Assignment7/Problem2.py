with open("a.txt", "r") as file:
    words = file.read().split()
max_len = 0
max_length_word = ""
for word in words:
    if max_len < len(word):
        max_len = len(word)
        max_length_word = word
print(max_length_word)
