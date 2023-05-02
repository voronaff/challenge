FROM python:3.10-alpine

COPY app /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "service_a.py" ]