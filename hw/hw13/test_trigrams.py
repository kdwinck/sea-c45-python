import pytest  # used for the exception testing

import trigrams


def test_open_file():
    trigrams.open_file('small_text.txt')


def test_create_words():
    text = trigrams.open_file('small_text.txt')
    words = []
    for line in text:
        line = line.strip()
        words += line.split(' ')
    assert(len(words) > 0)


def test_create_trigrams():
    text = trigrams.open_file('small_text.txt')
    words = []
    for line in text:
        line = line.strip()
        words += line.split(' ')
    trigrams_dic = {}
    for i in range(len(words) - 2):
        curr_word = words[i] + " " + words[i + 1]
        if curr_word in trigrams_dic:
            trigrams_dic[curr_word].append(words[i + 2])
        else:
            trigrams_dic[curr_word] = [words[i + 2]]
    assert(len(trigrams_dic) > 0)


def test_close_file():
    text = trigrams.open_file('small_text.txt')
    trigrams.close_file(text)
