FROM python:3.11

WORKDIR /code1

COPY requirements.txt /code1/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code1

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]