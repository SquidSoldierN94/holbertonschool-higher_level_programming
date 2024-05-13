#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None, sentence
    else:
        return sentence[0], len(sentence)
