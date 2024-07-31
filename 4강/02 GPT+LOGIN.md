# 문학 작품 생성기

사용자는 생성된 이야기를 저장하고, 조회하며, 수정하고, 삭제할 수 있습니다.     
이러한 기능을 구현하기 위해 간단한 데이터베이스와 사용자 인증 기능을 추가합니다.    
문학 작품 생성기는 사용자가 입력한 주제 또는 키워드를 바탕으로 GPT 모델을 활용해 짧은 이야기, 시, 또는 에세이를 생성하는 웹 애플리케이션입니다.      
사용자는 입력한 내용과 관련된 이야기를 웹 페이지에서 바로 볼 수 있습니다.

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

### 발전된 기능
- 장르 선택: 사용자가 생성할 이야기의 장르를 선택할 수 있게 합니다. 예: 판타지, 공포, 로맨스 등.
- 이야기 길이 조절: 사용자가 이야기의 길이(짧은 이야기, 중간 이야기, 긴 이야기)를 선택할 수 있게 합니다.
- 캐릭터 추가: 사용자 정의 캐릭터를 추가하여 이야기에서 등장시킬 수 있게 합니다.
- 다양한 형식 지원: 이야기 외에도 시, 수필 등의 형식 선택 가능.
- 이야기 저장 및 공유: 생성된 이야기를 PDF로 저장하거나 소셜 미디어에서 공유할 수 있게 합니다.

app.py
```python
from flask import Flask, render_template, request, send_file
from openai import OpenAI
import os
from fpdf import FPDF

app = Flask(__name__)

client = OpenAI(
    api_key="@@@"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_story():
    # 사용자 입력 정보 가져오기
    topic = request.form['topic']
    genre = request.form['genre']
    length = request.form['length']
    character = request.form.get('character', '')

    # GPT API 요청을 위한 메시지 설정
    system_message = f"당신은 창의적인 이야기 작가입니다. 주어진 장르와 길이에 맞춰 이야기를 생성하세요. 장르: {genre}, 길이: {length}."
    user_message = f"주제: {topic}, 캐릭터: {character}"

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': user_message}
    ]

    # GPT API 호출
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    # 응답에서 이야기 추출
    story = response['choices'][0]['message']['content']

    # 이야기 저장을 위한 세션 변수 설정
    session['story'] = story

    return render_template('result.html', topic=topic, story=story)

@app.route('/download')
def download_story():
    story = session.get('story', '')

    # PDF 생성
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, story)

    pdf_path = os.path.join("static", "story.pdf")
    pdf.output(pdf_path)

    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
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
    <a href="/download">이야기 다운로드 (PDF)</a>
    <a href="/">다시 생성하기</a>
</body>
</html>
```

### login
app.py
```python
# pip install -U Flask-SQLAlchemy
# pip install fpdf
import os
from flask import Flask, render_template, request, redirect, send_file, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Story
from openai import OpenAI
from fpdf import FPDF

client = OpenAI(
    api_key="@@@"
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stories.db'
app.config['SECRET_KEY'] = 'your_secret_key2'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/generate', methods=['POST'])
def generate_story():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # 사용자 입력 정보 가져오기
    topic = request.form['topic']
    genre = request.form['genre']
    length = request.form['length']
    character = request.form.get('character', '')

    # GPT API 요청
    messages = [
        {'role': 'system', 'content': f"당신은 창의적인 이야기 작가입니다. 장르: {genre}, 길이: {length}."},
        {'role': 'user', 'content': f"주제: {topic}, 캐릭터: {character}"}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", #"gpt-4o-mini",
        messages=messages
    )
    story_content = response.choices[0].message.content

    # 이야기 저장
    new_story = Story(title=topic, content=story_content, user_id=session['user_id'])
    db.session.add(new_story)
    db.session.commit()

    return redirect(url_for('dashboard'))

@app.route('/download')
def download_story():
    story = session.get('story', '')

    # PDF 생성
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, story)

    pdf_path = os.path.join("static", "story.pdf")
    pdf.output(pdf_path)

    return send_file(pdf_path, as_attachment=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    stories = Story.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', stories=stories)

@app.route('/story/<int:id>')
def view_story(id):
    story = Story.query.get_or_404(id)
    return render_template('view_story.html', story=story)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_story(id):
    story = Story.query.get_or_404(id)

    if request.method == 'POST':
        story.title = request.form['title']
        story.content = request.form['content']
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('edit_story.html', story=story)

@app.route('/delete/<int:id>')
def delete_story(id):
    story = Story.query.get_or_404(id)
    db.session.delete(story)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
```

models.py
```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    stories = db.relationship('Story', backref='author', lazy=True)

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

index.html
```
<!DOCTYPE html>
<html>
<head>
    <title>문학 작품 생성기</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>문학 작품 생성기</h1>
    <form action="/generate" method="post">
        <label for="topic">주제 입력:</label>
        <input type="text" id="topic" name="topic" required><br>

        <label for="genre">장르 선택:</label>
        <select id="genre" name="genre">
            <option value="Fantasy">판타지</option>
            <option value="Horror">공포</option>
            <option value="Romance">로맨스</option>
            <option value="Adventure">모험</option>
        </select><br>

        <label for="length">이야기 길이:</label>
        <select id="length" name="length">
            <option value="Short">짧은 이야기</option>
            <option value="Medium">중간 이야기</option>
            <option value="Long">긴 이야기</option>
        </select><br>

        <label for="character">캐릭터 이름 (선택 사항):</label>
        <input type="text" id="character" name="character"><br>

        <input type="submit" value="생성">
    </form>
</body>
</html>

```

login.html
```
<!DOCTYPE html>
<html>
<head>
    <title>로그인</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('home') }}">홈</a>
        <a href="{{ url_for('register') }}">회원가입</a>
    </nav>
    <div class="container">
        <h1>로그인</h1>
        <form action="{{ url_for('login') }}" method="post">
            <label for="username">아이디:</label>
            <input type="text" id="username" name="username" required>

            <label for="password">비밀번호:</label>
            <input type="password" id="password" name="password" required>

            <input type="submit" value="로그인">
        </form>
        {% if error %}
            <p style="color:red;">{{ error }}</p>
        {% endif %}
        <p>계정이 없으신가요? <a href="{{ url_for('register') }}">회원가입</a></p>
    </div>
    <footer>
        <p>&copy; 2024 문학 작품 생성기</p>
    </footer>
</body>
</html>
```
register.html
```
<!DOCTYPE html>
<html>
<head>
    <title>회원가입</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>회원가입</h1>
    <form action="/register" method="post">
        <label for="username">아이디:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">비밀번호:</label>
        <input type="password" id="password" name="password" required><br>
        <input type="submit" value="가입">
    </form>
</body>
</html>

```
dashboard.html
```
<!DOCTYPE html>
<html>
<head>
    <title>내 이야기</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>내 이야기</h1>
    <a href="/logout">로그아웃</a>
    <ul>
        {% for story in stories %}
            <li>
                <a href="{{ url_for('view_story', id=story.id) }}">{{ story.title }}</a>
                <a href="{{ url_for('edit_story', id=story.id) }}">편집</a>
                <a href="{{ url_for('delete_story', id=story.id) }}">삭제</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>

```
result.html
```
<!DOCTYPE html>
<html>
<head>
    <title>문학 작품 생성기</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>문학 작품 생성기</h1>
    <h2>주제: {{ topic }}</h2>
    <p>{{ story }}</p>
    <a href="/download">이야기 다운로드 (PDF)</a>
    <a href="/">다시 생성하기</a>
</body>
</html>

```
view_story.html
```
<!DOCTYPE html>
<html>
<head>
    <title>{{ story.title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>{{ story.title }}</h1>
    <p>{{ story.content }}</p>
    <a href="{{ url_for('dashboard') }}">뒤로 가기</a>
</body>
</html>

```

styles.css
```
/* 기본 스타일 */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

h1, h2 {
    color: #333;
    text-align: center;
}

a {
    color: #337ab7;
    text-decoration: none;
}

a:hover {
    color: #23527c;
    text-decoration: underline;
}

/* 네비게이션 스타일 */
nav {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    text-align: center;
}

nav a {
    color: #fff;
    margin: 0 15px;
    font-weight: bold;
}

nav a:hover {
    color: #d4d4d4;
}

/* 컨테이너 */
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    margin-top: 30px;
}

/* 폼 스타일 */
form label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

form input[type="text"],
form input[type="password"],
form select,
form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
}

form input[type="submit"] {
    background-color: #5cb85c;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

form input[type="submit"]:hover {
    background-color: #4cae4c;
}

/* 버튼 스타일 */
.button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #5bc0de;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: #31b0d5;
}

/* 스토리 리스트 */
.story-list ul {
    list-style-type: none;
    padding: 0;
}

.story-list li {
    background-color: #f9f9f9;
    margin: 5px 0;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.story-list li a {
    color: #337ab7;
}

.story-list li a:hover {
    text-decoration: underline;
}

/* 푸터 스타일 */
footer {
    background-color: #333;
    color: #fff;
    padding: 10px;
    text-align: center;
    position: fixed;
    bottom: 0;
    width: 100%;
}

```
