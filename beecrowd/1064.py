def positivo(n):
    if num>0:
        return True
def media(lista):
    media=sum(lista)/len(lista)
    return media
lista_positivos=[]
for i in range(6):
    num=float(input())
    if positivo(num):
        lista_positivos.append(num)
quant=len(lista_positivos)
resultado=media(lista_positivos)
print(f'{quant} valores positivos')
print(f'{resultado:.1f}')