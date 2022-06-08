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


