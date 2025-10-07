from quiz_db import Problem
from typing import List  # 타입힌트를 제공
from threading import Timer, Thread

# 문제, 정답을 담은 변수와 정답을 체크하는 함수를 담은 클래스
class Question:
    def __init__(self, text: str, answer: str):
        self.text = text   # 문제를 담는 변수
        self.answer = answer  # 정답을 담는 변수

    # 사용자 입력 값과 정답이 일치하는지 비교하여 T/F를 리턴하는 함수
    def check(self, user_input: str) -> bool:
        # 입력 받은 값과 정답이 (공백을 제거하고 대소문자 구분 없이) 같은지 비교
        return user_input.replace(" ", "").lower() == self.answer.replace(" ", "").lower()

# 퀴즈명, 퀴즈 종류 구분을 위한 변수를 담은 클래스
class QuizSet:
    def __init__(self, name: str, quiz_kind: int):
        self.name = name   # 퀴즈명
        self.quiz_kind = quiz_kind   # 퀴즈 종류(1: 넌센스, 2: IT 용어)

# 전반적인 게임 진행 클래스
class QuizGame:
    # QuizSet클래스를 리스트로 저장한 변수, 라운드당 문제수(5)를 저장한 변수 생성 후 초기화
    def __init__(self, quiz_sets: List[QuizSet]):
        # {"1": QuizSet("넌센스 퀴즈",1), "2": QuizSet("IT 용어 퀴즈",2)}
        self.quiz_sets = {str(i+1): qs for i, qs in enumerate(quiz_sets)}

    # 퀴즈 도입부 (종류 선택 or 종료) -> 1. 넌센스 퀴즈 ...
    def show_menu_and_get_choice(self):
        print("=== 🤗 퀴즈 게임에 오신 걸 환영합니다! 🤗 ===\n")
        # .items() : (키,값)쌍을 묶은 튜플 '객체'를 반환
        for key, qs in self.quiz_sets.items():
            print(f"{key}. {qs.name}")
        print("q. 종료")

        sel = input("\n플레이할 게임을 선택해주세요~!(1 또는 2, 종료는 q) : ").replace(" ", "").lower()
        if sel == "q":
            print("게임을 종료합니다. 안녕히가세요!👋")
            exit(0)

        if sel in self.quiz_sets:
            return sel   # "1" 또는 "2"를 반환(key)
        else:
            return None

    # 게임 진행 여부 체크 함수
    def ask_continue_or_exit(self) -> bool:
        while True:
            ans = input("계속하시겠습니까? (계속/종료(q)): ").replace(" ", "").lower()
            if ans in ('계속', 'y', 'yes', 'continue'):
                return True
            elif ans in ('종료', 'q', 'n', 'no', 'exit'):
                return False
            else:
                print("입력값을 이해하지 못했어요. '계속' 또는 '종료'로 입력해주세요.")

    # 게임 시작, 종료와 관련된 함수
    def start_quit(self):
        while True:
            # 해당 함수의 리턴값(1 또는 2 또는 q)을 저장
            choice = self.show_menu_and_get_choice()
            if choice is None:
                print("잘못된 입력입니다. 다시 선택하세요.")
                continue

            # Problem 클래스에서 문제 불러오기
            problem_db = Problem()
            # 문제를 랜덤으로 5개 가져와서 dict 형태로 저장
            quiz_dict = problem_db.random_question(self.quiz_sets[choice].quiz_kind)
            # 문제와 답을 저장한 클래스 객체 5개를 list 형태로 저장
            questions = [Question(text, answer) for text, answer in quiz_dict.items()]
            # 퀴즈명과 종류(1또는2)를 저장한 QuizSet 클래스 객체를 저장
            quizset = self.quiz_sets[choice]

            # 게임 중단
            quit_mid = self.play_quiz(quizset, questions)
            if quit_mid:
                # 게임 도중 q로 빠져나온 경우, 게임을 계속할건지 물어보기
                cont = self.ask_continue_or_exit()
                if not cont:
                    print("게임을 종료합니다. 수고하셨어요~!👋")
                    break
                else:
                    continue

            # 한 라운드가 끝나면 계속할건지 물어봄
            cont = self.ask_continue_or_exit()
            if not cont:
                print("게임을 종료합니다. 수고하셨어요~!👋")
                break

    # 라운드 플레이 관련 함수
    def play_quiz(self, quizset: QuizSet, questions: List[Question]) -> bool:
        print(f"\n=== {quizset.name} (5문제) ===")
        score = 0
        # 5문제를 푸는 반복문!
        for idx, q in enumerate(questions, start=1):  # 인덱스 시작값을 0이 아닌, 1로 지정
            # 출력 예시 => 문제 1/5: 'ndarray + index + column' 하면?
            print(f"\n문제 {idx}/{len(questions)}: {q.text}")

            answer_received = False  # 정답을 입력받는 변수

            def timeout():
                nonlocal answer_received
                if not answer_received:
                    print(f"⏰ 시간 초과 !!!")
                    answer_received = True

            # threading 모듈에 Timer 클래스 객체 생성
            # 20초 후에 timeout 함수를 실행하겠다!
            t = Timer(20, timeout)
            t.start()  # 타이머 시작

            raw = input("답 (20초 안에 입력하세요! q 입력시 종료됩니다.): ")
            answer_received = True   # 사용자 입력시 True로 바꿔줌
            t.cancel()   # 타이머 종료

            # q를 입력하면 게임 중단
            if raw.replace(" ", "").lower() == 'q':
                print("게임을 중단합니다.")
                return True
            # 엔터만 친 경우는 다음으로 계속
            if not raw.replace(" ", ""):
                print(f"❌ 정답을 입력하지 않아 오답처리 됩니다. 정답은 '{q.answer}' 입니다!")
                continue
            # 정답과 일치하면 T / 일치하지 않으면 F
            if q.check(raw):
                print("✅ 정답!")
                score += 1
            else:
                print(f"❌ 오답입니다! 정답은 '{q.answer}' 입니다!")

        print(f"\n === 라운드가 종료되었습니다. === \n 📊 맞춘 문제 수: {score}/{len(questions)}")
        return False  # 라운드 정상 종료

# 문제 데이터 생성
def make_sample_quizsets():
    return [
        QuizSet("넌센스 퀴즈", 1),
        QuizSet("IT 용어 퀴즈", 2)
    ]

# 실행
if __name__ == "__main__":
    quizsets = make_sample_quizsets()
    game = QuizGame(quizsets)
    game.start_quit()