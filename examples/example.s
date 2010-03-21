%{


import random

def new_number():
    ''' Generate a random num in the 
    [-10, 10] interval.
    '''
    return random.randint(-10, 10)


%}


TREE --> BINARY;
TREE --> UNARY;
UNARY --> NUM { '0' };
UNARY --> VAR;
VAR --> 'x';

BINARY --> '+'(TREE, TREE) { _[1] + _[0] + _[2] } 
         | '-'(TREE, TREE) { _[1] + _[0] + _[2] } 
         | '*'(TREE, TREE) { _[1] + _[0] + _[2] } 
         | '/'(TREE, TREE) { _[1] + _[0] + _[2] }
;

