maior=0
menor=0
for i in range(1,8):
 peso=float(input("Digite o peso da {}º pessoa:".format(i)))
 if i ==1:
   maior=peso
   menor=peso
 else:
  if peso>maior:
     maior=peso
  if peso<menor:
     menor=peso
print("O maior valor lido foi : {} kg".format(maior))
print("E menor peso lido foi: {} kg".format(menor))