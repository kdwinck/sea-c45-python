import random


def open_file():
    text = open("sherlock.txt", "r")
    return text


def create_words(text):
    lines = text.readlines()
    words = []
    for line in lines:
        words += line.split(' ')
    return words


def create_trigrams(words):
    trigrams = {}
    for i in range(len(words) - 2):
        curr_word = words[i] + " " + words[i + 1]
        if curr_word in trigrams:
            trigrams[curr_word].append(words[i + 2])
        else:
            trigrams[curr_word] = [words[i + 2]]
    return trigrams


def create_story(trigrams):
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
    return new_book


def close_file(text):
    text.close()


def main():
    text = open_file()
    words = create_words(text)
    words = list(map(str.strip, words))  # remove newline characters from
    trigrams = create_trigrams(words)
    new_book = create_story(trigrams)
    new_string = " ".join(new_book)
    print(new_string)

main()
