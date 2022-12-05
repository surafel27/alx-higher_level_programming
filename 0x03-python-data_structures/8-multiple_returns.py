#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        x = sentence[0]
        ln = len(sentence)
        return (ln, x)
