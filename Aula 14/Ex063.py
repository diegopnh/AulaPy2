fibo = int(input('Digite quantas sequências de Fibonacci você deseja: '))
num = 0
x = 0
a = 0
b = 1

while num < fibo:
    if num == 0:
        print('0',end = ' ')
    elif num == 1:
        print('1',end = ' ')
    else:
        x = b + a
        print(x, end = " ")
        a = x - a
        b = x
    num += 1