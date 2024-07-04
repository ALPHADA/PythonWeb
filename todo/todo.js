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
