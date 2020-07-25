#### 컴퓨터 기기 내 정보의 표현과 저장
1. 컴퓨터 정보는 2진수 bit들로 표현
2. 진법: 유한한 심볼로 무한한 숫자를 표현하는 방법

#### 프로그램 코드
1. high-level language
   - 영문자/숫자로 구성되어 사람이 이해하기 쉬운 언어
   - Python, C, C++, PASCAL, Scratch 등
   - Compiler, Assembler를 이용하여 기계어로 번역
2. Assembly language
   - 고급언어와 기계어 사이의 중간 언어
   - Assembler로 번역 시, 기계어와 일대일 대응
3. Machine language
   - 컴퓨터 하드웨어가 이해할 수 있는 언어
   - 2진 bit들로 구성

#### high-level language의 구성요소
- Vocabulary / Word
   - 변수와 예약어
- Sentence structure
   - 유효한 문법에 따른 변수, 예약어, 상수 등의 조합
- Story-structure building
   - 문제 해결을 위해 문법에 맞는 명령어들을 구성
   - 순차/반복/조건 등과 함수를 통한 코드 재활용 및 재귀
---

## Hello, python
#### 특징
- 단순함, 배우기 쉬운 언어
- 오픈 소스 소프트웨어
- 고수준 언어
- 이식성
- 객체지향언어
- 확장성
- 인터프리터 언어
   - 컴파일 과정을 필요로 하지 않으며, 소스코드로부터 곧바로 실행
- 포함성
   - C/C++ 프로그램에 파이썬을 포함하도록 하여 프로그램을 사용하는 사용자들이 스크립팅 기능을 사용
- 확장 가능한 라이브러리
 
 
#### 파이썬으로 할 수 있는 일
- 시스템 유틸리티
- GUI 프로그램
- C/C++과의 결합
- 웹 프로그래밍
- 수치연산 프로그래밍
- 데이터베이스 프로그래밍
- 그러나, 대단히 빠른 속도를 요구하거나 하드웨어를 직접 다루어야 하는 프로그램에는 적합하지 않음
---

### Python 수행방법
1. Interpreter
   - 파이썬 쉘에 한 문장(명령어)씩 타이핑, 입력하면, 파이썬은 문장을 수행하고 결과를 보여줌
      - 문답식으로 프로그램 진행
      - 대화형 쉘(interactive shell) 또는 대화형 모드(interactive mode): 파이썬 쉘은 파이썬 인터프리터와 대화하듯이 코드를 처리
   - 끝내려면? quit()이라 타이핑하고 enter키

2. Python script
   - 파이썬 인터프리터는 짧은 프로그램을 실험하는데 편리
   - 긴 프로그램은, 파일로 저장하고 파이썬이 파일을 수행하도록 하는 것이 나음
      - 관례적으로 파이썬 프로그램 파일은 .py 확장자를 붙여 저장

##### 대화식 vs 스크립트
- 대화식(Interactive)
   - 파이썬에 한 행씩 타이핑하면 파이썬이 대답
- 스크립트(Script)
   - 편집기(text editor)를 사용하여 일련의 문장들을 파일에 저장하고 파이썬에게 파일 속의 문장들을 순차적으로 수행하도록 함

3. python IDLE
   - python Integrated Development and Learning Environment
      - python 프로그램 작성을 도와주는 통합 개발환경
      - python 설치 시 기본으로 설치되는 프로그램
      
##### python에서 자주 보이는 에러
- 에러
   - NameError: name ... is not defined: 함수 이름을 잘못 입력했을 때 발생하는 에러
   - 파이썬은 대소문자를 구분하므로 대소문자를 정확히 입력
   - print처럼 전부 소문자로 입력했는지 확인
   - SyntaxError: invalid syntax: print() 안에 Hello,world!를 넣을 때 ''로 묶지 않아서 발생하는 구문 에러
   - SyntaxError: EOL while scanning string literal: 따옴표를 잘못 사용했을 때 발생하는 구문 에러
- IDLE의 파이썬 쉘에서는 위쪽 방향키를 누르면 이전 코드로 돌아갈 수 있음



   
   
