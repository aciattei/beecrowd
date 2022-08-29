x = input().split(' ')
a,b,c = x

maiorAB = (int(a)+int(b)+abs(int(a)-int(b)))/2
resultado = (int(maiorAB)+int(c)+abs(int(maiorAB)-int(c)))/2

print("{} eh o maior".format(round(resultado)))