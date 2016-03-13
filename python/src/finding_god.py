import re
import itertools


# Solution to https://programmingpraxis.com/2016/02/16/finding-god/


def check_trick(text):
    words = []
    max_index = 0
    for p in itertools.ifilter(None, re.split('\n+', text)):
        for w in itertools.ifilter(None, re.split('\W+', p)):
            words.append((w, max_index))
        max_index += 1
    max_index -= 1
    end_word = end_with(words, 0, max_index)
    i = 1
    while words[i][1] == 0:
        word = end_with(words, i, max_index)
        if word != end_word:
            return ''
        i += 1
    return end_word


def end_with(words, i, max_index):
    w = words[i]
    while w[1] != max_index:
        i += len(w[0])
        w = words[i]
    return w[0]


if __name__ == '__main__':
    text = """In the beginning God created the heaven and the earth.
And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
And God said, Let there be light: and there was light."""
    print(check_trick(text))
