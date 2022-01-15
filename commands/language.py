from nltk.tokenize import sent_tokenize, word_tokenize

simple_text = "Hello Mr. Henrique, how are you doing today? The weather is great and Python is awesome."

''' print(sent_tokenize(simple_text))

print(word_tokenize(simple_text)) '''

for i in word_tokenize(simple_text):
    print(i)