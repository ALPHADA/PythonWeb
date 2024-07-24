### ChatGPT
ChatGPT API를 활용하여 웹사이트를 제작해봅시다.      
이 애플리케이션은 사용자가 입력한 질문에 대해 ChatGPT API를 통해 답변을 제공하는 기능을 갖추게 됩니다.

#### OpenAI API Key 설정
먼저, OpenAI API 키가 필요합니다.     
[OpenAI](https://platform.openai.com/signup/)에서 계정을 생성하고 API 키를 발급받으세요.

#### 프로젝트 구조 설정
프로젝트 디렉토리 구조는 다음과 같습니다:

```arduino
코드 복사
chatgpt_web/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
```

#### Flask 애플리케이션 설정

app.py

```python
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = 'YOUR_OPENAI_API_KEY'  # 여기 YOUR_OPENAI_API_KEY 부분에 실제 API 키를 입력하세요.

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
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

#### HTML 템플릿 작성
templates/index.html

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

#### JavaScript 파일 작성
static/script.js

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

#### 스타일시트 작성
static/style.css

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

#### 실행
이제 애플리케이션을 실행합니다.

```bash
python app.py
```

브라우저에서 http://127.0.0.1:5000/로 접속하면 ChatGPT 웹 애플리케이션이 실행되고, 사용자가 입력한 질문에 대해 ChatGPT API를 통해 답변을 제공하는 기능을 사용할 수 있습니다.
