
# This will trigger an error on BINARY '+'
# duplicated definition.

TREE --> BINARY
	| UNARY
;

BINARY --> '+' (TREE, TREE)
	| '-' (TREE, TREE)
	| '+' (TREE, TREE)
;

