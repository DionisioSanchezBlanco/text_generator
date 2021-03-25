# Stage 2. Break the dataset into bigrams
from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import Counter

# f = open(input(), "r", encoding="utf-8")
f = open(input(), "r", encoding="utf-8")

# We get tokens from the corpus
wtk = WhitespaceTokenizer().tokenize(f.read())

# Bigrams generates an iterator. Put type list to get the data
bigr = list(bigrams(wtk))

dict_bigr = {}

# We create a dictionary
# Key = First value in the tuple
# Value = Second value that we store as a list associated to the key
for key, value in bigr:
    dict_bigr.setdefault(key, []).append(value)

head = None
while head != "exit":
    head = input()
    if head != "exit":
        try:
            print(f"Head: {head}")
            cad = "The requested word is not in the model. Please input another word."
            p = dict_bigr.setdefault(head, cad)
            if p == cad:
                print(p)
            else:
                list_tail = [tail for tail in dict_bigr[head]]
                dict_tail = Counter(list_tail)
                for key, values in dict_tail.most_common():
                    print(f"Tail: {key} Count: {values}")

        except ValueError:
            print("Typ Error. Please input an integer.")
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")

f.close()
