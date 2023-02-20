import json
import csv
from filterArray import filterWords

wordsInputPath = 'dataset/unigram_freq.csv'

thesaurusInputPath = 'dataset/en_thesaurus.jsonl'
thesaurusOutputPath = 'dataset/thesaurus.json'


def getWords(inputFile, filterList):
    with open(inputFile, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        output = [row[0] for row in reader if len(
            row[0]) > 2 and row[0] not in filterList]
        words = output[0:5000]

    return words


def getThesaurus(inputFile, outputFile, wordList):
    output = []
    # open jsonl, parse each line to a python dictionary
    with open(inputFile, 'r') as inFile, open(outputFile, 'w') as outFile:
        for line in inFile:
            obj = json.loads(line)
    # if x['word'] in wordlList and x['synonyms'] != []
            if obj['word'] in wordList and obj['synonyms'] != []:
                newObj = {
                    'word': obj['word'], 'pos': obj['pos'], 'synonyms': obj['synonyms']}
                output.append(newObj)
        # sort words and dump them to a json file
        sortedOutput = sorted(output, key=lambda x: x['word'])
        json.dump(sortedOutput, outFile)
    return sortedOutput


wordsArray = getWords(wordsInputPath, filterWords)

thesaurus = getThesaurus(thesaurusInputPath, thesaurusOutputPath, wordsArray)
