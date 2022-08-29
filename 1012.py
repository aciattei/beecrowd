ABC = input().split(' ')
a, b, c = ABC
PI = 3.14159

TRIANGULO = (float(a)*float(c))/2
CIRCULO = PI*(float(c)**2)
TRAPEZIO = ((float(a)+float(b))*float(c))/2
QUADRADO = float(b)*float(b)
RETANGULO = float(a)*float(b)

print('TRIANGULO: {:.3f}'.format(TRIANGULO))
print('CIRCULO: {:.3f}'.format(CIRCULO))
print('TRAPEZIO: {:.3f}'.format(TRAPEZIO))
print('QUADRADO: {:.3f}'.format(QUADRADO))
print('RETANGULO: {:.3f}'.format(RETANGULO))