languages = {'Scala': 'Martin Odersky', 'JavaSript': 'Brendan Eich', 'Python': 'Guido van Rossum', 'PHP': 'Rasmus Lerdorf'}
del languages['Scala']
for k in languages:
    print(f'My favorite programming language is {k}. It was created by {languages[k]}.')




#Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов
#(значення). Виведіть по черзі для усіх елементів словника повідомлення типу 
#My favorite programming language is Python. It was created by Guido van Rossum.. 
#Видаліть, на ваш вибір, одну пару «мова: розробник» із словника. Виведіть словник на екран.