import random

file = open("sherlock.txt", "r")

lines = file.readlines()
words = []
trigrams = {}

for line in lines:
    words += line.split(' ')

# remove newline characters from
words = list(map(str.strip, words))

# for i, word in enumerate(words):
for i in range(len(words) - 2):
    curr_word = words[i] + " " + words[i + 1]
    if curr_word in trigrams:
        trigrams[curr_word].append(words[i + 2])
    else:
        trigrams[curr_word] = [words[i + 2]]

word1 = 'Sherlock'
word2 = 'Holmes'
new_book = [word1, word2]

done = False

while not done:
    current_words = word1 + ' ' + word2
    if current_words in trigrams:
        random_value = random.choice(trigrams[current_words])
        new_book.append(random_value)
        word1 = word2
        word2 = random_value
    else:
        done = True

new_string = " ".join(new_book)
print(new_string)
