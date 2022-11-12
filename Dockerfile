FROM python:3
COPY . /app
RUN pip install -r requirements.txt
WORKDIR /app
CMD python school_api.py