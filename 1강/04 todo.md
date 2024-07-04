# TODO 리스트 만들기

간단한 투두 리스트(To-Do List) 웹 애플리케이션을 단계별로 만들어봅시다.    
HTML, CSS, JavaScript를 사용해서 구현합니다.

### 1단계: 기본 HTML 구조 만들기
먼저, 투두 리스트의 기본 HTML 구조를 만들어 봅시다.    
텍스트 입력 필드, 추가 버튼, 그리고 할 일 목록을 위한 <ul> 요소를 포함합니다.   

```html
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    <input type="text" id="taskInput" placeholder="Enter a new task">
    <button onclick="addTask()">Add Task</button>
    <ul id="taskList"></ul>
</body>
</html>
```

### 2단계: CSS로 스타일 추가하기
투두 리스트를 좀 더 보기 좋게 스타일링하기 위해 CSS를 추가합니다.

```html
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f2f2f2;
        }
        h1 {
            margin-top: 50px;
        }
        input {
            margin: 10px 0;
            padding: 10px;
            width: 200px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            border: none;
            background-color: #28a745;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background-color: white;
            margin: 5px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 200px;
        }
        .deleteButton {
            background-color: #dc3545;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            padding: 5px;
        }
        .deleteButton:hover {
            background-color: #c82333;
        }
    </style>
</head>
<body>
    <h1>To-Do List</h1>
    <input type="text" id="taskInput" placeholder="Enter a new task">
    <button onclick="addTask()">Add Task</button>
    <ul id="taskList"></ul>
</body>
</html>
```

### 3단계: JavaScript로 기능 추가하기
이제 JavaScript를 사용해서 할 일을 추가하고 삭제하는 기능을 구현합니다.

#### 1. JavaScript 파일 추가하기
HTML 파일에 JavaScript 파일을 추가합니다.    
`<script>` 태그를 사용해서 `todo.js` 파일을 불러옵니다.

```html
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <style>
        /* 위의 CSS 코드 추가 */
    </style>
</head>
<body>
    <h1>To-Do List</h1>
    <input type="text" id="taskInput" placeholder="Enter a new task">
    <button onclick="addTask()">Add Task</button>
    <ul id="taskList"></ul>
    <script src="todo.js"></script>
</body>
</html>
```

#### 2. todo.js 파일 내용 추가하기
이제 JavaScript 파일에서 할 일 추가 기능을 구현해봅시다.

```javascript
// todo.js

// 할 일을 추가하는 함수
function addTask() {
    // 입력 필드와 할 일 목록 요소를 가져오기
    let taskInput = document.getElementById("taskInput");
    let taskList = document.getElementById("taskList");

    // 입력 필드의 값을 가져오기
    let taskText = taskInput.value;

    // 입력 필드가 비어있으면 아무것도 하지 않음
    if (taskText === "") {
        return;
    }

    // 새로운 할 일 항목을 만들기
    let listItem = document.createElement("li");

    // 할 일 텍스트를 추가
    listItem.innerText = taskText;

    // 삭제 버튼을 만들기
    let deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete";
    deleteButton.className = "deleteButton";
    deleteButton.onclick = function() {
        taskList.removeChild(listItem);
    };

    // 할 일 항목에 삭제 버튼 추가
    listItem.appendChild(deleteButton);

    // 할 일 목록에 새로운 항목 추가
    taskList.appendChild(listItem);

    // 입력 필드 초기화
    taskInput.value = "";
}
```

### 4단계: 완성된 코드
이제 모든 파일을 완성된 상태로 확인해봅시다.

HTML 파일 (index.html):
```html
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f2f2f2;
        }
        h1 {
            margin-top: 50px;
        }
        input {
            margin: 10px 0;
            padding: 10px;
            width: 200px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            border: none;
            background-color: #28a745;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background-color: white;
            margin: 5px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 200px;
        }
        .deleteButton {
            background-color: #dc3545;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            padding: 5px;
        }
        .deleteButton:hover {
            background-color: #c82333;
        }
    </style>
</head>
<body>
    <h1>To-Do List</h1>
    <input type="text" id="taskInput" placeholder="Enter a new task">
    <button onclick="addTask()">Add Task</button>
    <ul id="taskList"></ul>
    <script src="todo.js"></script>
</body>
</html>
```

JavaScript 파일 (todo.js):
```javascript
// 할 일을 추가하는 함수
function addTask() {
    // 입력 필드와 할 일 목록 요소를 가져오기
    let taskInput = document.getElementById("taskInput");
    let taskList = document.getElementById("taskList");

    // 입력 필드의 값을 가져오기
    let taskText = taskInput.value;

    // 입력 필드가 비어있으면 아무것도 하지 않음
    if (taskText === "") {
        return;
    }

    // 새로운 할 일 항목을 만들기
    let listItem = document.createElement("li");

    // 할 일 텍스트를 추가
    listItem.innerText = taskText;

    // 삭제 버튼을 만들기
    let deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete";
    deleteButton.className = "deleteButton";
    deleteButton.onclick = function() {
        taskList.removeChild(listItem);
    };

    // 할 일 항목에 삭제 버튼 추가
    listItem.appendChild(deleteButton);

    // 할 일 목록에 새로운 항목 추가
    taskList.appendChild(listItem);

    // 입력 필드 초기화
    taskInput.value = "";
}
```

이제 브라우저에서 index.html 파일을 열어보면 작동하는 투두 리스트를 확인할 수 있습니다.      
할 일을 추가하고 삭제해보면서 JavaScript의 기능을 경험해봅시다.     
필요하다고 생각되는 기능을 더 추가해도 좋습니다!

