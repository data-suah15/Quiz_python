import threading
from typing import List # 타입 힌트
from quiz_DB import Problem


# 문제, 답, 사용자 입력에 대한 클래스
class Question:

    def __init__(self, text: str, answer: str):
        self.text = text  # 문제
        self.answer = answer  # 답

    # 사용자 입력
    def check(self, user_input: str) -> bool:
        # 공백 제거, 소문자 비교: 대소문자 무시, 양쪽 공백 무시
        return user_input.replace(" ", "").lower() == self.answer.replace(" ", "").lower()

# 퀴즈 명, 문제, 문제 랜덤 추출에 관한 클래스
class QuizSet:

    def __init__(self, name: str, quiz_kind: int):
        self.name = name  # 퀴즈 이름
        self.quiz_kind = quiz_kind  # 문제 종류 (1: 넌센스, 2: IT)


# 전반적인 게임 진행 클래스
class QuizGame:

    # 객체 생성 및 초기화
    def __init__(self, quiz_sets: List[QuizSet], num_questions_per_round: int = 5):
        self.quiz_sets = {str(i+1): qs for i, qs in enumerate(quiz_sets)}
        self.num_questions_per_round = num_questions_per_round

    # 게임의 도입부와 관련된 함수
    def start(self):
        while True:
            choice = self.show_menu_and_get_choice()
            if choice is None:
                print("잘못된 입력입니다. 다시 선택하세요.")
                continue
            # Problem에서 실제 문제 불러오기
            problem_db = Problem()
            quiz_dict = problem_db.random_question(self.quiz_sets[choice].quiz_kind)
            questions = [Question(text, answer) for text, answer in quiz_dict.items()]

            # 실제 문제와 답을 가진 QuizSet 생성
            quizset = QuizSet(self.quiz_sets[choice].name, self.quiz_sets[choice].quiz_kind)
            quit_mid = self.play_quiz(quizset, questions)

            if quit_mid:
                # 게임 도중 q로 빠져나온 경우, 다시 메인으로
                cont = self.ask_continue_or_exit()
                if not cont:
                    print("게임을 종료합니다. 수고하셨어요!")
                    break
                else:
                    continue

            # 한 판 끝나면 계속할건지 물어봄
            cont = self.ask_continue_or_exit()
            if not cont:
                print("게임을 종료합니다. 수고했어요!")
                break

    # 퀴즈 도입부 (종류 선택 or 종료)
    def show_menu_and_get_choice(self):
        print("=== 🤗 퀴즈 게임에 오신 걸 환영합니다! 🤗 ===\n")
        for key, qs in self.quiz_sets.items():
            print(f"{key}. {qs.name}")
        print("q. 종료")

        sel = input("선택(1 또는 2, 종료는 q): ").replace(" ", "").lower()
        if sel == 'q':
            print("게임을 종료합니다. 안녕히가세요!👋")
            exit(0)
        if sel in self.quiz_sets:
            return sel
        return None

    # 라운드 플레이 관련 함수
    def play_quiz(self, quizset: QuizSet, questions: List[Question]) -> bool:
        print(f"\n=== '{quizset.name}' (5문제) ===")
        score = 0

        for idx, q in enumerate(questions, start=1):
            print(f"\n문제 {idx}/{len(questions)}: {q.text}")

            answer_received = [False]  # 입력 받기 전까지는 False

            def timeout():
                if not answer_received[0]:
                    print("\n시간이 초과! 오답 처리됩니다.")
                    answer_received[0] = True

            # 20초 타이머 시작
            t = threading.Timer(20, timeout)
            t.start()

            raw = input("답 (20초 안에 입력하세요!!! q 입력시 종료): ")
            answer_received[0] = True  # 사용자가 입력하면 True로 바꿔줌
            t.cancel()  # 타이머 종료

            if raw.replace(" ", "").lower() == 'q':
                print("중간에 게임을 종료합니다.")
                return True

            if not raw.replace(" ", ""):  # 그냥 엔터만 친 경우는 오답 처리
                continue

            if q.check(raw):
                print("✅ 정답! ")
                score += 1
            else:
                print(f"❌ 오답! 정답: {q.answer}")

        print(f"\n === 라운드가 종료되었습니다. === \n 📊 맞춘 문제 수: {score}/{len(questions)}")
        return False  # 정상 종료

    # 게임 진행 여부 체크 함수
    def ask_continue_or_exit(self) -> bool:
        while True:
            ans = input("계속하시겠어요? (계속/종료(q)): ").replace(" ", "").lower()
            if ans in ('계속', 'c', 'y', 'yes'):
                return True
            if ans in ('종료', 'q', 'n', 'no', 'exit'):
                return False
            print("입력값을 이해하지 못했어요. '계속' 또는 '종료'로 입력하세요.")

# 문제 데이터 생성
def make_sample_quizsets():
    return [
        QuizSet("넌센스 퀴즈", 1),
        QuizSet("IT 퀴즈", 2)
    ]

# 실행
if __name__ == "__main__":
    quizsets = make_sample_quizsets()
    game = QuizGame(quizsets)
    game.start()