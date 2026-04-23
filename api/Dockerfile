FROM python:3.12-alpine

# Alpine's equivalent to apt-get install curl
RUN apk add --no-cache curl

# Add user (Note: Alpine adduser syntax is different)
RUN adduser -D appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER appuser

HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
