import json
import csv

wordsInputPath = 'dataset/unigram_freq.csv'
wordsArray = []

thesaurusInputPath = 'dataset/en_thesaurus.jsonl'
thesaurusOutputPath = '/Users/rosinascampino/Desktop/ReactNativeCourses/synonymGame/thesaurus.json'


def getWords(inputFile):
    with open(inputFile, 'r') as file:
        reader = csv.reader(file)
        output = []
        for row in reader:
            name = row[0]
            count = int(row[1])
            d = {'name': name, 'count': count}
            output.append(d)

    outputSorted = sorted(output, key=lambda x: x['count'], reverse=True)
    return outputSorted
