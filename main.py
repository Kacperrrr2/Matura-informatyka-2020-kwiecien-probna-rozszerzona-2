#zad.4.1
# wiersze =open('dane4.txt','r')
# tab=[]
# for wiersz in wiersze:
#     tab.append(int(wiersz.strip()))
# min_luka=9999999999
# max_luka=0
# for i in range(len(tab)-1):
#     luka=abs(tab[i]-tab[i+1])
#     if luka>max_luka:
#         max_luka=luka
#     if luka<min_luka:
#         min_luka=luka
# print(f' maxluka: {max_luka} minluka:{min_luka} ')
#zad.4.2
# wiersze =open('dane4.txt','r')
# tab=[]
# luki=[]
# for wiersz in wiersze:
#     tab.append(int(wiersz.strip()))
# min_luka=9999999999
# max_luka=0
# licznik_luk=0
# poczatkowa_wartosc=0
# koncowa_wartosc=0
# poczatkowa_wartosc_max=0
# koncowa_wartosc_max=0
# for i in range(len(tab)-3):
#      if abs(tab[i]-tab[i+1])==abs(tab[i+2]-tab[i+3]):
#          if licznik_luk==0:
#             poczatkowa_wartosc=tab[i]
#          licznik_luk += 1
#      else:
#          koncowa_wartosc=tab[i+1]
#          if licznik_luk>max_luka:
#              max_luka=licznik_luk
#              poczatkowa_wartosc_max=poczatkowa_wartosc
#              koncowa_wartosc_max=koncowa_wartosc
#          licznik_luk=0
# print(f'początkowa {poczatkowa_wartosc_max} koncowa {koncowa_wartosc_max} maksymalna luka {max_luka}')
# Zadanie 4.3
# krotnosc={}
# wiersze =open('dane4.txt','r')
# tab=[]
# for wiersz in wiersze:
#     tab.append(int(wiersz.strip()))
# min_luka=9999999999
# max_luka=0
# for i in range(len(tab)-1):
#     luka=abs(tab[i]-tab[i+1])
#     if luka in krotnosc:
#         krotnosc[luka]+=1
#     else:
#         krotnosc[luka]=1
# print(f'{max(dict.values(krotnosc))}  {max(krotnosc, key=krotnosc.get)}')