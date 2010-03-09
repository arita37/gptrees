#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def monte_carlo(elements, probs):
    ''' Given a vector of elements, and probabilistic
    values, an element is returned (random-picked) according
    to the given probabilities
    '''
    x = random.uniform(0, 1)
    sum = 0
    for probability, elem in zip(probs, elements):
        sum += probability
        if x < sum:
            return elem

    return elem


def monte_carlo_abs(elements, abs_freq):
    ''' Given a vector of elements, and counters (absolute frequencies)
    values, an element is returned (random-picked) according
    to the it's relative frequency used as a probability.
    '''
    SUM = float(sum(abs_freq))
    probabilities = [x / SUM for x in abs_freq]

    return monte_carlo(elements, probs)
     
            
    
    

