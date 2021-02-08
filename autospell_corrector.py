import random
random.seed(1234)
import json
import nltk
nltk.download('words')
from nltk.corpus import words
from nltk import edit_distance

import pytrec_eval


#D: Dictionary of words
#C: Corpus of misspelled words paired with the word intended (correct word)
#N: top-N similar words
D = words.words()
print(f'The size of the dictionary D: {len(D)}')
N = 10

# file1 = open("data/FAWTHROP1DAT.643")

# Using readline()
filename = 'data/FAWTHROP1DAT.643'
C_file = open(filename)
count = 0
mistakes = dict()
while True:
    count += 1
    line = C_file.readline()
    if not line:
        break
    mistake_pair = line.strip().split()
    mistakes[mistake_pair[1]] = mistake_pair[0]
C_file.close()
print(f'The size of the corpus C of misspelled words: {len(mistakes.items())}')
# for word in word_list:
#     if wordnet.synsets(word):
#         common_word_list.append(word)
#     else:
#         pass

mistakes_samples = mistakes
mistakes_samples = dict()
#random selection of the list for lower the time complexity
for i in range(100):
    k, v = random.choice(list(mistakes.items()))
    mistakes_samples[k] = v
print(f'The size of the sampled corpus C of misspelled words: {len(mistakes_samples.items())}')
qrel = dict()
qret = dict()

topN = dict()
for i, (misspelled, correct) in enumerate(mistakes_samples.items()):
    misspelled = misspelled.lower()
    correct = correct.lower()
    result = dict()
    for word in D:
        word = word.lower()
        distance = edit_distance(misspelled, word)
        result[word] = distance
        #print(str(word) + ": " + str(distance))

    sorted_result = dict(sorted(result.items(), key=lambda x: x[1]))
    topN[misspelled] = {k: (-1) * sorted_result[k] for k in list(sorted_result)[:N]}

    print(f'{misspelled, correct}')
    for j, (k, v) in enumerate(topN[misspelled].items()):
        asterisk = '*' if k.lower() == correct.lower() else ''
        print(f'{k}: {v} {asterisk}')

    #prepare for metric calculation
    qrel[misspelled] = {correct: 1}
    qret[misspelled] = topN[misspelled]
    #print(qrel)
    #print(qret)

#qret['wierd'] = {'weirddiii': -1,'we': -2,'wei': -3,'weir': -4,'weirddii': -5,'weir3ddii': -6,'we33irddii': -7,'weird': -8}
#{"wierd": {"success_1": 0.0,"success_5": 0.0,"success_10": 1.0}
metrics = {'success_1', 'success_5', 'success_10'}
evaluator = pytrec_eval.RelevanceEvaluator(qrel, metrics)
results = evaluator.evaluate(qret)
avg_result = dict()
for m in metrics:
    avg_result[m] = sum([v[m] for (k, v) in results.items()])/len(results)
print(f'{filename} => {avg_result}')
