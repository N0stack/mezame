FROM python:3.5.2

RUN apt update \
    && apt install -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --branch develop https://github.com/N0stack/mezame

WORKDIR /mezame/mezame

RUN pip install -r requirements.freeze

RUN python manage.py makemigrations \
    && python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
