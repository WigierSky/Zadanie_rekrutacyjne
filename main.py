#import FastApi
from  fastapi import FastAPI

#stworzenie instancji dla FastAPI
app = FastAPI()

#otwarcie pliku tekstowego
with open("plik.txt") as f:
    file = f.read()

#stworzenie scieżki dla operacji
@app.get("/data")
def root():
     return{"Informacja z pliku": file}