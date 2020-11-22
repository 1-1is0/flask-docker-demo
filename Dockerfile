FROM python:3.8

WORKDIR /app

RUN apt-get install git && \
	pip install -U pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py"]