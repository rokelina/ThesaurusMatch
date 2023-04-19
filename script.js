const startBtn = document.getElementById('start-app');
const wordItem = document.getElementById('word-item');
const promptWord = document.getElementById('prompt-word');
const form = document.getElementById('word-form');
const formInput = document.getElementById('word-input');
const solutionContainer = document.getElementById('solution-container');
const submitedWord = document.getElementById('submited-word');
const solutionMessage = document.getElementById('solution-message');
const solutionBtn = document.getElementById('solution-button');
const solutionWrapper = document.getElementById('solution-box');
const solutionList = document.getElementById('solution-list');
const restartBtn = document.getElementById('restart-button');

async function getData() {
  try {
    const res = await fetch('./dataset/thesaurus.json');
    if (!res.ok) {
      throw new Error('Something went wrong');
    }
    const data = await res.json();

    const randomWordObject = getRandomWord(data);
    promptWord.textContent = randomWordObject.word;
    solutionList.textContent = randomWordObject.synonyms;

    show(startBtn);
  } catch (error) {
    showErrorMessage();
    console.error('Something went wrong');
  }
}

function getRandomWord(arr) {
  const randomIndex = Math.floor(Math.random() * arr.length + 1);
  const randomWord = arr[randomIndex].word;
  const allSynonyms = arr
    .filter((obj) => obj.word === randomWord)
    .map((obj) => obj.synonyms)
    .flat()
    .map((word) => word.toLowerCase());

  const synonymArray = [...new Set(allSynonyms)];
  const outputWord = {
    word: randomWord,
    synonyms: synonymArray,
  };

  return outputWord;
}

function onStart() {
  show(wordItem);
  show(promptWord);
  disable(startBtn);
  startBtn.style.opacity = '0';
  startBtn.style.cursor = 'auto';
}

function onSubmit(e) {
  e.preventDefault();
  const input = formInput.value;
  if (input.trim() === '') {
    alert('Type a synonym');
    return;
  }
  //compare the value of input with the text content of li
  const array = solutionList.textContent.split(',');
  if (array.includes(input.trim().toLowerCase())) {
    solutionMessage.textContent = '🟢 Correct!';
  } else {
    solutionMessage.textContent = "🔴 That doesn't seem to be a synonym";
  }

  submitedWord.textContent = input;
  formInput.value = '';
  show(solutionContainer);
  disable(formInput);
}

function onRestart() {
  getData();
  show(promptWord);
  enable(formInput);
  hide(solutionContainer);
  hide(solutionWrapper);
  solutionBtn.textContent = 'Show solution';
}

function toggleSolution() {
  if (solutionBtn.textContent === 'Hide solution') {
    hide(solutionWrapper);
    solutionBtn.textContent = 'Show solution';
  } else {
    show(solutionWrapper);
    solutionList.textContent = solutionList.textContent.split(',').join(', ');
    solutionBtn.textContent = 'Hide solution';
  }
}

function showErrorMessage() {
  const errorMsg = document.createElement('h2');
  errorMsg.textContent = 'Oops... something went wrong';
  errorMsg.style.marginTop = '4rem';
  document.querySelector('header').insertAdjacentElement('afterend', errorMsg);
}

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

function disable(item) {
  item.disabled = true;
}

function enable(item) {
  item.disabled = false;
}

function init() {
  startBtn.addEventListener('click', onStart);
  form.addEventListener('submit', onSubmit);
  solutionBtn.addEventListener('click', toggleSolution);
  restartBtn.addEventListener('click', onRestart);
  document.addEventListener('DOMContentLoaded', getData);
}

init();
