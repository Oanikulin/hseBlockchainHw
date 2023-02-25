FROM python:3.9.16-slim-buster

COPY requiremnts.txt requiremnts.txt

RUN pip install -r requiremnts.txt

COPY solution.py .

CMD ["python", "solution.py"]