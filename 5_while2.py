"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Привет": "Привет!", "Как дела?": "Нормально", "Что делаешь?": "Программирую",
    "Кофе?": "Чай!", "Много работы?": "Очень", "До свидания!": "До новых встреч!"}

def ask_user(answers_dict):
    while True:
        user_say = input("Задайте вопрос\n")
        if user_say in questions_and_answers.keys():
            print(questions_and_answers.get(user_say))

    
if __name__ == "__main__":
    ask_user(questions_and_answers)
