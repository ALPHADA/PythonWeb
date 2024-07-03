# HTML
HTML은 웹페이지의 구조를 정의하는 언어입니다.     
HTML은 요소(tag)로 구성되며, 이 요소들은 태그(<>)로 감싸여 있습니다.      
기본적인 HTML 구조와 다양한 예제를 통해 HTML을 배워봅시다.    

### 기본 HTML 문서 구조
HTML 문서는 보통 다음과 같은 기본 구조를 가지고 있습니다.


```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Webpage</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is my first webpage.</p>
</body>
</html>

```

### 주요 HTML 태그들
1. 제목 태그 (`<h1>` ~ `<h6>`)
제목을 표시하는 태그로, `<h1>`이 가장 큰 제목이고 `<h6>`이 가장 작은 제목입니다.

```html

<h1>Title 1</h1>
<h2>Title 2</h2>
<h3>Title 3</h3>
<h4>Title 4</h4>
<h5>Title 5</h5>
<h6>Title 6</h6>
```

2. 단락 태그 (`<p>`)
텍스트 단락을 표시하는 태그입니다.
```html
<p>This is a paragraph.</p>
<p>Another paragraph.</p>
```

3. 링크 태그 (`<a>`)
다른 페이지나 URL로 연결하는 하이퍼링크를 생성하는 태그입니다.
```html
<a href="https://www.example.com">Visit Example.com</a>
```

4. 이미지 태그 (`<img>`)
이미지를 삽입하는 태그입니다. src 속성을 사용해 이미지 파일의 경로를 지정합니다.

```html
<img src="path/to/image.jpg" alt="Description of Image">
```

5. 목록 태그
순서가 없는 목록 (`<ul>` 와 `<li>`)

```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

순서가 있는 목록 (`<ol>` 와 `<li>`)
```html
<ol>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>
```

6. 테이블 태그 (`<table>`, `<tr>`, `<td>`, `<th>`)
표를 만드는 태그입니다.
```html
<table>
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>Data 1</td>
        <td>Data 2</td>
    </tr>
    <tr>
        <td>Data 3</td>
        <td>Data 4</td>
    </tr>
</table>
```

7. 폼 태그 (`<form>`, `<input>`, `<button>`, `<textarea>`)
사용자 입력을 받는 폼을 만드는 태그입니다.
```html
<form action="/submit" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    <br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
    <br>
    <button type="submit">Submit</button>
</form>
```

# HTML 태그

#### 표기법

`<START TAG>` CONTENT `</END TAG>`

#### 예시

|START TAG	| CONTENT	| END TAG|
|------|------|------|
|`<h1>`	|제목	|`</h1>`|
|`<p>`	|문단	|`</p>`|
|`<br>`	|none	|none|

위의 표에서 `<br>` tag처럼 간혹 몇개의 태그들은 CONTENT를 가지지 않는다.     
이를 empty tag라고 한다.     
또한, 이러한 empty tag는 END TAG를 가지지 않고 START TAG만 표기해준다.

#### 중첩 TAG
중첩 : 겹치거나 포개어짐

```
<!DOCTYPE HTML>
<html>
<head>
<title>중첩 TAG</title>
<meta charset="UTF-8">
</head>
<body>
<h1>제목입니다.</h1>
<p>문단입니다</p>
</body>
</html>
```
- `<html>` tag는 `<head>` tag 와 `<body>` tag 를 중첩.
- `<head>` tag는 `<title>` tag 와 `<meta>` tag 중첩
- `<body>` tag는 `<h1>` tag와 `<p>` tag 중첩.

#### 잘못된 예시

```
<!DOCTYPE HTML>
<html>
<head>
<title>중첩 TAG</title>
<meta charset="UTF-8">
</head>
<body>
<h1>제목입니다.
```
`<p></h1>`

```
1 문단입니다 
</p>
</body>
</html>
```
`<END TAG>`가 오기전에 새로운 `<START TAG>`가 올 수 없다.

### TAG를 다 외워야 하나요?

 HTML은
약 150개가 넘는 태그가 존재합니다.

 

 

그럼 그 많은 태그를 다 외워야 할까요?

https://www.advancedwebranking.com/seo/html-study/


아래 그래프는
전 세계에 있는 웹페이지들이
몇 종류의 태그로 이루어져 있는지를 보여주고 있습니다.

아래 그래프는 태그별 인기도입니다.     

![스크린샷 2022-06-08 오후 1 50 30](https://user-images.githubusercontent.com/48852104/172534208-f341aa74-e4a3-4bc0-85e8-e72ec381de18.png)

우리는 모두 외우는 것이 아니라 어떤 태그를 사용할지 검색을 하여 선택할 수 있습니다.       
검색을 두려워하지 맙시다.    

