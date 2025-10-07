# QUIZ_GAME_mini_project
파이썬 미니 프로젝트로 퀴즈 게임 구현

## 프로그램 구조
```bash
        .
        ├── Q_nonsense.json # nonsense 문제(딕셔너리 형태) 
        ├── A_nonsense.json # nonsense 정답(딕셔너리 형태)
        ├── Q_IT.json # IT 문제(딕셔너리 형태)
        ├── A_IT.json # IT 정답(딕셔너리 형태)
        ├── quiz_DB.py # DB/문제 선택 관련 로직
        ├── quiz_main.py # 메인 실행 파일(게임 실행)
        └── README.md
```


## 기술 스택
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
버전 : Python 3.13.7


## 실행 결과 - 단계별

## 프로젝트 후기
## 참고
https://cocoon1787.tistory.com/689 (기술스택 벳지 설정방법 링크)

## 🛠 기술 스택 (Tech Stack)

### 언어 & 런타임
- **Python 3.x**
  - 기본 문법 (변수, 자료형, 조건문, 반복문, 함수, 클래스)
  - 객체지향 프로그래밍 (클래스/메서드 설계)
  - 문자열 처리 (`strip()`, `lower()` 등)

### 주요 라이브러리
- **random** : 문제 랜덤 추출
- **typing** : 타입 힌트(`List`, `Dict`)로 코드 가독성 향상
- **threading** *(선택)* : 시간 제한 기능 구현 시 활용

### 프로그램 구조
- **클래스 기반 설계**
  - `Question` : 문제와 정답 관리
  - `QuizSet` : 문제집 관리 및 랜덤 추출
  - `QuizGame` : 메뉴 출력, 게임 진행, 정답 확인
- 함수형 프로그래밍 일부 활용 (정답 비교, 입력 처리)

### 개발 환경
- **OS** : Windows 10/11
- **IDE/Editor** : Visual Studio Code
- **버전 관리** : Git / GitHub

### 협업 & 관리
- GitHub Repository로 코드 버전 관리
- README.md를 통한 문서화

---

## 📌 프로젝트 특징
- CLI(콘솔 기반) 퀴즈 게임
- OOP(Object-Oriented Programming) 적용
- 사용자 입력 처리 (공백/대소문자 무시)
- 문제 랜덤 출제 기능
- *(선택 기능)* 제한 시간 내 정답 입력
