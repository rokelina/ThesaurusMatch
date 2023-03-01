import json
import csv

frequentWordsPath = 'dataset/sources/unigram_freq.csv'
filterWords = 'dataset/sources/filterWords.csv'

thesaurusInputPath = 'dataset/sources/en_thesaurus.jsonl'
thesaurusOutputPath = 'dataset/thesaurus.json'


def getFilterArray(inputFile):
    with open(inputFile, 'r') as file:
        reader = csv.reader(file)
        filterArray = [word[0].lower() for word in reader]
    return filterArray


def getFrequentWords(inputFile, filterList):
    with open(inputFile, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        output = [row[0] for row in reader if len(
            row[0]) > 2 and row[0] not in filterList]
        words = output[0:5000]

    return words


def filterThesaurus(inputFile, frequentList):
    output = []
    with open(inputFile, 'r') as file:
        for line in file:
            obj = json.loads(line)
            # if x['word'] in frequentlList and x['synonyms'] != []
            if obj['word'].lower() in frequentList and obj['synonyms'] != []:
                newObj = {
                    'word': obj['word'].lower(), 'pos': obj['pos'], 'synonyms': obj['synonyms']}
                output.append(newObj)
        # sort words and dump them to a json file
        sortedOutput = sorted(output, key=lambda x: x['word'])
    return sortedOutput


def outputThesaurus(inputArray, filterArray, outputFile):
    output = []
    # another iteration to check for "inappropiate" synonyms
    for obj in inputArray:
        filtered = []
        for synonym in obj['synonyms']:
            if synonym.lower() not in filterArray:
                filtered.append(synonym)
        new_object = {'word': obj['word'].lower(
        ), 'pos': obj['pos'], 'synonyms': filtered}
        if new_object['synonyms'] != []:
            output.append(new_object)

    with open(outputFile, 'w') as file:
        json.dump(output, file)
    return output


filter_words = getFilterArray(filterWords)
frequent_words = getFrequentWords(frequentWordsPath, filter_words)
filtered_thesaurus = filterThesaurus(thesaurusInputPath, frequent_words)
final_output = outputThesaurus(
    filtered_thesaurus, filter_words, thesaurusOutputPath)
