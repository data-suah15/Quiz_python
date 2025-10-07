# 🎮 Terminal Quiz Game_python
두 가지 퀴즈(넌센스 / IT 용어) 중 선택하여 제한시간 내에 문제를 푸는 텍스트 기반 게임<br />파이썬으로 구현


## 1️⃣ 프로젝트 개요
이 프로젝트는 파이썬으로 구현한 CLI(터미널) 환경에서 실행되는 퀴즈 게임입니다.<br />
사용자는 ‘넌센스 퀴즈’ 또는 ‘IT 용어 퀴즈’ 중 하나를 선택해 플레이하며,<br />
랜덤으로 선택된 5문제를 풀게 되고 각 문제는 제한시간 안에 답을 입력해야 합니다.<br />
문제를 풀때마다 정답 개수가 계산되고, 라운드가 종료되면 결과가 출력됩니다.<br />
이후 플레이를 계속할 것인지 종료할 것인지를 선택하여 플레이를 반복합니다.


## 2️⃣ 파일 구조
```bash
        .
        ├── Q_nonsense.json # 넌센스 문제(딕셔너리 형태) 
        ├── A_nonsense.json # 넌센스 정답(딕셔너리 형태)
        ├── Q_IT.json       # IT 용어 문제(딕셔너리 형태)
        ├── A_IT.json       # IT 용어 정답(딕셔너리 형태)
        ├── quiz_DB.py      # DB(json파일 열기)/문제 선택 관련 로직
        ├── quiz_main.py    # 메인 실행 파일(게임 실행)
        └── README.md       # 프로젝트 설명서
```


## 3️⃣ 실행방법
```bash
git clone https://github.com/username/project.git  
cd project  
python main.py
```


## 4️⃣ 주요 기능

✅ 두 가지 모드 선택 — 넌센스 / IT 용어 퀴즈 중 선택해서 플레이.

✅ 제한시간 문제 풀이 — 각 문제는 제한 시간(20초) 내에 답 입력.

✅ 정답 자동 판정(입력 정규화) — 입력의 공백 제거 및 대소문자 무시로 유연한 채점.

✅ 중간 종료 지원 — 문제 중간에 q 입력 시 라운드 즉시 종료.

✅ 라운드별 결과 출력 — 라운드 종료 후 정답 개수 출력.

✅ 간단한 반복(계속/종료) 흐름 — 라운드 종료 후 계속 플레이 여부 선택 가능.

✅ 간단한 인터페이스 — 텍스트 기반의 직관적인 UI


## 5️⃣ 실행 예시
<img width="400" height="350" alt="image" src="https://github.com/user-attachments/assets/6c49d363-f32c-4b20-aca4-7d6a920eb0bd" /><br />
<img width="488" height="350" alt="image" src="https://github.com/user-attachments/assets/2abb280f-31ec-4a69-a626-be15e7b34f3f" />


## 6️⃣ 기술 스택
### Python 3.13.7<br />
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"><img src="https://img.shields.io/badge/CLI-0F0F0F?style=for-the-badge&logo=terminal&logoColor=white">

### 주요 라이브러리
- **json** : 문제, 정답 파일 읽어오기
- **random** : 5문제 랜덤 추출
- **typing** - List : 타입 힌트로 코드 가독성 향상
- **threading** - Timer / Thread : 시간 제한 기능 구현시 활용

## 7️⃣ 개발 환경
- **OS** : Windows 10/11, MacOS Sequoia
- **IDE/Editor** : PyCharm
- **버전 관리** : GitHub

## 프로젝트 후기


## 참고
https://cocoon1787.tistory.com/689 (기술스택 벳지 설정방법 링크)
