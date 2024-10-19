FROM python:3.12-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY cat_breeder .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "cat_breeder.asgi:application", "--host", "0.0.0.0", "--port", "8000"]