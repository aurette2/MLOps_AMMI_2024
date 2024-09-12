FROM python:3.12.6

WORKDIR /app

COPY . /app

# Install any dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && python model_training.py

EXPOSE 8000

# CMD ["python","model_training.py"]

CMD ["fastapi", "dev", "main.py"]
