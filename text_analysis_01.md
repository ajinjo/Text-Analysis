# 텍스트 분석

- 비정형 텍스트에서 의미 있는 정보를 추출 (비정형 데이터인 텍스트를 분석하는것)
- ML모델은 주어진 정형 데이터 기반에서 모델을 수립하고 예측을 수행함
- 또한 숫자형의 피처 기반 데이터만 입력받을 수 있기 때문에 텍스트를 머신러닝에 적용하기 위해서는 비정형 텍스트 데이터를 어떻게 피처 형태로 추출하고 추출된 피처에 의미 있는 값을 부여하는가 하는 것이 매우 중요함
- 텍스트를 word기반의 다수의 피처로 추출하고 이 피처에 단어 빈도수같은 숫자값을 부여하면 텍스트는 단어의 조합인 벡터값으로 표현됨 
- 피처 벡터화(BOW, Word2Vec방법) , 피처 추출(Feature Extraction)



### 텍스트 분류

- 문서가 '특정 분류' 또는 '카테고리'에 속하는 것을 예측하는 기법

- 특정 신문 기사 내용이 연애/정치/사회/문화 중 어떤 카테고리에 속하는지 자동으로 분류하거나 스팸 메일 검출 같은 프로그램

- 지도학습 방법 적용

  

### 감성 분석

- 텍스트에 나타나는 감정/판단/믿음/의견/기분 등 주관적인 요소를 분석하는 기법

- 소셜 미디어 감정 분석, 영화나 제품에 대한 긍정 또는 리뷰, 여론조사 의견 분석 등 다양한 영역에서 활용됨 

- 지도학습 방법뿐만 아니라 비지도학습 이용해 적용할 수 있음

  

### 텍스트 요약

- 텍스트 내에서 중요한 주제나 중심 사상을 추출하는 기법 
- 토픽 모델링



### 텍스트 군집화와 유사도 측정 

- 비슷한 유형의 문서에 대해 군집화 수행하는 기법
- 텍스트 분류를 비지도학습을 수행하는 방법의 일환
- 문서들간의 유사도 측정해 비슷한 문서끼리 모을 수 있는 방법



### 텍스트 분석 수행 프로세스

① 텍스트 전처리 : 텍스트를 피처로 만들기 전에 미리 클렌징, 대/소문자 변경, 특수문자 삭제 등의 클렌징 작업, 단어 등의 토큰화 작업, 의미 없는 단어 Stop word 제거 작업, 어근 추출(Stemming/Lemmatization)등의 텍스트 정규화 작업을 수행하는 것을 통칭함.

② 피처 벡터화/추출 : 사전 준비 작업으로 가공된 텍스트에서 피처를 추출하고 여기에 벡터값을 할당함. 대표적인 방법은 BOW와 Word2Vec이 있으며 BOW는 대표적으로 Count기반과 TF-IDF 기반 벡터화가 있음.

③  ML 모델 수립 및 학습/예측/평가 : 피처 벡터화된 데이터 세트에 ML모델을 적용해 학습/예측/평가를 수행함. 





## 텍스트 사전 준비 작업 '텍스트 전처리' - 텍스트 정규화

텍스트 자체를 바로 피처로 만들 수는 없다. 따라서 사전에 텍스트를 가공하는 준비 작업이 필요하다. 텍스트 정규화는 텍스트를 머신러닝 알고리즘이나 NLP 애플리케이션에 입력 데이터로 사용하기 위해 ※클렌징/정제/토큰화/어근화※ 등 다양한 텍스트 데이터의 사전 작업을 수행하는 것을 의미한다. 

텍스트 분석은 이러한 텍스트 정규화 작업이 매우 중요하다. 

1) 클렌징

   - 텍스트 분석에 방해가 되는 ※불필요한 문자, 기호※ 등을 사전에 제거하는 작업
   - HTML, XML 태그나 특정 기호 등을 사전에 제거함 

2) 토큰화

   - 문서에서 문장을 분리하는 문장 토큰화

     - 문장의 마침표(.), 개행문자(\n) 등 문장의 마지막을 뜻하는 기호에 따라 분리하는 것이 일반적

     - sent_tokenize()를 이용해 문장 토큰화를 수행함 

     - ```python
       from nltk import sent_tokenize
       import nltk
       nltk.download('punkt')
       
       text_sample = 'The Matrix is everywhere its all around us, here even in this room.\
       			   You can see it out your window or on your television.\
       			   You feel it when you go to work, or go to church or pay your taxes.'
       senetences = sent_tokenize(text = text_sample)
       print(type(sentences), len(sentences))
       print(sentences)
       
       # <class 'list'> 3
       ```

   - 문장에서 단어를 분리하는 단어 토큰화

     - 공백, 콤마(,), 마침표(.), 개행문자 등으로 단어를 분리함

     - 정규 표현식을 이용해 다양한 유형으로 토큰화를 수행 할 수 있음

     - word_tokenize()를 이용해 단어 토큰화를 수행함

     - ```python
       from nltk import word_tokenize
       
       sentence = "The Matrix is everywhere its all around us, here even in this room."
       words = word_tokenize(sentence)
       print(type(words), len(words))
       print(words)
       
       # <class 'list'> 15 
       ```

3) 필터링/스톱 워드 제거/철자 수정

   - 스톱 워드(Stop word) : 분석에 큰 의미가 없는 단어

   - is, the, a, will 등 문장을 구성하는 필수 문법 요소지만 문맥적으로 큰 의미가 없는 단어 

   - ```python
     import nltk
     nltk.download('stopwords')
     
     print('영어 stop words 개수:', len(nltk.corpus.stopwords.words('english')))
     print(nltk.corpus.stopwords.words('english')[:20])
     ```

     - 문장별로 단어를 토큰화해 생성된 리스트에 대해서 stopwords를 필터링으로 제거해 분석을 위한 의미 있는 단어만 추출

     - ```python
       import nltk
       
       stopwords = nltk.corpus.stopwords.words('english')
       all_tokens = []
       
       # 위 예제에서 3개의 문장별로 얻은 word_tokens list에 대해 스톱 워드를 제거하는 반복문 
       for sentence in word_tokens:
           filtered_words = []
           # 개별 문장별로 토큰화된 문장 list에 대해 스톱 워드를 제거하는 반복문
           for word in sentence:
               # 소문자로 모두 변환합니다.
               word = word.lower()
               # 토큰화된 개별 단어가 스톱 워드의 단어에 포함되지 않으면 word_tokens에 추가
               if word not in stopwords:
                 filtered_words.append(word)
           all_tokens.append(filtered_words)
       print(all_tokens)
       
       # [['matrix','everywhere','around','us',',',even',,'room','.''],['see','window','television','.'],'feel','go','work',',','go','church','pay','taxes','.']
       # is, this와 같은 스톱 워드가 필터링을 통해 제거됨
       ```

       

4) Stemming

5) Lemmatization









