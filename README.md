```
Requirements:
======
	Python: 3.7   
	PyTorch: 1.1.0 

Input format:
======
Input is in CoNLL format (We use BIO tag scheme), where each character and its label are in one line. Sentences are split with a null line.

Naloxone	B-Chemical
reverses	O
the	O
antihypertensive	O
effect	O
of	O
clonidine	B-Chemical
.	O
