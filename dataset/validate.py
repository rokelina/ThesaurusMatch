import json
import csv

wordsInputPath = 'dataset/unigram_freq.csv'


thesaurusInputPath = 'dataset/en_thesaurus.jsonl'
thesaurusOutputPath = '/Users/rosinascampino/Desktop/ReactNativeCourses/synonymGame/thesaurus.json'


def getWords(inputFile):
    with open(inputFile, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        output = [row[0] for row in reader]
        words = output[0:10000]

    return words


wordsArray = getWords(wordsInputPath)
print(wordsArray[0])
