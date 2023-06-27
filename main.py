import os
from Materi.pertemuan import *
os.system('cls')

menu = [' Pertemuan 1', ' Pertemuan 2', ' Pertemuan 3',
        ' Pertemuan 4', ' Pertemuan 5', ' Pertemuan 6',
        ' Pertemuan 7', ' Pertemuan 8', ' Pertemuan 9', 
        'Pertemuan 10', 'Pertemuan 11', 'Pertemuan 12',
        'Pertemuan 13']

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
  
  if pilihMenu == "1":
    while True:
      os.system('cls')
      print(50*'=')
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
      os.system('cls')
      print(50*'=')
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
      os.system('cls')
      print(50*'=')
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
      os.system('cls')
      print(50*'=')
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
      os.system('cls')
      print(50*'=')
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
      os.system('cls')
      print(50*'=')
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
  
  elif pilihMenu == "7":
    while True:
      os.system('cls')
      print(50*'=')
      print("\t\t  (Pertemuan 7)")
      print("\t\t     Pra UTS")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan7.soal())
      elif pilihMenus == "2":
        print(Pertemuan7.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "8":
    while True:
      os.system('cls')
      print(50*'=')
      print("\t\t  (Pertemuan 8)")
      print("\t\t       UTS")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan8.soal())
      elif pilihMenus == "2":
        print(Pertemuan8.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "9":
    while True:
      os.system('cls')
      print(50*'=')
      print("\t\t  (Pertemuan 9)")
      print("\t\t    Prosedur")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan9.soal())
      elif pilihMenus == "2":
        print(Pertemuan9.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "10":
    while True:
      os.system('cls')
      print(50*'=')
      print("\t\t  (Pertemuan 10)")
      print("\t\tFungsi dan Parameter")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan10.soal())
      elif pilihMenus == "2":
        print(Pertemuan10.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "11":
    while True:
      os.system('cls')
      print(50*'=')
      print("\t\t  (Pertemuan 11)")
      print("    Array Manipulation: Sorting dan Searching")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan11.soal())
      elif pilihMenus == "2":
        print(Pertemuan11.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "12":
    while True:
      os.system('cls')
      print(50*'=')
      print("\t\t  (Pertemuan 12)")
      print("\t   Exceptions dan Data Processing")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan12.soal())
      elif pilihMenus == "2":
        print(Pertemuan12.tugas())
      elif pilihMenus == "3":
        os.system('cls')
        break
      else:
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "13":
    while True:
      os.system('cls')
      print(50*'=')
      print("\t\t  (Pertemuan 13)")
      print("\t\tStruktur Data List")
      print(50*'-')
      print(menus)
      print(50*'-')
      pilihMenus = input("Pilih Menu: ")
      print(50*'-')
      if pilihMenus == "1":
        print(Pertemuan13.soal())
      elif pilihMenus == "2":
        print(Pertemuan13.tugas())
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
    os.system('cls')
    print("Menu tidak ditemukan!")
    continue