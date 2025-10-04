import json, random

class Problem:
    def random_question(self, quiz_kind):
        self.quiz_kind(quiz_kind)
        all_keys = list(self.questions.keys())
        selected_keys = random.sample(all_keys, 5)
        quiz_dict = {self.questions[count]: self.answers[count] for count in selected_keys}
        return quiz_dict

    def quiz_kind(self, quiz_kind):
        if quiz_kind == 1:
            with open('Q_nonsense.json', 'r', encoding='UTF-8') as open1:
                self.questions = json.load(open1)
            with open('A_nonsense.json', 'r', encoding='UTF-8') as open2:
                self.answers = json.load(open2)
        if quiz_kind == 2:
            with open('Q_IT.json', 'r', encoding='UTF-8') as open1:
                self.questions = json.load(open1)
            with open('A_IT.json', 'r', encoding='UTF-8') as open2:
                self.answers = json.load(open2)