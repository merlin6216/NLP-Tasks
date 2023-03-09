#basic similarity program
import spacy
nlp = spacy.load('en_core_web_sm')

#compare words line by line
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#compare all words to each other using a for loop
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#compare one sentence to other sentences
sentence_to_compare = "Why is my cat in the car"

sentences = ["Where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

#observations
#despite banana and cat having no real world similarities spacy still assigns a small correlation of 0.22
#interestingly the correlation is much lower for other fruits, for example changing word 3 to 'peach' reduces the similarity to 0.15 
#but changing word 1 can have the opposite effect, for example 'duck' returns 0.35. do ducks eat bananas?!
#it would take extensive research to see which combinations yield the highest scores between seemingly unrelated fruits and animals

#by changing the nlp to 'en_core_web_sm' the program throws out a long warning message:
#'UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. 
#This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available. 

#the results are vastly different from the 'en_core_web_md' nlp as the 'sm' model is much smaller and has less scope
