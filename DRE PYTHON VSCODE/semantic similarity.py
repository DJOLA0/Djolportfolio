import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# if the word comparison is dissimilar = closer to 0.0 
# if the word comparison is similar = closer to 1. 
''''''


# code for when you want to compare a series of words to one another
tokens = nlp('cat apple monkey banana ')

for token1 in tokens:   # compare one word (token1) to all other 'tokens' in string
    for token2 in tokens: # do the same for the next word
        print(token1.text, token2.text, token1.similarity(token2))

# cat and monkey are both similar because they are both animals (0.59)
# banana and apple are similar because they are both fruits (0.66)
# monkey and banana (0.40) have a higher similarity than monkey and apple (0.2)
''''''

sentence_to_compare = "why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, this is my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)