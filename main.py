from functions import form_random_question, set_game_data, read_json, get_correct_questions_quantity, print_info, \
    get_final_points
import time

jsn_questions = read_json("questions.json")
questions = form_random_question(jsn_questions)

# Для записи данных, после игры (отвечен ли вопрос, количество баллов и т.д.)
final_data = []

print_info()
time.sleep(10)

for idx, question in enumerate(questions):

    print(f"Вопрос {int(idx) + 1}, {question}")

    user_answer = input("Введите Ваш ответ: \n")
    question.set_user_answer(user_answer)

    final_data.append(set_game_data(question))

    # Выбор одного ответа, в случае множественных вариантов
    correct_answer = question.correct_answers[0]
    if question.is_correct():  # Проверка правильности введенного пользователем ответа
        print(f"Ответ верный, получено {question.points} баллов")
    else:
        print(f"Ответ неверный. Верный ответ: {correct_answer}")

quantity = len(final_data)
final_points = get_final_points(final_data)
correct_questions_quantity = get_correct_questions_quantity(final_data)

print(f"""\nВот и все! Вы ответили на {correct_questions_quantity} из {quantity} вопросов
и заработали {final_points} очков!""")
