cont=0
soma=0
for i in range(1,7):
    num=int(input("Digite um numero inteiro"))
    if num %2==0:
      soma = soma + num

print("A soma dos numeros pares e igual a {}".format(soma))
