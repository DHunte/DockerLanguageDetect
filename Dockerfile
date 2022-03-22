FROM ubuntu:latest as download
WORKDIR /dl
RUN apt-get update -y 
RUN apt-get install -y wget
RUN wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin

FROM python:3.8
WORKDIR /app
COPY requirements.txt requirements.txt
COPY --from=download /dl/lid.176.bin /app/lid.176.bin
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5500
CMD [ "python3", "main.py"]
