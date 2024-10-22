import pandas as pd
import random

data = pd.read_csv("phrases.csv")

nouns = data["noun"].dropna().str.strip()
verbs = data["verbs"].dropna().str.strip()
adjectives = data["adjectives"].dropna().str.strip()
adverbs = data["adverbs"].dropna().str.strip()
miscellaneous = data["miscellaneous"].dropna().str.strip()
prepositions = data["prepositions"].dropna().str.strip()

data_list = [nouns, adjectives, verbs, adverbs, prepositions, miscellaneous]

def generate_passphrase(num_words):
    phrase = ""
    for i in range(num_words):
        word_list = random.choice(data_list)
        word = random.choice(word_list.values)
        
        word = word.replace(" ", "")
        
        phrase += word

    return phrase  

# num_words_in_passphrase = 10 
# for i in range(10):
print(generate_passphrase(10))
