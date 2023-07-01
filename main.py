import os
from Materi.pertemuan import *
os.system('cls')

while True: 
  print(50*'=')
  print(Header.titleUtama)
  print(50*'=')
  
  print("MENU : ")
  for i, data in enumerate(Header.menu):
    print(f'\t{i+1}. {data}')
    
  print(50*'=')
  pilihMenu = input("Pilih Menu 1-13 [Q:Exit]: ").lower()
  
  if pilihMenu == "1":
    os.system('cls')
    while True:
      print(Pertemuan1.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
    
  elif pilihMenu == "2":
    os.system('cls')
    while True:
      print(Pertemuan2.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
      
  elif pilihMenu == "3":
    os.system('cls')
    while True:
      print(Pertemuan3.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
      
  elif pilihMenu == "4":
    os.system('cls')
    while True:
      print(Pertemuan4.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')   
      
  elif pilihMenu == "5":
    os.system('cls')
    while True:
      print(Pertemuan5.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "6":
    os.system('cls')
    while True:
      print(Pertemuan6.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "7":
    os.system('cls')
    while True:
      print(Pertemuan7.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "8":
    os.system('cls')
    while True:
      print(Pertemuan8.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "9":
    os.system('cls')
    while True:
      print(Pertemuan9.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "10":
    os.system('cls')
    while True:
      print(Pertemuan10.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "11":
    os.system('cls')
    while True:
      print(Pertemuan11.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "12":
    os.system('cls')
    while True:
      print(Pertemuan12.menu())
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
        os.system('cls')
        print(50*'=')
        print("Menu tidak ditemukan!")
        continue
      print(50*'-')
  
  elif pilihMenu == "13":
    os.system('cls')
    while True:
      print(Pertemuan13.menu())
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
        os.system('cls')
        print(50*'=')
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