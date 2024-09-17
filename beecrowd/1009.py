nome=input('')
fixo=float(input(''))
vendas=float(input(''))
comicao=0.15
salario=fixo+(vendas*comicao)
print(f'TOTAL = R$ {salario:.2f}')