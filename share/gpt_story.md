```
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="@@@"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_story():
    # 사용자가 입력한 주제를 가져옴
    topic = request.form['topic']

    # GPT API 요청을 위한 메시지 설정
    messages = [
        {'role': 'system', 'content': '당신은 창의적인 이야기 작가입니다. 주어진 주제에 따라 이야기를 생성하세요.'},
        {'role': 'user', 'content': f'주제: {topic}'}
    ]

    # GPT API 호출
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    # 응답에서 이야기 추출
    story = response['choices'][0]['message']['content']

    return render_template('result.html', topic=topic, story=story)

if __name__ == '__main__':
    app.run(debug=True)
```

index.html
```
<!DOCTYPE html>
<html>
<head>
    <title>문학 작품 생성기</title>
</head>
<body>
    <h1>문학 작품 생성기</h1>
    <form action="/generate" method="post">
        <label for="topic">주제 입력:</label>
        <input type="text" id="topic" name="topic" required>
        <input type="submit" value="생성">
    </form>
</body>
</html>
```
result.html
```
<!DOCTYPE html>
<html>
<head>
    <title>문학 작품 생성기</title>
</head>
<body>
    <h1>문학 작품 생성기</h1>
    <h2>주제: {{ topic }}</h2>
    <p>{{ story }}</p>
    <a href="/">다시 생성하기</a>
</body>
</html>
```
