# Stage 1. Text Generator
from nltk.tokenize import WhitespaceTokenizer

f = open(input(), "r", encoding="utf-8")

# We get tokens from the corpus
wtk = WhitespaceTokenizer().tokenize(f.read())

print("Corpus statistics")
print(f"All tokens: {len(wtk)}")

# Create a set for unique words. Sets don't allow duplicate values
print(f"Unique tokens: {len(set(wtk))}\n")

option = None
while option != "exit":
    option = input()
    if option != "exit":
        try:
            print(wtk[int(option)])
        except ValueError:
            print("Type Error. Please input an integer.")
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")

f.close()
