"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    
    def compare(text1, text2):
        if (isinstance(text1, str) and isinstance(text2, str)) == False:
            return 0
        elif text1 == text2:
            return 1
        elif text1 != text2 and text2 == "learn":
            return 3
        elif len(text1) > len(text2):
            return 2


    print(compare("Python", 3))
    print(compare("Python", "Python"))
    print(compare("Python 3", "Python"))
    print(compare("Python", "learn"))
    print(compare("Питон", "learn"))
    print(compare("Длинная строка", "123"))
    print(compare("321", "321"))
    print(compare(123, "456"))
    
if __name__ == "__main__":
    main()
