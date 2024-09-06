// 02-list.js
// localStorage 에서 할일 목록 불러오기

const userInput = document.querySelector('#userInput')
const myList = document.querySelector('#myList')

const saved = localStorage.getItem('todos')
myList.innerHTML = saved

function addList() {
  const liTag = document.createElement('li')
  liTag.innerText = userInput.value
  myList.appendChild(liTag)
  localStorage.setItem('todos', myList.innerHTML)
  userInput.value = ''
}

userInput.addEventListener('keypress', function(event) {
  if (event.key === 'Enter') {
    addList()
  }
})

// reset function
function resetList() {
  // 화면에서 다 지우고
  myList.innerHTML = ''
  // localStorage 도 초기화
  localStorage.setItem('todos', '')
}