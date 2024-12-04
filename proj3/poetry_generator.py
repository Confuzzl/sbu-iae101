# IAE 101
# Project 03 - Poetry Generator
# Vincent Yang
# 116579508
# viyyang
# 11/16/24
# poetry_generator.py (v.7)

import nltk
import pronouncing
import random
from typing import Generator

pre_my_corpus = []

# This uses the King James Bible as the corpus
# Use: nltk.corpus.gutenberg.fileids()
# to see which other gutenberg works are available.
pre_my_corpus = nltk.corpus.gutenberg.words('bible-kjv.txt')

# This uses all the words in the entire gutenberg corpus
# pre_my_corpus = nltk.corpus.gutenberg.words()

# This loop constructs a corpus from all the shakespeare plays included in the
# shakespeare corpus included in NLTK
# Use: nltk.corpus.shakespeare.fileids()
# to see which shakespeare works are included.

# for fid in nltk.corpus.shakespeare.fileids():
#     pre_my_corpus += nltk.corpus.shakespeare.words(fid)
# pre_my_corpus: Generator[str, None, None] = (word for fid in nltk.corpus.shakespeare.fileids() for word in nltk.corpus.shakespeare.words(
#     fid))


# my_corpus: list[str] = []
# for w in pre_my_corpus:
#     my_corpus.append(w.lower())
my_corpus = [w.lower() for w in pre_my_corpus]

bigrams = nltk.bigrams(my_corpus)
cfd = nltk.ConditionalFreqDist(bigrams)

# next_word_generator
# This function...


def next_word_generator(source: str = None) -> str:
    result = None
    # print()
    # print("SOURCE:", source)
    if (source == None) or (source not in cfd) or (not source.isalpha()):
        while result == None or not result.isalpha():
            result = random.choice(my_corpus)
    else:
        # print("CFD ENTRY:")
        # print(cfd[source])
        init_list = list(cfd[source].elements())
        # print("INIT_LIST:")
        # print(init_list)
        choice_list = [x for x in init_list if x.isalpha()]
        # print("CHOICE_LIST:")
        # print(choice_list)
        # print()
        if len(choice_list) > 0:
            result = random.choice(choice_list)
        else:
            while result == None or not result.isalpha():
                result = random.choice(my_corpus)
    return result


# This function takes a single input:
# word - a string representing a word
# The function returns the number of syllables in word as an
# integer.
# If the return value is 0, then word is not available in the CMU
# dictionary.
def count_syllables(word: str):
    phones = pronouncing.phones_for_word(word)
    count_list = [pronouncing.syllable_count(x) for x in phones]
    if len(count_list) > 0:
        result = max(count_list)
    else:
        result = 0
    return result

# This function takes a single input:
# word - a string representing a word
# The function returns a list of words that rhyme with
# the input word.


def get_rhymes(word: str):
    # result = []
    # pre_result = pronouncing.rhymes(word)
    # for w in pre_result:
    #     if w in my_corpus:
    #         result.append(w)
    # # print()
    # # print("PRE_RESULT:", len(pre_result))
    # # print(pre_result)
    # # print("RESULT:", len(result))
    # # print(result)
    # # print()
    # return result
    return [w for w in pronouncing.rhymes(word) if w in my_corpus]

# This function takes a single input:
# word - a string representing a word
# The function returns a list of strings. Each string in the list
# is a sequence of numbers. Each number corresponds to a syllable
# in the word and describes the stress placed on that syllable
# when the word is pronounced.
# A '1' indicates primary stress on the syllable
# A '2' indicates secondary stress on the syllable
# A '0' indicates the syllable is unstressed.
# Each element of the list indicates a different way to pronounce
# the input word.


def get_stresses(word):
    result = pronouncing.stresses_for_word(word)
    return result

# A test function that demonstrates how each of the helper functions included
# in this file work.  You supply a word and it will run each of the above
# functions on that word.


def test():
    keep_going = True
    while keep_going:
        sw = input("Please enter a word (Enter '0' to quit): ")
        if sw == '0':
            keep_going = False
        elif sw == "":
            pass
        else:
            print("Random 5 words following", sw)
            wl = [sw]
            iw = sw
            for i in range(4):
                elements = list(cfd[iw].elements())
                print()
                nw = next_word_generator(iw)
                print("NW:", nw)
                print("COUNT:", elements.count(nw))
                print()
                wl.append(nw)
                iw = nw
            print(" ".join(wl))
            print()
            print("Pronunciations of", sw)
            print(pronouncing.phones_for_word(sw))
            print()
            print("Syllables in", sw)
            print(count_syllables(sw))
            print()
            print("Rhymes for", sw)
            print(get_rhymes(sw))
            print()
            print("Stresses for", sw)
            print(get_stresses(sw))
            print()


############################################################
##                                                         #
### STUDENT SECTION                                        #
##                                                         #
############################################################

# generate_rhyming_line()
# Complete this function so that it returns a list. The list
# must contain two strings of 5 words each. Each string
# corresponds to a line. The two lines you return must rhyme.
def generate_rhyming_lines():
    def prelude():
        return " ".join([next_word_generator() for _ in range(4)])
    word = None
    rhyme_list = []
    while len(rhyme_list) == 0:
        word = next_word_generator()
        rhyme_list = get_rhymes(word)
    return (f"{prelude()} {word}", f"{prelude()} {random.choice(rhyme_list)}")


# generate_10_syllable_lines()
# Complete this function so that it returns a list. The list
# must contain two strings of 10 syllables each. Each string
# corresponds to a line and each line must be composed of words
# whose number of syllables add up to 10 syllables total.


def generate_10_syllable_lines():
    def line():
        syllables = 0
        line: list[str] = []
        while syllables != 10:
            word = next_word_generator()
            s = count_syllables(word)
            if s == 0 or syllables + s > 10:
                continue
            line.append(word)
            syllables += s
        return " ".join(line)
    return (line(), line())


ALLOW_SECONDARY_STRESS = True


def normalize_stress(stress: str):
    return "".join([("1" if ALLOW_SECONDARY_STRESS else "0")
                    if char == "2" else char for char in stress])


def is_alternating(start, stress):
    return True if stress == "" else False if stress[0] != str(
        start) else is_alternating(start ^ 1, stress[1:])


def generate_metered_line_full(length):
    syllables = 0
    last_stress = 1
    line: list[str] = []
    line_stresses: list[str] = []
    while syllables < length:

        this_stress = last_stress ^ 1

        word = next_word_generator()
        s = count_syllables(word)
        if s == 0 or syllables + s > length:
            continue
        word_stress = [normalize_stress(stress) for stress in get_stresses(
            word)]

        valid = False
        valid_stress = None
        for stress in word_stress:
            # THERE MAY BE A MISMATCH BETWEEN SYLLABLE AND STRESS COUNT "desperate"
            if len(stress) == s and is_alternating(this_stress, stress):
                valid = True
                valid_stress = stress
                break

        if not valid:
            continue
        line.append(word)
        syllables += s
        line_stresses.append(valid_stress)

        # bit magic
        last_stress ^= (s % 2)

    return (" ".join(line), " ".join(line_stresses))

# generate_metered_line()
# Complete this function so that it returns a string. This string
# will be composed of randonly selected words, will contain 10
# syllables, and the rhythm of the line must match the following
# pattern of stresses: 0101010101


def generate_metered_line():
    return generate_metered_line_full(10)[0]

# generate_line()
# Use this function to generate each line of your poem.
# This is where you will implement the rules that govern
# the construction of each line.
# For example:
#     -number of words or syllables in line
#     -stress pattern for line (meter)
#     -last word choice constrained by rhyming pattern
# Add any parameters to this function you need to bring in
# information about how a particular line should be constructed.


def generate_line(final_word: str, final_word_syllables: int):
    prelude, prelude_stresses = generate_metered_line_full(
        10 - final_word_syllables)
    stresses = get_stresses(final_word)
    stress_start = final_word_syllables % 2
    for stress in stresses:
        if (is_alternating(stress_start, stress)):
            return (f"{prelude} {final_word}", f"{prelude_stresses} {stress}")
    return [None, None]


# generate_poem()
# Use this function to construct your poem, line by line.
# This is where you will implement the rules that govern
# the structure of your poem.
# For example:
#     -The total number of lines
#     -How the lines relate to each other (rhyming, syllable counts, etc)


def generate_poem():
    # ABAB rhyme scheme
    SHOW_STRESSES = False
    NUM_STANZAS = 2

    STANZAS = []

    def generate_line_pair() -> tuple[tuple[str, str], tuple[str, str]]:
        final = next_word_generator()
        all_rhymes = []
        while len(all_rhymes) < 2 or (s := count_syllables(final)) == 0:
            final = next_word_generator()
            all_rhymes = get_rhymes(final)
        rhyme_pair = random.sample(all_rhymes, 2)

        first, first_stresses = generate_line(rhyme_pair[0], s)
        if (first == None):
            return generate_line_pair()
        second, second_stresses = generate_line(rhyme_pair[1], s)
        if (second == None):
            return generate_line_pair()
        return ((first, first_stresses), (second, second_stresses))

    for _ in range(NUM_STANZAS):
        A1, A2 = generate_line_pair()
        B1, B2 = generate_line_pair()
        stanza = ""
        for line, stresses in [A1, B1, A2, B2]:
            if (SHOW_STRESSES):
                stresses_padded = " ".join([
                    f"{stress: <{len(word)}}" for word, stress in zip(line.split(" "), stresses.split(" "))])
                stanza += f"{line}\n{stresses_padded}\n"
            else:
                stanza += f"{line}\n"
        STANZAS.append(stanza)

    return "\n\n".join(STANZAS)


if __name__ == "__main__":
    # print(generate_rhyming_lines())
    # print(generate_10_syllable_lines())
    # print(generate_metered_line())
    print(generate_poem())

    # test()
    # print()

    # result1 = generate_rhyming_lines()
    # print("RHYMING LINES:")
    # print(result1)
    # print()
    # #
    # result2 = generate_10_syllable_lines()
    # print("10 SYLLABLE LINES:")
    # print(result2)
    # print()
    # #
    # result3 = generate_metered_line()
    # print("METERED LINE:")
    # print(result3)
    # print()
    # #
    # my_poem = generate_poem()
    # print("A POEM:")
    # print(my_poem)
    print("\n\nIf this is all you see, try uncommenting some lines in main.\n\n")
