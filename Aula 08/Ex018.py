from math import radians, sin, cos, tan
a = float(input('Digite o ângulo: '))

print('O seno desse ângulo é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(sin(radians(a)),cos(radians(a)),tan(radians(a))))
