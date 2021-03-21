# Stage 1. Text Generator
from nltk.tokenize import word_tokenize

f = open("corpus.txt", "r", encoding="utf-8")

# We get tokens from the corpus
wtk = word_tokenize(f.read())

print("Corpus statistics")
print(f"All tokens: {len(wtk)}")

# Create a set for unique words. Sets don't allow duplicate values
print(f"Unique tokens: {len(set(wtk))}\n")

option = None
while option != "exit":
    try:
        print(wtk[int(input())])
    except ValueError:
        print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")

f.close()
