x,y=map(int,input().split())
if x==1:
    preço=4.00*y
if x==2:
    preço=4.50*y
if x==3:
    preço=5.00*y
if x==4:
    preço=2.00*y
if x==5:
    preço=1.50*y
print(f'Total: R$ {preço:.2f}')

