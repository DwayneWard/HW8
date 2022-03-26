class GenericQuestion:
    """
    Класс является базовым.
    Инициализирует экземпляр и высчитывает сложность вопроса для вывода пользователю
    """

    def __init__(self):
        self.question = ""
        self.author = ""
        self.hardness = ''
        self.correct_answers = []
        self.unit = ''
        self.is_asked = False
        self.user_answer = None
        self.points = 0

    def hard(self):
        hard = ''
        if 1 <= int(self.hardness) < 3:
            hard = "легко"
        elif 3 <= int(self.hardness) < 4:
            hard = "средне"
        elif 4 <= int(self.hardness) <= 5:
            hard = "сложно"

        return hard


class Question(GenericQuestion):
    """
    Класс-наследник класса GenericQuestion.
    """

    @property
    def correct_answers(self):
        return self._correct_answers

    @property
    def points(self):
        return self._points

    def set_question(self, question):
        self.question = question

    def set_author(self, author):
        self.author = author

    def set_hardness(self, hardness):
        self.hardness = hardness

    def set_unit(self, unit):
        self.unit = unit

    def set_is_asked(self, is_asked):
        self.is_asked = is_asked

    def set_user_answer(self, user_answer):
        self.user_answer = user_answer

    def calculate_points(self):
        return int(self.hardness) * 10

    def is_correct(self):
        return self.user_answer in self.correct_answers

    def __repr__(self):
        return f"""тема: {self.unit}, сложность: {self.hard()}
{self.question}"""

    @correct_answers.setter
    def correct_answers(self, value):
        self._correct_answers = value

    @points.setter
    def points(self, value):
        self._points = value

    def set_correct_answers(self, correct_answers):
        self._correct_answers = correct_answers

    def set_points(self, points):
        self._points = points
