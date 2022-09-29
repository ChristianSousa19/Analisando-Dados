con=0
soma=0
for cont in range(1,500,2):
    if cont %3==0:
      con=con+1
      soma=soma+cont
print(" a soma dos {} números multilpos tem o resultado {}".format(con,soma))