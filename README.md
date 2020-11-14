# String similarity using fuzzy matching
## What is it?
This is a fuzzy matching algorithm like fuzzywuzzy, but instead of using only one algorithm this uses 3 with a composite score available as well as access to use any of the algorithms.
## Installation
    pip install stringsim
## How does it work?
It has all of the major algorithms for fuzzy matching: cosine similarity, levenchtein distance, and ngrams (bigrams support for other numbers coming soon). This package can also find the top match from a list of a query using an unweighted average.
## What can this be used for?
Well it can be used in applications where one needs to find the best match out of a list of names etc. Can even be used for txt files.
