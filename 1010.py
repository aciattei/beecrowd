linha1 = input().split(' ')
linha2 = input().split(' ')

c1, n1, v1 = linha1
c2, n2, v2 = linha2

TOTAL = float((int(n1) * float(v1)) + (int(n2) * float(v2)))

print('VALOR A PAGAR: R$ {:.2f}'.format(TOTAL))