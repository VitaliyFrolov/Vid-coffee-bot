FROM mirror.gcr.io/library/python:3.12-slim as builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM mirror.gcr.io/library/python:3.12-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY . .

CMD [ "python3", "main.py" ]