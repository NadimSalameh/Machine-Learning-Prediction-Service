FROM python:3.9.7

ADD ./ flaskapp

WORKDIR /flaskapp

RUN pip install -r requirements.txt

CMD ["python","app.py"]