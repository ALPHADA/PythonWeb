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

# if __name__ == '__main__':
#    app.run(debug=True)
