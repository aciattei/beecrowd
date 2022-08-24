NAME = str(input())
SALARY = float(input())
SALES = float(input())

TOTAL= SALARY + (SALES*15/100)

print('TOTAL = R$ {:.2f}'.format(TOTAL))