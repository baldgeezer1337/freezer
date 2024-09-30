import itertools
import datetime
from datetime import time

class Pakalpojums:
    Pakalpojuma_kategorija=''
    Pakalpojuma_nosaukums=''
    Pakalpojuma_cena=''
    id_iter=itertools.count()

    def __init__(self, pak_kat=None, pak_nos=None, pak_atl=None, pak_cena=10):
        self.Pakalpojuma_id=next(self.id_iter)+1
        self.Pakalpojuma_kategorija=pak_kat
        self.Pakalpojuma_nosaukums=pak_nos
        self.Pakalpojuma_atlaide=pak_atl
        self.Pakalpojuma_cena_stunda=pak_cena
        self.Laiks_pieejams=True

    def Pakalpojuma_info(self):
        return[
            self.Pakalpojuma_kategorija, self.Pakalpojuma_nosaukums,
            self.Pakalpojuma_atlaide, self.Pakalpojuma_cena_stunda
        ]
    
    def Pakalpojuma_info_print(self):
        print('Pakalpojuma kategorija: ' +str(self.Pakalpojuma_kategorija))
        print('Pakalpojuma nosaukums: ' +str(self.Pakalpojuma_nosaukums))
        print('Pakalpojuma atlaide: ' +str(self.Pakalpojuma_atlaide))
        print('Pakalpojuma cena par stundu: ' +str(self.Pakalpojuma_cena_stunda))
        print('Laiks pieejams: '+str(self.Laiks_pieejams)+'\n')

class Klients:
    Klienta_vaards=''
    Klienta_uzvaards=''
    Klienta_PK=''
    Klienta_tel_numurs=0

    id_iter_kl=itertools.count()

    def __init__(self,_vaards, _uzvaards,_pk,_tel_numurs):
        self.Klienta_id=next(self.id_iter_kl)+1
        self.Klienta_vaards=_vaards
        self.Klienta_uzvaards=_uzvaards
        self.Klienta_PK=_pk
        self.Klienta_tel_numurs=_tel_numurs

    def klienta_info(self):
        return[
            self.Klienta_vaards, self.Klienta_uzvaards,self.Klienta_PK,
            self.Klienta_tel_numurs 
        ]

    def Klienta_info_print(self):
        print('Klienta vards:'+self.Klienta_vaards)
        print('Klienta uzvards:'+self.Klienta_uzvaards)
        print('Klienta personas kods:'+self.Klienta_PK)
        print('Klienta telefons:'+str(self.Klienta_tel_numurs)+'\n')

class Izmantosana:
    Pakalpojuma_saakuma_laiks=0
    Pakalpojuma_beigu_laiks=0
    Pakalpojuma_datums=0
    Izmantosana_cena_stunda=10
    id_Pakalpojums=0
    id_Klients=0

    id_iter_izmantosana=itertools.count()

    def Cena_kopa(self):
        kopeeja_cena=self.Izmantosana_cena_stunda*((
            (self.Pakalpojuma_beigu_laiks - self.Pakalpojuma_saakuma_laiks)
        ))
        return kopeeja_cena
    
    
    def Izmantosana_imfo_print(self):
        print("Pakalpojuma sakuma laiks: " + str(self.Pakalpojuma_saakuma_laiks))
        print("Pakalpojuma beigu laiks: " + str(self.Pakalpojuma_beigu_laiks))
        print("Pakalpojums id: " + str(self.id_Pakalpojums))
        print("Klienta id: " + str(self.id_Klients))
        print("Pakalpojuma cena stunda, EUR: " + str(self.Izmantosana_cena_stunda) + "\n")


pak1=Pakalpojums("Frizētava","Matu griešana","20%",30) 
pak2=Pakalpojums("Uzacu un skropstu krāsošana","Uzacu krāsošana","25%")
pak3=Pakalpojums("Kosmētiskās procedūras","Higiēniskā sejas tīrīšana")

print(pak1.Pakalpojuma_id)
pak1.Pakalpojuma_info()
pak1.Pakalpojuma_info_print()
print(pak2.Pakalpojuma_id)
pak2.Pakalpojuma_info()
pak2.Pakalpojuma_info_print()
print(pak3.Pakalpojuma_id)
pak3.Pakalpojuma_info()
pak3.Pakalpojuma_info_print()

Klients1=Klients('Aija','Zālīte','190490-11490', 29800789)   
Klients2=Klients('Janis','Ozols','030589-11430', 24852789)  
Klients3=Klients('Sintija','Molocko','260998-12215', 20898777)  

print(Klients1.Klienta_id)
Klients1.klienta_info()
Klients1.Klienta_info_print()
print(Klients2.Klienta_id)
Klients2.klienta_info()
Klients2.Klienta_info_print()
print(Klients3.Klienta_id)
Klients3.klienta_info()
Klients3.Klienta_info_print()