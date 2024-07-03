# CSS
CSS(Cascading Style Sheets)는 웹페이지의 스타일(디자인)을 정의하는 언어입니다.      
CSS를 사용하면 HTML 요소의 색상, 폰트, 레이아웃 등을 설정할 수 있습니다.    
기본적인 CSS 사용법과 다양한 예제를 통해 CSS를 배워봅시다.


### 기본적인 CSS 문법
CSS는 선택자(selector)와 선언(declaration)으로 구성됩니다.    
선택자는 스타일을 적용할 HTML 요소를 지정하고, 선언은 그 요소에 적용할 스타일을 정의합니다.   

```css
selector {
    property: value;
}
```

### CSS 적용 방법
인라인 스타일(In-line style): HTML 태그에 직접 스타일을 지정.

```css
<p style="color: blue;">This is a blue paragraph.</p>
```

내부 스타일 시트(Internal style sheet): HTML 문서의 <head> 안에 <style> 태그를 사용해 스타일을 지정.

```css
<head>
    <style>
        p {
            color: blue;
        }
    </style>
</head>
```

외부 스타일 시트(External style sheet): 별도의 CSS 파일을 만들어 HTML 문서에 링크.

```css
<!-- HTML 문서 -->
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<!-- styles.css 파일 -->
p {
    color: blue;
}
```

### 주요 CSS 속성
1. 색상 (Color)

텍스트 색상: color
```css
p {
    color: red;
}
```

배경 색상: background-color
```css
body {
    background-color: lightgray;
}

2. 글꼴 (Font)

글꼴 종류: font-family
```css
p {
    font-family: Arial, sans-serif;
}
```

글꼴 크기: font-size
```css
p {
    font-size: 16px;
}
```

글꼴 굵기: font-weight
```css
p {
    font-weight: bold;
}
```

3. 텍스트 정렬 (Text Alignment)

텍스트 정렬: text-align
```css
h1 {
    text-align: center;
}
```

4. 여백 (Margin and Padding)

바깥 여백: margin
```css
p {
    margin: 20px;
}
```

안쪽 여백: padding
```css
div {
    padding: 10px;
}
```

5. 테두리 (Border)

테두리 스타일: border
```css
p {
    border: 1px solid black;
}
```

6. 크기 (Width and Height)

넓이: width
```css
div {
    width: 50%;
}
```

높이: height
```css
div {
    height: 100px;
}
```

### css 예제

예제 1: 기본 스타일 적용
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: lightblue;
        }
        h1 {
            color: navy;
            text-align: center;
        }
        p {
            font-family: verdana;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a styled paragraph.</p>
</body>
</html>
```

예제 2: 클래스와 아이디 선택자
HTML 문서:
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <h1 class="title">Hello, World!</h1>
    <p id="intro">This is a styled paragraph with an ID.</p>
    <p class="content">This is another styled paragraph with a class.</p>
</body>
</html>
```

styles.css 파일:
```css
.title {
    color: navy;
    text-align: center;
}
#intro {
    font-family: verdana;
    font-size: 20px;
}
.content {
    font-family: arial;
    font-size: 18px;
}
```

예제 3: 레이아웃 만들기
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            width: 100%;
            border: 1px solid black;
        }
        .header, .footer {
            background-color: lightgray;
            padding: 10px;
            text-align: center;
        }
        .content {
            padding: 20px;
        }
        .column {
            float: left;
            width: 50%;
        }
        .row::after {
            content: "";
            clear: both;
            display: table;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>My Website</h1>
        </div>
        <div class="content">
            <div class="row">
                <div class="column" style="background-color:lightblue;">
                    <h2>Column 1</h2>
                    <p>Some text..</p>
                </div>
                <div class="column" style="background-color:lightgreen;">
                    <h2>Column 2</h2>
                    <p>Some text..</p>
                </div>
            </div>
        </div>
        <div class="footer">
            <p>Footer</p>
        </div>
    </div>
</body>
</html>
```
