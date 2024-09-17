idade=int(input(''))
ano=idade//365
mes=idade%365
mesf=mes//30
dias=mes%30
print(f'{ano} ano(s)')
print(f'{mesf} mes(es)')
print(f'{dias} dia(s)')
