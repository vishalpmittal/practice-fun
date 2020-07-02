FROM python:3
ENV PYTHONUNBUFFERED 1
ADD . /atomwise-app
WORKDIR /atomwise-app
RUN pip install "Django==3.0.4"
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
