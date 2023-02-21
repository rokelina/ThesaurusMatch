import data from './dataset/thesaurus.json' assert { type: 'json' };
console.log(data);

//on program start load data into memory, return an object with a
//random word as a property and an array of all synonyms as the value

function load() {
  //generate a random index
  let randomIndex;
  //get the word object located at that index in data
  let randomWord;
  //get all the synonyms available for that word
  let synonymArray;

  return (outputWord = {
    randomWord: synonymArray,
  });
}

function play(outputWord) {
  //takes the object returned by load()
  //generates a prompt object that displays the word propery

  let inputSynonym = prompt(`What's a synonym for ${outputWord.key}?`);

  //user input. on click "ok" will compare input with outputWord and alert('message')
  if (outputWord.values.includes(inputSynonym.toLowerCase())) {
    alert('Correct!');
  } else {
    alert("That word doesn't seem to be a synonym");
  }
}
