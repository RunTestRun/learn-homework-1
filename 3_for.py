"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():

    school = [
        {'school_class': '1a', 'scores': [5,3,5,2,5]}, 
        {'school_class': '2a', 'scores': [5,2,1,4,3]}, 
        {'school_class': '3a', 'scores': [2,4,3,5,5]},
        {'school_class': '4a', 'scores': [5,4,5,4,5]},
        {'school_class': '5a', 'scores': [1,2,3,4,5]}
    ]

    scores_sum = 0
    scores_len = 0
    num = 0

    for score in school:
        scores_sum += sum(school[num]['scores'])
        scores_len += len(school[num]['scores'])
        num += 1

    print(f"Средний балл по всей школе: {scores_sum/scores_len}")

    scores_sum = 0
    num = 0

    for score in school:
        scores_sum = sum(school[num]['scores'])/len(school[num]['scores'])
        print(f"Средний балл по классу {school[num]['school_class']} составляет: {scores_sum}")
        num += 1

if __name__ == "__main__":
    main()
