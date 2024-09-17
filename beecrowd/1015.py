import math
x1,y1=map(float,input('').split())
x2,y2=map(float,input('').split())
conta=((x2-x1)**2)+((y2-y1)**2)
raiz_quadrada=math.sqrt(conta)
print(f'{raiz_quadrada:.4f}') #OK