from flask import Flask
import random
from sifre_olusturucu import sifre_olustur
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<a href = '/sifre'>YENİ ŞİFRE OLUŞTUR</a>"
liste = ["armut","elma","portakal","greyfurt","nar","muz","mandalina","kiraz","şeftali","kayısı"]
@app.route("/husuk")
def husuk():
    kelime = random.choice(liste)
    return f"<a href = '/'>{kelime}</a></h1>"

@app.route("/sifre")
def sifre():
    a = sifre_olustur()
    return f"<h1>{a}</h1><a href = '/'>BAŞKA ŞİFRE</a>"
app.run(debug=True)
 