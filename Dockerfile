#syntax=docker/dockerfile:1

#używamy bazowego obrazu Pythona
FROM python:latest

WORKDIR /REPO

COPY ./requirements.txt /REPO/requirements.txt

RUN pip3 install --upgrade -r /REPO/requirements.txt

EXPOSE 80

CMD ["uvicorn", "--host=0.0.0.0"]

