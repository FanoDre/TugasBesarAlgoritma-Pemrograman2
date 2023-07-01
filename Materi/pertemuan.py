import webbrowser


class Header():
  title = (
            ("[+] Pertemuan 1", "[+] Pengenalan Dasar Python"),
            ("[+] Pertemuan 2", "[+] Pengenalan Dasar Python 2"),
            ("[+] Pertemuan 3", "[+] Python Data Types, Variables, Operators"),
            ("[+] Pertemuan 4", "[+] Output Program pada Python"),
            ("[+] Pertemuan 5", "[+] Boolean Values, Conditional Execution Continues"),
            ("[+] Pertemuan 6", "[+] Loops, Lists and List Processing"),
            ("[+] Pertemuan 7", "[+] Pra UTS"),
            ("[+] Pertemuan 8", "[+] UTS"),
            ("[+] Pertemuan 9", "[+] Prosedur"),
            ("[+] Pertemuan 10", "[+] Fungsi dan Parameter"),
            ("[+] Pertemuan 11", "[+] Array Manipulation: Sorting dan Searching"),
            ("[+] Pertemuan 12", "[+] Exceptions dan Data Processing"),
            ("[+] Pertemuan 13", "[+] Struktur Data List")
          )
  
  titleUtama = """                  Selamat Datang!
  Aplikasi Pembelajaran Algoritma & Pemrograman 2"""

  menu = [' Pertemuan 1', ' Pertemuan 2', ' Pertemuan 3',
        ' Pertemuan 4', ' Pertemuan 5', ' Pertemuan 6',
        ' Pertemuan 7', ' Pertemuan 8', ' Pertemuan 9', 
        'Pertemuan 10', 'Pertemuan 11', 'Pertemuan 12',
        'Pertemuan 13']

  menus = """MENU:
      1. Lihat Materi
      2. Lihat Tugas
      3. Menu Utama"""


class Pertemuan1():
  def menu():
    print(50*'=')
    print(Header.title[0][0])
    print(Header.title[0][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://docs.google.com/presentation/d/1EJvzcJguja5QW93CDL11z4UCCoqhglax/edit#slide=id.p4'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "Belum ada tugas di Pertemuan 1"

class Pertemuan2():
  def menu():
    print(50*'=')
    print(Header.title[1][0])
    print(Header.title[1][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://docs.google.com/presentation/d/1DnPPbiXLGKtH9NKSfNE480bOOdTgUNjZ/edit#slide=id.p1'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "Belum ada tugas di Pertemuan 2"

class Pertemuan3():
  def menu():
    print(50*'=')
    print(Header.title[2][0])
    print(Header.title[2][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://docs.google.com/presentation/d/1HrdjC5wa322m8w3wzQhoY7gwbYfwn3F1/edit#slide=id.p1'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "Belum ada tugas di Pertemuan 3"
  
class Pertemuan4():
  def menu():
    print(50*'=')
    print(Header.title[3][0])
    print(Header.title[3][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://docs.google.com/presentation/d/1WRg4ECmmL-d-A7peoUrBfp7f79C1KVF5/edit#slide=id.p1'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "Belum ada tugas di Pertemuan 4"

class Pertemuan5():
  def menu():
    print(50*'=')
    print(Header.title[4][0])
    print(Header.title[4][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://docs.google.com/presentation/d/17MzdN701NeVnfeV_OVlvIkqizK1TLV8w/edit#slide=id.p1'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "Belum ada tugas di Pertemuan 5"

class Pertemuan6():
  def menu():
    print(50*'=')
    print(Header.title[5][0])
    print(Header.title[5][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  
  def soal():
    url = 'https://docs.google.com/presentation/d/1WzRP3NYJpLjS6yL_JvX6scHKM-BpiNMg/edit#slide=id.p1'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "Belum ada tugas di Pertemuan 6"

class Pertemuan7():
  def menu():
    print(50*'=')
    print(Header.title[6][0])
    print(Header.title[6][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://drive.google.com/drive/folders/1DKjopSv_6Ardf0KBkbTD4nzTD0LeDHL7?usp=sharing'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "Belum ada tugas di Pertemuan 7"
  
  
class Pertemuan8():
  def menu():
    print(50*'=')
    print(Header.title[7][0])
    print(Header.title[7][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://drive.google.com/drive/folders/10EFGudAzJqRTWP8fxjfXRWA1hDj5sb5z?usp=sharing'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "Belum ada tugas di Pertemuan 8"
  
  
class Pertemuan9():
  def menu():
    print(50*'=')
    print(Header.title[8][0])
    print(Header.title[8][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://docs.google.com/presentation/d/1kuUJ_5uvXuQJgQEq2ukCkIzMxHStTBwe/edit?rtpof=true&sd=true'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "9"
  
class Pertemuan10():
  def menu():
    print(50*'=')
    print(Header.title[9][0])
    print(Header.title[9][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://docs.google.com/presentation/d/10iJvb04ifrSuhQp9Pkh5OfB1uzSq0sa6/edit'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "10"
  
class Pertemuan11():
  def menu():
    print(50*'=')
    print(Header.title[10][0])
    print(Header.title[10][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://docs.google.com/presentation/d/1tBn4hqI6i9mx_GttrMo2hgVmf0E5bZb1/edit?rtpof=true&sd=true'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "11"
  
class Pertemuan12():
  def menu():
    print(50*'=')
    print(Header.title[11][0])
    print(Header.title[11][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://docs.google.com/presentation/d/1_PQ9iy1M_K1kYOiXq2OG4aHQrD78XtcH/edit#slide=id.p1'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "12"
  
class Pertemuan13():
  def menu():
    print(50*'=')
    print(Header.title[12][0])
    print(Header.title[12][1])
    print(50*'-')
    print(Header.menus)
    return 50*'-'
  
  def soal():
    url = 'https://docs.google.com/presentation/d/1JWq9wcUBtHs8YGhNDlz5499SB0wAoR0C/edit'
    urlOpen = webbrowser.open_new_tab(url)
    return urlOpen
  
  def tugas():
    return "13"
  
  