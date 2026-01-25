FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip3 install pip==25.3.0

COPY requirements/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /code

COPY src .

EXPOSE 4000

CMD ["chalice", "local", "--host=0.0.0.0", "--port=4000"]
