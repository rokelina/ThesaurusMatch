import json
import csv

wordsInputPath = 'dataset/unigram_freq.csv'


thesaurusInputPath = 'dataset/en_thesaurus.jsonl'
thesaurusOutputPath = '/Users/rosinascampino/Desktop/ReactNativeCourses/synonymGame/thesaurus.json'


def getWords(inputFile):
    with open(inputFile, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        output = []
        for row in reader:
            name = row[0]
            count = int(row[1])
            d = {'name': name, 'count': count}
            output.append(d)

    outputSorted = sorted(
        output[0:10000], key=lambda x: x['count'], reverse=True)

    return outputSorted


wordsArray = getWords(wordsInputPath)

print(wordsArray[-1])
