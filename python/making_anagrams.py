#!/bin/env python

def number_needed(a, b):

    # determine the minimum number of character deletions required to make and anagrams.
    
    COUNTER = 0
    
    a_chr = {}
    for i in a:
        if a_chr.has_key(i):
            a_chr[i] = a_chr[i] + 1
        else:
            a_chr[i] = 1
    b_chr = {}
    for i in b:
        if b_chr.has_key(i):
            b_chr[i] = b_chr[i] + 1
        else:
            b_chr[i] = 1
            
    for i in range(97,123):
        if a_chr.has_key(chr(i)) and b_chr.has_key(chr(i)):
            COUNTER = COUNTER + abs(a_chr[chr(i)]-b_chr[chr(i)])
        elif a_chr.has_key(chr(i)):
            COUNTER = COUNTER + a_chr[chr(i)]
        elif b_chr.has_key(chr(i)):
            COUNTER = COUNTER + b_chr[chr(i)]
            
    return COUNTER

a = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
b = 'fcrxzwscanmligyxyvym'
print number_needed(a,b)
