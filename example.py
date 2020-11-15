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