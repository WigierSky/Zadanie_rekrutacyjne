#import FastApi
from  fastapi import FastAPI

#stworzenie instancji dla FastAPI
app = FastAPI()

#otwarcie pliku tekstowego
file = open("plik.txt")
text = ""

#zczytanie danych z pliku tekstowego i zapisanie ich
for file_x in file.readlines():
    text += " " + file_x.strip()

#stworzenie scieżki dla operacji
@app.get("/data")

#definicja funkcji operacji zwracającą tekst z pliku
def root():
     return{"Informacja z pliku": text}