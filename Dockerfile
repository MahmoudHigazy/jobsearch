FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install pipenv
RUN pipenv install
EXPOSE 8000
RUN pipenv run python manage.py makemigrations
RUN pipenv run python manage.py migrate
CMD ["pipenv", "run","python", "manage.py", "runserver", "0.0.0.0:8000"]
