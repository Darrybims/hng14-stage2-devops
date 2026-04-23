FROM python:3.12-slim

RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

USER appuser

HEALTHCHECK CMD python -c "print('ok')" 

CMD ["python", "worker.py"]

