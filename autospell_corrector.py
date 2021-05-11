import nltk
nltk.download('words')
from nltk.corpus import words
from nltk import edit_distance

# file1 = open("data/FAWTHROP1DAT.643")

# Using readline()

#Open and read pairs in a dictionary
file1 = open("data/FAWTHROP1DAT.643")
count = 0
mistakes = dict()
while True:
    count += 1
    line = file1.readline()
    if not line:
        break
    mistake_pair = line.strip().split()
    mistakes[mistake_pair[1]] = mistake_pair[0]
file1.close()

#Get List of Words from NLTK word list
word_list = words.words()
common_word_list = []


result = dict()
positions = []

#Calculate Levenshtien distance and suggest correct word based on that
for index, (key, value) in enumerate(mistakes.items()):
    if index % 27 == 0:
        print(key, value)
        key = 'ABBATOIR'
        value = 'ABATTOIR'
        for word in word_list:
            distance = edit_distance(key.upper(), word.upper())
            result[word] = distance
            print(str(word) + ": " + str(distance))
            y = 2
        sorted_result = dict(sorted(result.items(), key=lambda x: x[1]))
        result2 = {k: sorted_result[k] for k in list(sorted_result)[:10]}
        positions.append(result2.get(str(value).lower()))
        print("For the mistake " + key.lower() + ", the correct word " + value.lower()
              + " was found at " + str(result2.get(str(value).lower())))
        result = dict()

ewr = 4
