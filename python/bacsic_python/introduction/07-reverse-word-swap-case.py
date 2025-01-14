import math
import os
import random
import re
import sys

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    word_list = sentence.split()
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    return reversed_sentence.swapcase()


sentence = "aWESOME is cODING"

result = reverse_words_order_and_swap_cases(sentence)

print("%s  >  %s" % (sentence, result))

    