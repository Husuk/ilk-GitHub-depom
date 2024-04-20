import random
elemanlar = ["!","#","-","$","&","+","*"]
def sifre_olustur():
    sifre = ""
    for i in range(10):
        sifre += random.choice(elemanlar)
    return sifre