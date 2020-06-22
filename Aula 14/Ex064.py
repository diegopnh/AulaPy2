contnum = 0
somanum = 0
num = 0

num = int(input('Digite números inteiros (Digite 999 para parar): '))
while num != 999:
    somanum += num
    contnum += 1
    num = int(input('Digite números inteiros (Digite 999 para parar): '))


print('Foram digitados {} números'.format(contnum))
print('A soma dos números é {}'.format(somanum))