#docker run -it -p 8000:8000 app
FROM python:3.10-buster

WORKDIR /var/app

# ARG - для этапа сборки
# ENV - на этапе выполнения

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .


CMD uvicorn main:app --host=0.0.0.0 --port=8000
