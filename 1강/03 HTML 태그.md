# HTML 태그

#### 표기법

`<START TAG>` CONTENT `</END TAG>`

#### 예시

|START TAG	| CONTENT	| END TAG|
|------|------|------|
|`<h1>`	|제목	|`</h1>`|
|`<p>`	|문단	|`</p>`|
|`<br>`	|none	|none|

위의 표에서 `<br>` tag처럼 간혹 몇개의 태그들은 CONTENT를 가지지 않는다. 이를 empty tag라고 한다.
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


