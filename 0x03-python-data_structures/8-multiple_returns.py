#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first = list(i[0] for i in sentence)

    if length > 0:
        return length, first
    elif length <= 0:
        return 0, 'None'


"""
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, "None")
    return (len(sentence), sentence[0])

"""
