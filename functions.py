import random
from classes import Question
import json

def print_info():
    print("""Перед началом игры необходимо знать:
1. На вопросы можно отвечать либо цифрами, либо словами;
2. Ответ словами записывается ТОЛЬКО прописными буквами (например, november);
3. Игра начнется через 10 секунд\n""")

def read_json(file: json) -> dict:
    """
    Фукнция производит чтение из json файла, формирует исходный список questions и перемешивает список.

    :param file: Имя файла

    :return: Данные из json-файла.
    """
    with open(file, 'r') as file:
        questions_temp = json.load(file)
    return questions_temp


def form_random_question(questions_from_json: dict) -> list:
    """
    Функция реализует заполнение полей экземпляров класса Question и рандомизацию

    :param questions_from_json: Полученные из JSON файла данные

    :return: Рандомизированный список вопросов
    """
    questions = []
    for key in questions_from_json.keys():
        question = Question()
        question.set_question(questions_from_json[key]['question'])
        question.set_author(questions_from_json[key]['author'])
        question.set_unit(questions_from_json[key]['unit'])
        question.set_hardness(questions_from_json[key]['hardness'])
        question.set_correct_answers(questions_from_json[key]['correct_answers'])
        questions.append(question)

    random.shuffle(questions)

    return questions


def set_game_data(question: Question) -> Question:
    """
    Функция производит запись данных игры пользователя в атрибуты словаря с вопросом

    :param question: Текущий вопрос

    :return: Измененный
    """

    if question.is_correct():
        question.set_is_asked(True)
        question.set_points(question.calculate_points())

    return question


def final_points(final_data: list) -> int:
    """
    Функция возвращает количество правильных ответов пользователя

    :param questions: Список вопросов с необходимыми записями по окончании игры

    :return: Количество правильно отвеченных вопросов
    """

    correct = 0

    for question in final_data:
        if question.is_asked:
            correct += 1

    return correct
