mediaidade=0
somaidade=0
maioridadehomem=0
nomemaisvelho=""
totmulher20=0
for p in range(1,6):
 print(" {} Pessoa:".format(p))
 nome=str(input("Digite seu nome:")).strip()
 idade=int(input("Digite sua idade"))
 sexo=str(input("Digite seu sexo [S/M]")).strip()
 somaidade=somaidade+idade

 if p ==1 and sexo in "Mm":
      maioridadehomem=idade
      nomemaisvelho=nome
 if sexo in "Mm" and idade>maioridadehomem:
      maioridadehomem=idade
      nomemaisvelho=nome
 if sexo in "Ff" and idade <20:
     totmulher20+=1
mediaidade=somaidade/4
print(" A media da idade do grupo e de {} Anos".format(mediaidade))
print(" O homem mais velho tem {} anos e seu nome é {}".format(idade,nome))
print(" Ao total sâo {} mulheres com menos de 20 anos".format(totmulher20))