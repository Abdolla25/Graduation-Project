# %%
import os
import nltk
import nltk.corpus

# %%
print(os.listdir((nltk.data.find("corpora"))))


# %%
nltk.corpus.gutenberg.fileids()


# %%
hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
hamlet
# %%
for word in hamlet[:500]:
    print(word, sep=' ',end=' ')
# %%
from nltk.tokenize import word_tokenize
text = "Natural Language Processing (or Text Analytics/Text Mining) applies analytic tools to learn from collections of text data, like social media, books, newspapers, emails, etc. The goal can be considered to be similar to humans learning by reading such material. However, using automated algorithms we can learn from massive amounts of text, very much more than a human can. It is bringing a new revolution by giving rise to chatbots and virtual assistants to help one system address queries of millions of users."
textTokens = word_tokenize(text)
textTokens
# %%
len(textTokens)
# %%
from nltk.probability import FreqDist
fdist = FreqDist()
for word in textTokens:
    fdist[word.lower()]+=1
fdist
# %%
fdistTop10 = fdist.most_common(10)
fdistTop10
# %%
from nltk.tokenize import blankline_tokenize
textBlank = blankline_tokenize(text)
len(textBlank)
# %%

# %%
