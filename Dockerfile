FROM UBUUNTU:2020
WORKDIR /app



COPY . /app





CMD["python3", "server.py"]
