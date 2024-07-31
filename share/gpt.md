-proj-418yuqNf2J1kqvnnFIimT3BlbkFJSSTeZ7wSSRZmxv33kU4m

```
# pip3 install flask
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
client = OpenAI(
    api_key="@@@"
)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/color')
def color():
  return render_template('color.html')


@app.route('/gpt', methods=['GET', 'POST'])
def gpt():
  user_input = request.args.get(
    'user_input') if request.method == 'GET' else request.form['user_input']
  print(user_input)
  messages = [{"role": "user", "content": user_input}]

  try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", #"gpt-4o-mini",
        messages=messages
    )
    print(response.choices[0])
    content = response.choices[0].message.content
  except :
    content = "The server is experiencing a high volume of requests. Please try again later."

  return jsonify(content=content)


@app.route('/gpt_color', methods=['GET', 'POST'])
def gpt_color():
  user_input = request.args.get(
    'user_input') if request.method == 'GET' else request.form['user_input']
  print(user_input)
  messages = [
    {
        'role': 'system',
        "content": "사용자의 요청에 따라 색상 코드를 추천해주세요. 응답 형식은 다음과 같은 JSON 형식이어야 합니다: {\"reasonForRecommendation\":\"...\", \"colorlist\":[\"#123456\", \"#654321\", ...]}. 'reasonForRecommendation'은 한국어로 작성해주세요."
    },
    {
        'role': 'user',
        "content": 'DESC::맛있는 딸기'
    },
    {
        'role': 'assistant',
        "content": '{"reasonForRecommendation":"딸기의 상큼하고 달콤한 맛을 나타내기 위해 밝은 빨간색과 분홍색을 추천합니다.","colorlist":["#FF6384","#FF99A5","#FF5678","#FF8699","#FFB3C6"]}'
    },
    {
        'role': 'user',
        "content": 'DESC::우거진 숲속의 소나무'
    },
    {
        'role': 'assistant',
        "content": '{"reasonForRecommendation":"푸르른 소나무와 숲의 신선함을 표현하기 위해 짙은 초록색을 추천합니다.","colorlist":["#228B22","#006400","#2E8B57","#3CB371","#556B2F"]}'
    },
    {
        'role': 'user',
        "content": 'DESC::드넓은 사막의 모래'
    },
    {
        'role': 'assistant',
        "content": '{"reasonForRecommendation":"사막의 넓고 황량한 풍경을 나타내기 위해 따뜻한 모래색과 갈색을 추천합니다.","colorlist":["#C2B280","#D2B48C","#DEB887","#F4A460","#BC8F8F"]}'
    },
    {
        'role': 'user',
        "content": user_input
    }
    ]

  try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", #"gpt-4o-mini",
        messages=messages
    )
    print(response)
    content = response.choices[0].message.content
  except :
    content = "The server is experiencing a high volume of requests. Please try again later."

  return jsonify(content=content)


if __name__ == '__main__':
  app.run(debug=True)

```
index.html
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>GPT-3 Whale Coding</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
      }

      .chat-container {
        background-color: #ffffff;
        border-radius: 5px;
        padding: 20px;
        width: 80%;
        max-width: 600px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
      }

      h1 {
        text-align: center;
        margin-bottom: 20px;
      }

      #chat-form {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
      }

      #user-input {
        flex-grow: 1;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
      }

      #submitBtn {
        background-color: #4caf50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 15px;
        margin-left: 10px;
        cursor: pointer;
      }

      #submitBtn:hover {
        background-color: #45a049;
      }

      #result {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 20px;
        background-color: #f8f8f8;
        min-height: 100px;
        overflow-wrap: break-word;
      }
    </style>
  </head>
  <body>
    <div class="chat-container">
      <h1>GPT-3 대화를 시작하세요!</h1>
      <form id="chat-form">
        <input
          type="text"
          id="user-input"
          name="user_input"
          placeholder="안녕하세요? ..."
        />
        <button type="submit" id="submitBtn">Send</button>
      </form>
      <div id="result"></div>
    </div>

    <script>
      window.onload = function () {
        document
          .getElementById("chat-form")
          .addEventListener("submit", function (event) {
            // Prevent the form from submitting and refreshing the page
            event.preventDefault();

            let userInput = document.getElementById("user-input").value;
            let url = `/gpt?user_input=${encodeURIComponent(userInput)}`;

            fetch(url)
              .then((response) => response.json())
              .then((data) => {
                let content = data.content;
                let resultDiv = document.getElementById("result");
                resultDiv.innerHTML = content;
              })
              .catch((error) => {
                console.error("Error fetching GPT-3 response:", error);
              });
          });
      };
    </script>
  </body>
</html>
```
color.html
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>GPT-3 Whale Coding</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
      }

      .chat-container {
        background-color: #ffffff;
        border-radius: 5px;
        padding: 20px;
        width: 80%;
        max-width: 600px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
      }

      h1 {
        text-align: center;
        margin-bottom: 20px;
      }

      #chat-form {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
      }

      #user-input {
        flex-grow: 1;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
      }

      #submitBtn {
        background-color: #4caf50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 15px;
        margin-left: 10px;
        cursor: pointer;
      }

      #submitBtn:hover {
        background-color: #45a049;
      }

      #result {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 20px;
        background-color: #f8f8f8;
        min-height: 100px;
        overflow-wrap: break-word;
      }
    </style>
  </head>
  <body>
    <div class="chat-container">
      <h1>어울리는 색 추천</h1>
      <form id="chat-form">
        <input
          type="text"
          id="user-input"
          name="user_input"
          placeholder="밤하늘의 별..."
        />
        <button type="submit" id="submitBtn">Send</button>
      </form>
      <div id="result"></div>
    </div>

    <script>
      window.onload = function () {
        document
          .getElementById("chat-form")
          .addEventListener("submit", function (event) {
            event.preventDefault();

            let userInput = document.getElementById("user-input").value;
            let url = `/gpt_color?user_input=${encodeURIComponent(userInput)}`;

            fetch(url)
              .then((response) => response.json())
              .then((data) => {
                const content = JSON.parse(data.content)
                let recommendation = content.reasonForRecommendation;
                let resultDiv = document.getElementById("result");
                resultDiv.innerHTML = recommendation;

                const colorlist = content.colorlist;
                for (let i = 0; i < colorlist.length; i++) {
                    const divElem = document.createElement('div');
                    divElem.style.height = '50px';
                    divElem.style.backgroundColor = colorlist[i];
                    divElem.textContent = colorlist[i];
                    resultDiv.appendChild(divElem);
                }
              })
              .catch((error) => {
                console.error("Error fetching GPT-3 response:", error);
              });
          });
      };
    </script>
  </body>
</html>
```
