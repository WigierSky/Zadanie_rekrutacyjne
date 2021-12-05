#używamy bazowego obrazu Pythona
FROM python:latest

#stworzenie folderu roboczego aplikacji
WORKDIR /src

#skopiowanie pliku requirements.txt do folderu roboczego
COPY ./requirements.txt /src/requirements.txt

#instalowanie pakietów z pliku requirements.txt
RUN pip3 install --upgrade -r /src/requirements.txt

#otwarcie portu (aplikacja webowa)
EXPOSE 80

#parametry
CMD ["python", "main.py"]

