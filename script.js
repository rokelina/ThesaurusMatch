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

async function getData() {
  try {
    const res = await fetch('./dataset/thesaurus.json');
    if (!res.ok) {
      throw new Error('Something went wrong');
    }
    const data = await res.json();

    //call getRandomWord on data
    const randomWordObject = getRandomWord(data);
    promptWord.textContent = randomWordObject.word;

    // Create a label element for each element in the synonyms array
    randomWordObject.synonyms.forEach((synonym) => {
      const li = document.createElement('li');
      li.textContent = synonym;
      solutionList.appendChild(li);
    });

    show(startBtn);
  } catch (error) {
    showErrorMessage();
    console.error('Something went wrong');
  }
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

  const array = Array.from(document.querySelectorAll('li')).map(
    (li) => li.textContent
  );

  if (array.includes(input.trim().toLowerCase())) {
    solutionMessage.innerHTML = `<span style="color:green" aria-label="Correct">🟢</span> Correct!`;
  } else {
    solutionMessage.innerHTML = `<span style="color:red" aria-label="Not a synonym">🔴</span> That doesn't seem to be a synonym`;
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
  document.querySelectorAll('li').forEach((li) => li.remove());
}

function toggleSolution() {
  if (solutionBtn.textContent === 'Hide solution') {
    hide(solutionWrapper);
    solutionBtn.textContent = 'Show solution';
  } else {
    show(solutionWrapper);
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
