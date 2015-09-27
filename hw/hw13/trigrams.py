import string

file = open("sherlock_small.txt", "r")

lines = file.readlines()
words = []
trigrams = {}

for line in lines:
    words += line.split(' ')

remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
words = [s.translate(remove_punctuation_map) for s in words]
words = list(map(str.strip, words))

for i, word in enumerate(words):
    if (i < len(words) - 2):
        trigrams[(word, words[i + 1])] = words[i + 2]

# print(str(words))
# print(str(trigrams))

new_book = ['He', 'had']

i = 0
while i < 100:
    current_words = [new_book[len(new_book) - 2], new_book[len(new_book) - 1]]
    if tuple(current_words) in trigrams:
        new_book.append(trigrams[tuple(current_words)])
    i += 1

print(new_book)
