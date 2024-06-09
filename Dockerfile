FROM python:3.10-slim

WORKDIR /app

ADD requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# RUN pip install -vvv uvloop

ADD backend backend
ADD main.py main.py

ENV PORT=5000
CMD uvicorn main:app --host 0.0.0.0 --port $PORT

