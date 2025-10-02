import json, random

class Problem:
    def f_random_question(self, a_quiz_kind):
        self.f_quiz_kind(a_quiz_kind)
        v_all_keys = list(self.v_questions.keys())
        v_selected_keys = random.sample(v_all_keys, 5)
        v_quiz_dict = {self.v_questions[v_count]: self.v_answers[v_count] for v_count in v_selected_keys}
        return v_quiz_dict

    def f_quiz_kind(self, a_quiz_kind):
        if a_quiz_kind == 1:
            with open('Q_nonsense.json', 'r', encoding='UTF-8') as v_open1:
                self.v_questions = json.load(v_open1)
            with open('A_nonsense.json', 'r', encoding='UTF-8') as v_open2:
                self.v_answers = json.load(v_open2)
        if a_quiz_kind == 2:
            with open('Q_IT.json', 'r', encoding='UTF-8') as v_open1:
                self.v_questions = json.load(v_open1)
            with open('A_IT.json', 'r', encoding='UTF-8') as v_open2:
                self.v_answers = json.load(v_open2)