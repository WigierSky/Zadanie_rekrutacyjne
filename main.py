#import FastApi
from  fastapi import FastAPI

#stworzenie instancji dla FastAPI
app = FastAPI()

#otwarcie pliku tekstowego i odczytanie danych
with open("file.txt") as f:
    file = f.read()

#stworzenie dekoratora oraz funkcji
@app.get("/data")
def root():
     return{"Informacja z pliku": file}
