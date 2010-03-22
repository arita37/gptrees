

S --> TREE;

TREE --> BINARY (TREE, TREE)
    | UNARY
;

BINARY --> '-'(TREE, TREE);

TREE --> OTHER;

BINARY --> '/';
BINARY --> '*';
BINARY --> '+';

UNARY --> NUM { genNum() } ;
OTHER --> 'FIN';

