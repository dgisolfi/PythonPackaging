FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt \
    && pip3 install connexion[swagger-ui]

COPY . /usr/src/app

EXPOSE 8012

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]