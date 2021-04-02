# Stage 6. Generate sentences based on trigrams

from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from nltk.util import trigrams
from collections import Counter
import random
import re


# To get the a random head from the full tokens list to initialize the sentence
# Match to ini_word
def get_head(head, ini_word):
    result = ""
    while not result:
        head = random.choice(list(dict_trig.keys()))
        first_word = head.split()
        result = re.match(ini_word, first_word[0])

    return head


# To get the final word matching to RegExp
def get_final(tail, final_word):
    return re.match(final_word, tail)


# f = open("../test/corpus.txt", "r", encoding="utf-8")
f = open(input(), "r", encoding="utf-8")

# We get tokens from the corpus
wtk = WhitespaceTokenizer().tokenize(f.read())

# Trigrams generates an iterator. Put type list to get the data
# bigr = list(bigrams(wtk))
trig = list(trigrams(wtk))
dict_trig = {}

# We create a dictionary
# Key = First value in the tuple
# Value = Second value that we store as a list associated to the key
for key1, key2, value in trig:
    key = f"{key1} {key2}"
    dict_trig.setdefault(key, []).append(value)

# RegExp templates
ini_word = "[A-Z].+[^\.\!\?]$"
final_word = "[A-z].+[\.\!\?]"

head = None
i = 1
sentence = []

while i <= 10:
    # To get different seed each time
    random.seed()
    head = get_head(head, ini_word)
    sentence.append(head)
    result_final = ""

    while not result_final:
        new_head = head.split()
        list_tail = [tail for tail in dict_trig[head]]
        dict_tail = Counter(list_tail)  # Dictionary with keys and times repeated
        word_tail = [key for key in dict_tail.keys()]
        weight_tail = [value for value in dict_tail.values()]
        head = "".join(random.choices(word_tail, weights=weight_tail, k=1))
        result_final = get_final(head, final_word)
        sentence.append(head)

        if result_final and len(sentence) < 4:
            result_final = None

        head = f"{new_head[1]} {head}"
    print(*sentence)
    sentence.clear()

    i += 1

f.close()
