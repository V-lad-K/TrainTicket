FROM python:3.11

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]