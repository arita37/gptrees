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
UNARY --> NUM;
UNARY --> VAR;
VAR --> 'x';

BINARY --> '+'(TREE, TREE)
         | '-'(TREE, TREE)
         | '*'(TREE, TREE)
         | '/'(TREE, TREE)
;

