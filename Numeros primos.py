num=int(input("Digite um numero:"))
tot=0
for c in range(1,num+1):
    if num %c==0:
        tot+=1
        print("\033[33m",end='')
    else:
         print("\033[31m",end='')
    print(c)
print("O numero {} foi divisivel {} vezees".format(num,tot))
if tot==2:
    print("Portanto ele é um numero  primo")
else:
    print("Portanto ele nâo e um numero primo")