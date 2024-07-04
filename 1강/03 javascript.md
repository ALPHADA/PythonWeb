# JavaScript
JavaScript는 웹페이지에 동적인 기능을 추가하는 데 사용되는 프로그래밍 언어입니다.    
기본적인 사용법과 다양한 예제를 통해 JavaScript를 배워봅시다.    

### 기본적인 JavaScript 사용법
JavaScript 코드는 HTML 문서 내의 <script> 태그 안에 작성하거나, 별도의 .js 파일에 작성한 후 HTML에서 불러올 수 있습니다.   

HTML에 직접 JavaScript 작성하기
```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Example</title>
</head>
<body>
    <h1 id="greeting">Hello, World!</h1>
    <button onclick="changeGreeting()">Click me</button>
    <script>
        function changeGreeting() {
            document.getElementById("greeting").innerText = "Hello, JavaScript!";
        }
    </script>
</body>
</html>
```

외부 JavaScript 파일 사용하기
```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Example</title>
    <script src="script.js"></script>
</head>
<body>
    <h1 id="greeting">Hello, World!</h1>
    <button onclick="changeGreeting()">Click me</button>
</body>
</html>
```
```javascript
function changeGreeting() {
    document.getElementById("greeting").innerText = "Hello, JavaScript!";
}
```

### JavaScript 기본 문법

1. 변수 선언

변수는 데이터를 저장하는 공간입니다.    
var, let, const 키워드를 사용해 변수를 선언할 수 있습니다.

```javascript
var name = "Alice";
let age = 25;
const pi = 3.14;
```

2. 데이터 타입

JavaScript 여러 가지 데이터 타입
- 문자열(String)
- 숫자(Number)
- 불리언(Boolean)
- 배열(Array)
- 객체(Object) 등

```javascript
let message = "Hello, World!"; // String
let number = 42; // Number
let isValid = true; // Boolean
let colors = ["red", "green", "blue"]; // Array
let person = {name: "Alice", age: 25}; // Object
```

3. 함수

함수는 반복적으로 사용할 수 있는 코드 블록입니다.

```javascript
function greet(name) {
    return "Hello, " + name + "!";
}

let greeting = greet("Alice");
console.log(greeting); // "Hello, Alice!"
```

4. 조건문

조건문은 특정 조건에 따라 다른 코드를 실행합니다.

```javascript
let age = 18;

if (age >= 18) {
    console.log("You are an adult.");
} else {
    console.log("You are a minor.");
}
```

5. 반복문

반복문은 특정 코드를 여러 번 실행할 때 사용합니다.

```javascript
for (let i = 0; i < 5; i++) {
    console.log("Number: " + i);
}

let colors = ["red", "green", "blue"];
for (let color of colors) {
    console.log(color);
}
```

### JavaScript 예제들

예제 1: 간단한 계산기
```html
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
    <script src="calculator.js"></script>
</head>
<body>
    <h1>Simple Calculator</h1>
    <input type="number" id="num1" placeholder="Enter first number">
    <input type="number" id="num2" placeholder="Enter second number">
    <button onclick="calculate()">Calculate</button>
    <p id="result"></p>
</body>
</html>
```

JavaScript (calculator.js):
```javascript
function calculate() {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let sum = num1 + num2;
    document.getElementById("result").innerText = "Result: " + sum;
}
```

예제 2: 이미지 슬라이더

```html
<!DOCTYPE html>
<html>
<head>
    <title>Image Slider</title>
    <script src="slider.js"></script>
</head>
<body>
    <h1>Image Slider</h1>
    <img id="slider" src="image1.jpg" alt="Image Slider" width="400">
    <button onclick="previousImage()">Previous</button>
    <button onclick="nextImage()">Next</button>
</body>
</html>
```

JavaScript (slider.js):
```javascript
let images = ["image1.jpg", "image2.jpg", "image3.jpg"];
let currentIndex = 0;

function showImage(index) {
    document.getElementById("slider").src = images[index];
}

function previousImage() {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
    showImage(currentIndex);
}

function nextImage() {
    currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
    showImage(currentIndex);
}
```

예제 3: 간단한 투두 리스트

```html
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <script src="todo.js"></script>
</head>
<body>
    <h1>To-Do List</h1>
    <input type="text" id="task" placeholder="Enter a new task">
    <button onclick="addTask()">Add Task</button>
    <ul id="taskList"></ul>
</body>
</html>
```

JavaScript (todo.js):
```javascript
function addTask() {
    let task = document.getElementById("task").value;
    if (task) {
        let taskList = document.getElementById("taskList");
        let listItem = document.createElement("li");
        listItem.innerText = task;
        taskList.appendChild(listItem);
        document.getElementById("task").value = "";
    }
}
```
