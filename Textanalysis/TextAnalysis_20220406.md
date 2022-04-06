### 텍스트 분석

--------------------------------------------------------------------------------

- 토큰화 : 텍스트를 일정한 단위(문장 단위, 단어 단위, 형태소 단위)로 구분짓는 일

- 문장 단위 토큰화(sentence tokenization)
- 단어 단위 토큰화(word tokenization)
- 형태소 단위 토큰화(POS tokenization)

1. 품사 태깅
   - 문법 범주 할당
2. 표제어 추출
   - 감성사전 및 토픽사전 단어 추가 등 사전관리
3. 형태소 분석
   - 자립/의존형태소 분리
4. 불용어 제거
   - 가치 없는 토큰 and, the, a 등 제거



### konlpy

------------------------------------------------------------

- 한국어 형태소 분석 패키지

- 자바 기반 파이썬 라이브러리

  1. 패키지 설치

     ```python
     !python -m pip install --upgrade konlpy
     ```

  2. 

  3. ddd

  4. ddd

  5. ddd

  6. ddd

4

- 형태소 분석이란?
  - 형태소를 분석하여 어근, 접두사/접미사 등 문장의 다양한 언어적 속성의 구조를 분석하는 것

- 형태소 태깅?
  - part-of-speech tagging, POS tagging, or simply tagging
  - 문장에서 각 형태소 역할(명사, 동사, 형용사 등 품사)을 식별하여 분류하고 그에 따라 태그를 붙이는 과정을 말한다.
  - 즉, 품사(part-of-speech, POS)를 사용해 주어진 문장의 단어를 분리하는 프로세스다.
- 품사(part-of-speech, POS)
  - 문장에서의 형태소의 역할(명사, 동사, 형용사 등)을 나타낸다.



#### KoNLPy에서 제공하는 형태소 분석기 5개

- Hannanum, Komoran, Kkma, Mecab, Okt

- 한나눔

  - ```python
    hannanum = konlpy.Hannanum()
    hannanum.pos(text)
    ```

- 코모란

  - ```python
    komoran = konlpy.tag.Komoran()
    komoran.pos(text)
    ```

- 꼬꼬마

  - ```python
    kkma = konlpy.tag.Kkma()
    kkma.pos(text)
    ```

- Open Korean Text(Okt)

  - ```python
    okt = konlpy.tag.Okt()
    okt.pos(text)
    ```



s





