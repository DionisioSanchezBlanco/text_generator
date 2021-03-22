# Stage 2. Break the dataset into bigrams
from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams

f = open(input(), "r", encoding="utf-8")

# We get tokens from the corpus
wtk = WhitespaceTokenizer().tokenize(f.read())

# Bigrams generates an iterator. Put type list to get the data
bigr = list(bigrams(wtk))

print(f"Number of bigrams: {len(bigr)}")

option = None
while option != "exit":
    option = input()
    if option != "exit":
        try:
            print(f"Head: {bigr[int(option)][0]} Tail: {bigr[int(option)][1]}")
        except ValueError:
            print("Typ Error. Please input an integer.")
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")

f.close()
