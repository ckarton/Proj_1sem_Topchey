import random #подключаем стороннюю библиотеку
N = random.randrange(0,86400) #назначаем переменную с рандомным значением секунд так как их точное кол-во не указано
print("число секунд:", N) #выводим значение N
m = int(N%60) #назначаем новую переменную которая равна делению N на 60 т.к. нас интересуют только минуты
print("Целые минуты:", m) #выводим переменную m и получаем кол-во целых минут