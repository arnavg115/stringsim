# String similarity using fuzzy matching
## What is it?
This is a fuzzy matching algorithm like fuzzywuzzy, but instead of using only one algorithm this uses 3 with a composite score available as well as access to use any of the algorithms.
## Installation
<<<<<<< HEAD
One can use pip.
```
pip install stringsim
```
or if that does not work try
```
pip3 install stringsim
```
=======
    pip install stringsim
>>>>>>> 71667c63b91b594b202c63ea2081ad93d0034bca
## How does it work?
It has all of the major algorithms for fuzzy matching: cosine similarity, levenchtein distance, and ngrams (bigrams support for other numbers coming soon). This package can also find the top match from a list of a query using an unweighted average.
## What can this be used for?
Well it can be used in applications where one needs to find the best match out of a list of names etc. Can even be used for txt files.
<<<<<<< HEAD
## Example
```python
from stringsim import txtsim as ts
#One way to import 
with open("example.txt")as txt:
    read = txt.read().split("\n")
#converts a txt into a list of elements seperated by line (see example.txt)
query = input("Enter an element here: ")
#gets an input from the user
topmatches = ts.comp(query,read)
#uses the comp method of txtsim which returns a list of tuples. Each tuple contains the name of the element and also the match score(higher is better). These are aranged in highest to lowest score.
print(topmatches[0])
#prints the best match
```
so if
```python
query = "oxygne"
```
then the program prints
```
('Oxygen', 0.7467582303206116)
```
=======
>>>>>>> 71667c63b91b594b202c63ea2081ad93d0034bca
