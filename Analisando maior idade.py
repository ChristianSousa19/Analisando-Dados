contm=0
contn=0

for i in range(1,8):
  idade=int(input("Em que ano a {}º pessoa nasceu?".format(i)))
  tot=2022-idade

  if tot<18:
    contm+=1
    print("Menor idade")

  else:
     contn+=1
     print("Maior idade")
print("ao total temos {} pessoa maiores de idade e {} menores de idade".format(contn,contm))
