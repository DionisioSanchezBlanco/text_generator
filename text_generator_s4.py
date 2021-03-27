# Stage 4. Generate random text
# Hint: The tail chosen will become in the new head for the next iteration

from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import Counter
import random

# f = open("../test/corpus.txt", "r", encoding="utf-8")
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

i = 1
sentence = []
while i <= 10:
    # To get different seed each time
    random.seed()

    # To get the a random head from the full tokens list
    head = random.choice(wtk)
    sentence.append(head)
    try:
        cad = "The requested word is not in the model. Please input another word."
        p = dict_bigr.setdefault(head, cad)
        if p == cad:
            print(p)
        else:
            for _i in range(9):
                list_tail = [tail for tail in dict_bigr[head]]
                dict_tail = Counter(list_tail)  # Dictionary with keys and times repeated
                word_tail = [key for key in dict_tail.keys()]
                weight_tail = [value for value in dict_tail.values()]
                head = "".join(random.choices(word_tail, weights=weight_tail, k=1))
                sentence.append(head)

        print(*sentence)
        sentence.clear()

    except ValueError:
        print("Typ Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")

    i += 1

f.close()
