# LLM

### 개념


### 학습자료
https://yongeekd01.tistory.com/118

### 실습
```python
# pip install tensorflow
import tensorflow as tf
# from tensorflow.keras.preprocessing.text import Tokenizer
from keras.layers import TextVectorization;
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
import numpy as np

# 데이터 준비
data = """
The quick brown fox jumps over the lazy dog. 
I am your father. 
To be or not to be, that is the question. 
All that glitters is not gold. 
I think, therefore I am. 
Elementary, my dear Watson. 
May the Force be with you. 
Houston, we have a problem. 
I'm the king of the world! 
It's alive! It's alive! 
You're gonna need a bigger boat. 
Here's looking at you, kid. 
Go ahead, make my day. 
I see dead people. 
Keep your friends close, but your enemies closer. 
I'll be back. 
You can't handle the truth! 
A martini. Shaken, not stirred. 
I feel the need—the need for speed. 
Carpe diem. Seize the day, boys. 
You talking to me? 
What we've got here is failure to communicate. 
I love the smell of napalm in the morning. 
You've got to ask yourself one question: 'Do I feel lucky?' Well, do you, punk? 
You had me at 'hello.' 
I'll have what she's having. 
Here's Johnny! 
Hasta la vista, baby. 
You can't handle the truth! 
Bond. James Bond.
"""

# 데이터 전처리

vectorize_layer = TextVectorization(
    max_tokens=None,  # 최대 단어 수 (None이면 제한 없음)
    output_mode='int',  # 정수 인덱스로 변환
    output_sequence_length=None  # 시퀀스 길이 (None이면 최대 길이로 맞춤)
)

# TextVectorization 레이어를 데이터에 맞게 어댑트
vectorize_layer.adapt([data])

# 어휘 사전 크기 계산
vocab = vectorize_layer.get_vocabulary()
total_words = len(vocab)

# 데이터 벡터화 및 시퀀스 생성
input_sequences = []
for line in data.split("\n"):
    # 텍스트를 시퀀스로 변환
    token_list = vectorize_layer([line])
    token_list = token_list.numpy()[0]
    
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

# 패딩
max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre')

# 특징과 라벨 분리
input_sequences = np.array(input_sequences)
X, y = input_sequences[:,:-1], input_sequences[:,-1]
y = tf.keras.utils.to_categorical(y, num_classes=total_words)

# 모델 정의
model = Sequential()
model.add(Embedding(total_words, 64, input_length=max_sequence_len-1))
model.add(LSTM(100))
model.add(Dense(total_words, activation='softmax'))

# 모델 컴파일
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 학습
model.fit(X, y, epochs=100, verbose=1)

# predict_next_word 함수
def predict_next_word(seed_text, next_words=1):
    for _ in range(next_words):
        token_list = vectorize_layer([seed_text])
        token_list = pad_sequences(token_list, maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict(token_list, verbose=0)
        predicted_word_index = np.argmax(predicted, axis=-1)[0]
        predicted_word = vocab[predicted_word_index]
        seed_text += " " + predicted_word
    return seed_text

# 예측
print(predict_next_word("The quick brown", 3))

```

### 설명
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 예제 텍스트 데이터
data = """
The quick brown fox jumps over the lazy dog. 
I am your father. 
To be or not to be, that is the question. 
...
Bond. James Bond.
"""

# TextVectorization 레이어 생성 (토크나이저 역할)
vectorize_layer = TextVectorization(
    max_tokens=None,  # 사용할 최대 토큰 수 (None이면 모든 단어 사용)
    output_mode='int',  # 정수 인덱스의 시퀀스로 출력
    output_sequence_length=None  # 출력 시퀀스 길이 (None이면 원래 길이 사용)
)

# TextVectorization 레이어를 데이터에 맞게 어댑트 (학습)
vectorize_layer.adapt([data])

# 어휘 사전 생성 및 크기 계산
vocab = vectorize_layer.get_vocabulary()  # 어휘 사전 리스트를 반환
total_words = len(vocab)  # 어휘 사전의 총 단어 수

# 데이터 전처리
input_sequences = []  # 입력 시퀀스를 저장할 리스트
for line in data.split("\n"):  # 데이터를 줄 단위로 나눔
    token_list = vectorize_layer([line])  # 각 줄을 정수 인덱스의 시퀀스로 변환
    token_list = token_list.numpy()[0]  # 넘파이 배열로 변환 후 1차원 배열 추출
    for i in range(1, len(token_list)):  # 2번째 단어부터 마지막 단어까지 반복
        n_gram_sequence = token_list[:i+1]  # i+1번째까지의 n-그램 시퀀스 생성
        input_sequences.append(n_gram_sequence)  # 시퀀스를 리스트에 추가

# 시퀀스 패딩 (모든 시퀀스의 길이를 동일하게 맞춤)
max_sequence_len = max([len(x) for x in input_sequences])  # 시퀀스의 최대 길이
input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre')

# 특징(X)과 라벨(y) 분리
input_sequences = np.array(input_sequences)  # 입력 시퀀스를 넘파이 배열로 변환
X, y = input_sequences[:,:-1], input_sequences[:,-1]  # X는 시퀀스의 마지막 단어 제외, y는 마지막 단어
y = tf.keras.utils.to_categorical(y, num_classes=total_words)  # y를 원-핫 인코딩으로 변환

# 간단한 LSTM 모델 정의
model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequence_len-1))  # 임베딩 레이어
model.add(LSTM(150))  # LSTM 레이어
model.add(Dense(total_words, activation='softmax'))  # 출력 레이어 (소프트맥스 활성화 함수 사용)

# 모델 컴파일 (손실 함수와 옵티마이저 설정)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 학습
model.fit(X, y, epochs=10, verbose=1)  # 10번 에포크 동안 학습

# 예측 함수 정의
def predict_next_word(seed_text, next_words=1):
    for _ in range(next_words):
        token_list = vectorize_layer([seed_text])  # 입력 텍스트를 정수 인덱스로 변환
        token_list = pad_sequences(token_list, maxlen=max_sequence_len-1, padding='pre')  # 패딩
        predicted = model.predict(token_list, verbose=0)  # 다음 단어 예측
        predicted_word_index = np.argmax(predicted, axis=-1)[0]  # 가장 높은 확률의 단어 인덱스 선택
        predicted_word = vocab[predicted_word_index]  # 인덱스를 단어로 변환
        seed_text += " " + predicted_word  # 시드 텍스트에 예측된 단어 추가
    return seed_text

# 예측 테스트
print(predict_next_word("The quick brown", next_words=3))  # "The quick brown" 다음에 올 세 단어 예측

```
