# 2. Функция на вход получает два произвольных числа.
# Вывести в консоль наибольшее из чисел.
def num_1(a,b):
    if a>=b:
        print(a)
    elif b>=a:
        print(b)
num_1(5,1)


# 3. Функция на вход получает два произвольных числа.
# Вывести в консоль “yes”, если они отличаются друг от друга на 135,
# иначе вывести на экран “No”
def num_2(a,b):
    if a==b+135:
        print('yes')
    elif a==b-135:
        print('yes')
    elif b==a+135:
        print('yes')
    elif b==a-135:
        print('yes')
    else:
        print('no')
num_2(136,1)

# 4. Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень)
def num_3(a):
    if a==12 or a==1 or a==2:
        print('зима')
    elif a in range (3,6):
        print ('весна')
    elif a in range (6,9):
        print ('лето')
    elif a in range (9,12):
        print ('осень')
num_3(12)

# 5. Функция на вход получает три произвольных числа.
# Если все числа больше 10, то вывести на экран “yes”, иначе “no”;
def num_4(a,b,c):
    if a>10 and b>10 and c>10:
        print ('yes')
    else:
        print ('no')

num_4(11,11,9)
