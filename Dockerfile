FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt --index-url https://pypi.org/simple
CMD ["python", "main.py"]
