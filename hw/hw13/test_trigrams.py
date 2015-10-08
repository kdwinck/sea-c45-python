import pytest  # used for the exception testing

import trigrams


def test_open_file():
    trigrams.open_file('small_text.txt')


def test_read_words():
    lines = text.readlines()
    words = []
    for line in lines:
        words += line.split(' ')
    words = trigrams.create_words('small_text.txt')
    assert(len(words) > 0)
