'''
1.1) FAÇA UM PROGRAMA QUE O USUÁRIO INFORME QUANTOS DIAS DE VIDA ELE TEM e o sistema mostre-a expressa em anos, meses e dias de vida.


usando função do python:
import datetime

my_birthdate = datetime.date(1979,3,12)
my_birthtime = datetime.time(6,0)
my_birthday = datetime.datetime.combine(my_birthdate, my_birthtime)
now = datetime.datetime.now()

time_passed = now - my_birthday
how_many_seconds = time_passed.total_seconds()
print how_many_seconds
'''
dias=int(input("Digite quantos dias de vida você tem: "))
anos= dias/365
restoMeses= (dias%365)
meses1=restoMeses/12
restoDias=restoMeses%12

print("%d"% anos, "%d"% meses1, restoDias)
