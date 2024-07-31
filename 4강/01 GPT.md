# ChatGPT API
#### API란 무엇인가?
API는 Application Programming Interface의 약자로, 소프트웨어 애플리케이션 간의 상호 작용을 정의하는 규칙과 도구의 집합입니다.     
API를 사용하면 특정 소프트웨어 기능을 호출하여 사용할 수 있습니다.

#### OpenAI API 소개
OpenAI API는 GPT-3, GPT-4와 같은 AI 모델에 접근할 수 있는 API입니다.      
이 API를 사용하면 자연어 처리 기능을 손쉽게 구현할 수 있습니다.     
ChatGPT API는 OpenAI의 언어 모델을 사용하여 채팅 응답을 생성하는 기능을 제공합니다.

#### API 키 발급
OpenAI API를 사용하기 위해서는 API 키가 필요합니다. API 키는 OpenAI 웹사이트에서 발급받을 수 있습니다.

OpenAI 홈페이지에 접속하여 계정을 만듭니다.
로그인 후, OpenAI Dashboard에서 API 키를 발급받습니다.

[OpenAI](https://platform.openai.com/signup/)에서 계정을 생성하고 API 키를 발급받으세요.

#### API 호출 방법
OpenAI API를 호출하기 위해서는 HTTP 요청을 사용합니다.     
Python에서는 requests 라이브러리를 사용하여 API를 호출할 수 있습니다.

```
사전 준비
Python 설치: Python 공식 웹사이트에서 Python을 다운로드하고 설치합니다.
requests 라이브러리 설치: 터미널(또는 명령 프롬프트)을 열고 다음 명령어를 입력하여 requests 라이브러리를 설치합니다.
```
```sh
pip install requests
```


#### OpenAI API 사용 예제
1. API 키 설정
- 발급받은 API 키를 코드에 설정합니다.

```python
import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'
```

2. API 호출 예제
- 다음은 OpenAI API를 사용하여 ChatGPT 모델을 호출하는 예제입니다.

```python
from openai import OpenAI
client = OpenAI(
    api_key="@@@"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are my english teacher."},
    {"role": "user", "content": "Hello, how are you?"}
  ]
)

print(completion.choices[0].message)
```

#### Flask를 사용한 간단한 웹 애플리케이션 예제


프로젝트 구조
```arduino
chatgpt_web/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
app.py
```
```python
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(
    api_key="@@@"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    try:

        response = client.chat.completions.create(
            model="gpt-3.5-turbo", #"gpt-4o-mini",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        print(answer)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChatGPT Web</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>ChatGPT Web</h1>
        <div id="chat-box">
            <div id="messages"></div>
        </div>
        <form id="chat-form">
            <input type="text" id="user-input" placeholder="Ask me anything..." required>
            <button type="submit">Send</button>
        </form>
    </div>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
```
script.js
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('chat-form');
    const input = document.getElementById('user-input');
    const messages = document.getElementById('messages');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const question = input.value;
        addMessage('You', question);
        input.value = '';

        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: question })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                addMessage('Error', data.error);
            } else {
                addMessage('ChatGPT', data.answer);
            }
        })
        .catch(error => {
            addMessage('Error', 'An error occurred: ' + error.message);
        });
    });

    function addMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
        messages.appendChild(messageElement);
        messages.scrollTop = messages.scrollHeight;
    }
});
```
style.css
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 400px;
}

h1 {
    margin-top: 0;
}

#chat-box {
    border: 1px solid #ccc;
    padding: 10px;
    height: 300px;
    overflow-y: auto;
    margin-bottom: 10px;
}

.message {
    margin-bottom: 10px;
}

#chat-form {
    display: flex;
}

#user-input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px 0 0 5px;
}

#chat-form button {
    padding: 10px;
    border: none;
    background-color: #28a745;
    color: white;
    cursor: pointer;
    border-radius: 0 5px 5px 0;
}

#chat-form button:hover {
    background-color: #218838;
}
```
