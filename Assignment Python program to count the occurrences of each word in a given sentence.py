"""
A python program to count the occurrences of each word in a given sentence
"""


def counter_of_word(sentence):
    word_freq = {}
    for i in sentence:
        word_freq[i] = word_freq.get(i, 0) + 1
    print(word_freq)


txt = str(input("Enter your sentence here: "))
new_txt = txt.split()

counter_of_word(new_txt)

