FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install --default-timeout=100 future

RUN pip install -r ./requirements.txt


ENV ENVIRONMENT production

COPY run.py /main/__init__.py
