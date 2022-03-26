from functions import form_random_question, set_game_data, read_json, final_points

jsn_questions = read_json("questions.json")
questions = form_random_question(jsn_questions)

# Для записи данных, после игры (отвечен ли вопрос, количество баллов и т.д.)
final_data = []

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
print(f"Вот и все! Отвечено {final_points(final_data)} из {quantity}")
