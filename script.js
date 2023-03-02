import data from './dataset/thesaurus.json' assert { type: 'json' };

const startBtn = document.querySelector('.start-app');
const wordItem = document.getElementById('word-item');
const form = document.getElementById('word-form');
const formInput = document.getElementById('word-input');
const solution = document.getElementById('solution-item');
const submitedWord = document.querySelector('h4');
const solutionMessage = document.querySelector('.solution-message');
const solutionBtn = document.querySelector('.solution-button');
const solutionList = document.querySelector('li');
const listWrapper = document.querySelector('ul');

function show(item) {
  if (item.classList.contains('hidden')) {
    item.classList.remove('hidden');
  }
}

function hide(item) {
  if (!item.classList.contains('hidden')) {
    item.classList.add('hidden');
  }
}
function disableBtn(btn) {
  btn.disabled = true;
}
function load(arr) {
  const randomIndex = Math.floor(Math.random() * arr.length + 1);
  const randomWord = data[randomIndex].word;
  const synonymArray = arr
    .filter((obj) => obj.word === randomWord)
    .map((obj) => obj.synonyms)
    .flat()
    .map((word) => word.toLowerCase());

  const outputWord = {
    word: randomWord,
    synonyms: synonymArray,
  };
  return outputWord;
}

function start() {
  const randomWord = load(data);
  const word = document.querySelector('h2');
  word.textContent = randomWord.word;
  solutionList.textContent = randomWord.synonyms;
  show(wordItem);
  disableBtn(startBtn);
}

function formSubmit(e) {
  e.preventDefault();
  const input = formInput.value;
  if (input.trim() === '') {
    alert('Type a synonym');
    return;
  }
  //compare the value of input with the text content of li
  const array = solutionList.textContent.split(',');
  if (array.includes(input.trim().toLowerCase())) {
    solutionMessage.textContent = 'Correct!';
  } else {
    solutionMessage.textContent = "That word doesn't seem to be a synonym";
  }

  submitedWord.textContent = input;
  show(solution);
}

function toggleSolution() {
  if (solutionBtn.textContent === 'Show solution') {
    show(listWrapper);
    solutionBtn.textContent = 'Hide solution';
  } else {
    hide(listWrapper);
    solutionBtn.textContent = 'Show solution';
  }
}

startBtn.addEventListener('click', start);
form.addEventListener('submit', formSubmit);
solutionBtn.addEventListener('click', toggleSolution);
