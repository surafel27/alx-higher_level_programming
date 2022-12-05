#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None)
    else:
        x = sentence[0]
        l = len(sentence)
        return (l, x)
