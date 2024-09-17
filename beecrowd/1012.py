a,b,c=map(float,input('').split( ))
area_triangulo=a*c/2
pi=3.14159
area_circulo=pi*(c**2)
area_trapezio=(a+b)*c/2 #ok
area_quadrado=b**2
area_retangulo=a*b
print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')