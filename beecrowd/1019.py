segun=int(input(''))
horas=segun//3600

if horas==0:
    minutos=segun//60
    segundos=segun%60
    print(f'{horas}:{minutos}:{segundos}')
if horas!=0:
    minutos=segun%3600
    mini=minutos//60
    segundos=minutos%60
    print(f'{horas}:{mini}:{segundos}')