FROM python:3.8

LABEL org.opencontainers.image.source https://github.com/arcweld/azure-flask-container-app

COPY ./requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN pip install -r requirements.txt

COPY webapp/* /webapp

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
