#Processors

This README includes a simple description of what each of the processors accomplishes.
More detailed explanations of all but the bloom process can be found here https://wiki.illinois.edu/wiki/download/attachments/615490095/jmpierc2_thesis.pdf?version=1&modificationDate=1485554677000&

## Bloom
Algae's built-in 'Bloom' detector for C/C++ should have the best performance: both in computation time and total cheating caught. It uses an inverted index of token subsequences, identifier names, and literals/comments to find similar code. Thus, one should be able to get away with only running the Bloom detector in practice.

## Lazy
For each student, the Lazy pre-processor does the following to each le of interest:
* Converts all text to uppercase
* Removes all comments
* Removes all whitespace
* Removes all of the following common characters: ( ) ; , f g ' "
