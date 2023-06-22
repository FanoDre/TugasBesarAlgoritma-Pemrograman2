import os
os.system('cls')

menu = ['Pertemuan 1', 'Pertemuan 2', 'Pertemuan 3',
        'Pertemuan 4', 'Pertemuan 5']

print(50*'=')
print("\t\tSelamat Datang!")
print(50*'=')
print("\t      Aplikasi Pembelajaran")
print("\t    Algoritma & Pemrograman 2")

  
while True: 
  print(50*'=')
  print("MENU : ")
  for i, data in enumerate(menu):
    print(f'\t{i+1}. {data}')
  print(50*'=')
  pilihMenu = input("Pilih Menu diatas:  ")
  print(50*'-')
  if pilihMenu == "1":
    print("Pertemuan 1")
    
  elif pilihMenu == "2":
    from Pertemuan2 import *
    print(pertemuan2.tugas())
    
  elif pilihMenu == "3":
    from Pertemuan3 import *
    print(pertemuan3.tugas())
    
  elif pilihMenu == "4":
    from Pertemuan4 import *
    print(pertemuan4.tugas())
    
  elif pilihMenu == "5":
    from Pertemuan5 import *
    print(pertemuan5.tugas())
    
  else:
    break