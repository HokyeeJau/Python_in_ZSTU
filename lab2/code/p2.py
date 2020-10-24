# A package dealing with tokens mostly used in NLP
!pip install nltk
import nltk
nltk.download('punkt')

# Import text file
file_ad = "hamlet.txt"
with open(file_ad, "r+") as f:
    hamlet = f.readlines()  
print(type(hamlet))

# Tokenisation
tokenized_corpus = []
for sent in hamlet:
    tokens = []
    for token in sent.split(" "):
        tokens.append(token.lower())
    tokenized_corpus.append(tokens)

# Generate vocabulary set && Record the appearance
vocab_dict = {}
for sent in tokenized_corpus:
    for token in sent:
        if token in vocab_dict:
            vocab_dict[token] = vocab_dict[token] + 1
        else:
            vocab_dict[token] = 1
vocab_set = vocab_dict.keys()

sorted_vocab_dict = dict(sorted(vocab_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))

i = 0
for k,v in sorted_vocab_dict.items():
    i = i + 1
    if i == 11:
        break
    print("{}. {:<10}{:>5}".format(i, k, v))