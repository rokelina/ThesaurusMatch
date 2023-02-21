import data from './dataset/thesaurus.json' assert { type: 'json' };

function load(arr) {
  //generate a random index
  const randomIndex = Math.floor(Math.random() * arr.length + 1);
  //get the object located at that index in data and store the value of 'word'
  const randomWord = data[randomIndex].word;
  //get all the synonyms available for that word
  let synonymArray = [];
  //look at the whole array and find all the synonyms for randomWord
  arr.forEach((obj) => {
    if (obj.word === randomWord) {
      synonymArray.push(obj.synonyms);
    }
  });
  const outputWord = {
    word: randomWord,
    synonyms: synonymArray.flat(),
  };
  return outputWord;
}

function play(outputWord) {
  //takes the object returned by load()
  //generates a prompt object that displays the object.word value
  let inputSynonym = prompt(`What's a synonym for "${outputWord.word}"?`);

  //checks if input is a valid synonym
  if (outputWord.synonyms.includes(inputSynonym.trim().toLowerCase())) {
    alert('Correct!');
  } else {
    alert("That word doesn't seem to be a synonym");
  }
}

const word = load(data);
play(word);
