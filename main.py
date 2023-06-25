import os
from Materi.pertemuan import *
os.system('cls')

menu = ['Pertemuan 1', 'Pertemuan 2', 'Pertemuan 3',
        'Pertemuan 4', 'Pertemuan 5', 'Pertemuan 6']

menus = """MENU:
      1. Lihat Materi
      2. Lihat Tugas
      3. Menu Utama"""

while True: 
  print(50*'=')
  print("\t\tSelamat Datang!")
  print(50*'=')
  print("\t      Aplikasi Pembelajaran")
  print("\t    Algoritma & Pemrograman 2")
  print(50*'=')
  
  print("MENU : ")
  for i, data in enumerate(menu):
    print(f'\t{i+1}. {data}')
    
  print(50*'=')
  pilihMenu = input("Pilih Menu 1-13 [Q:Exit]: ").lower()
  print(50*'=')
  
  if pilihMenu == "1":
    while True:
      print("\t\t  (Pertemuan 1)")
      print("\t     Pengenalan Dasar Python")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan1.soal())
      elif pilihMenus == "2":
        print(Pertemuan1.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
    
  elif pilihMenu == "2":
    while True:
      print("\t\t  (Pertemuan 2)")
      print("\t     Pengenalan Dasar Python")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan2.soal())
      elif pilihMenus == "2":
        print(Pertemuan2.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
      
  elif pilihMenu == "3":
    while True:
      print("\t\t  (Pertemuan 3)")
      print("Python Data Types, Variables, Operators, and Basic I/O Operations")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan3.soal())
      elif pilihMenus == "2":
        print(Pertemuan3.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
      
  elif pilihMenu == "4":
    while True:
      print("\t\t  (Pertemuan 4)")
      print("\t    Output Program pada Python")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan4.soal())
      elif pilihMenus == "2":
        print(Pertemuan4.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')   
      
  elif pilihMenu == "5":
    while True:
      print("\t\t  (Pertemuan 5)")
      print("  Boolean Values, Conditional Execution Continues")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan5.soal())
      elif pilihMenus == "2":
        print(Pertemuan5.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "6":
    while True:
      print("\t\t  (Pertemuan 6)")
      print("\t Loops, Lists and List Processing")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan6.soal())
      elif pilihMenus == "2":
        print(Pertemuan6.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "q":
    os.system('cls')
    quit()
  
  else:
    print("Menu tidak ditemukan!")
    continue