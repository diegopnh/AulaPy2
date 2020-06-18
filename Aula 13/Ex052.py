num = int(input('Digite o seu número: '))
a = 0

for c in range(2,num):
    if num % c == 0:
        a = c + a
    else:
        pass

if num == 1:
    print('Esse número não é primo!')
elif a == 0:
    print('Esse número é primo!')
else:
    print('Esse número não é primo!')
    
 