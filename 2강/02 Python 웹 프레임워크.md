# Python 웹 프레임워크
Python을 사용해서 웹페이지를 만들기 위해서는 웹 프레임워크를 사용하는 것이 일반적입니다.     
대표적인 Python 웹 프레임워크로는 Flask와 Django가 있습니다.      
먼저 간단하고 가벼운 Flask를 사용해서 웹페이지를 만드는 방법을 알아봅시다.    

## 이론적인 내용
### 1. 웹 프레임워크란?
웹 프레임워크는 웹 애플리케이션을 개발할 때 필요한 여러 가지 기능과 도구를 제공하는 라이브러리나 프레임워크입니다.        
Flask와 Django는 모두 웹 프레임워크로, 웹 서버와의 상호작용, 템플릿 렌더링, 데이터베이스 처리 등을 쉽게 할 수 있게 해줍니다.     


### 2. Flask란?
Flask는 파이썬으로 작성된 마이크로 웹 프레임워크입니다.      
"마이크로"라는 단어는 Flask가 가벼운 프레임워크라는 것을 의미하며, 필요에 따라 기능을 확장할 수 있습니다.      

Flask는 다음과 같은 특징을 가지고 있어:
- 간단하고 가벼움
- 모듈화와 확장성이 뛰어남
- 라우팅, 템플릿 렌더링, 폼 처리 등의 기능 제공

### 3. Flask의 주요 구성 요소
- 라우팅: URL과 함수를 연결해주는 기능
- 템플릿: HTML 파일에 동적으로 데이터를 삽입할 수 있게 해주는 기능
- 요청 처리: GET, POST 등의 HTTP 요청을 처리하는 기능
- 폼 처리: 사용자의 입력을 받는 기능

## Flask를 사용한 웹 애플리케이션 만들기
### 개발 환경 설정
먼저 Flask를 설치합니다.      
터미널에서 다음 명령어를 실행해서 설치할 수 있습니다:    

```
pip install Flask
```

### Flask 애플리케이션 생성

간단한 "Hello, World!" 웹 애플리케이션을 만들어봅시다.

app.py 파일을 생성하고 다음 코드를 작성하세요.    

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

```

app.run(debug=True)를 사용하면 애플리케이션이 디버그 모드로 실행됩니다.      
이를 통해 코드 변경 시 자동으로 서버를 재시작하고, 에러 메시지를 더 잘 확인할 수 있습니다.

### 웹 애플리케이션 실행

터미널에서 app.py 파일이 있는 디렉토리로 이동한 후 다음 명령어를 실행하세요:
```
python app.py
```

그러면 http://127.0.0.1:5000/에서 "Hello, World!" 메시지를 볼 수 있습니다.

## 간단한 블로그
### 1. 프로젝트 구조
프로젝트 디렉토리를 다음과 같이 구성하세요:
```
my_blog/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css
```

### 2. Flask 애플리케이션 코드 작성
app.py:
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    posts = [
        {
            'author': 'Alice',
            'title': 'First Post',
            'content': 'This is my first post!',
            'date_posted': 'April 20, 2021'
        },
        {
            'author': 'Bob',
            'title': 'Second Post',
            'content': 'This is my second post!',
            'date_posted': 'April 21, 2021'
        }
    ]
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. HTML 템플릿 작성
templates/index.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Blog</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Welcome to My Blog</h1>
    {% for post in posts %}
    <div class="post">
        <h2>{{ post.title }}</h2>
        <p><strong>By {{ post.author }} on {{ post.date_posted }}</strong></p>
        <p>{{ post.content }}</p>
    </div>
    {% endfor %}
</body>
</html>
```

### 4. CSS 스타일 작성
static/style.css:
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    text-align: center;
}
.post {
    background: white;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ccc;
    width: 80%;
    max-width: 600px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```

5. 애플리케이션 실행
터미널에서 app.py 파일이 있는 디렉토리로 이동한 후 다음 명령어를 실행하세요:
```
python app.py
````
이제 http://127.0.0.1:5000/에서 간단한 블로그 웹페이지를 볼 수 있습니다.
