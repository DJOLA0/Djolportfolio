# A code that performs NLP on a tokenised list, using spaCy library
import spacy
# English library
nlp = spacy.load('en_core_web_sm')
# Create a list of garden sentences from Wiki + given from the task
gardenpathSentences = ["The complex houses married and single soldiers and their families.",
                       "The horse raced past the barn fell.",
                       "Mary gave the child a Band-Aid.",
                       "That Jill is never here hurts.",
                       "The cotton clothing is made of grows in Mississippi."]

tokenised_list = []
# tokenise the list using append and split method
for sentence in gardenpathSentences:
    tokenised_list.append(sentence.split())

print(tokenised_list)

# entity is the text
# find the type of entity, and get a label assigned to the text using NLP
for sentence in tokenised_list:
    doc = nlp(" ".join(sentence))
    for ent in doc.ents:
        print(ent.text, ent.label_)

# the model recognises Mary and Jill as Person
# the model recognises mississippi as a GPE (geopolitical entity)
# These entities and their explanations make sense, however I would have thought NLP would recognise more entities but maybe is error on my part.