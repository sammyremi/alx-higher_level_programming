#!/usr/bin/python3

def multiple_returns(sentence):
    lent = len(sentence)
    
    if lent == 0:
        ch = (None)
    else:
        ch = (sentence[0])
    return (lent, ch)
