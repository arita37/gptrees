# Generates A+A+A...

TREE --> '+'(TREE, TREE) { _[1] + '+' + _[2] }
    | 'A'
;


