a,b,c,d=map(float,input('').split())
soma_1=a+b
soma_2=c+d
if b>c and d>a and soma_2>soma_1 and c>=0 and d>=0 and a%2==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')