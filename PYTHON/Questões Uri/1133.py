valor=int(input())
valor1=int(input())
minimo=0
maximo=0
contagem=int(0)
if valor>valor1:
  minimo=valor1
  maximo=valor
else:
  maximo=valor1
  minimo=valor

for cont in range(minimo+1, maximo, 1):
  if(cont%5)==2 or (cont%5)==3:
    print(cont)