FROM python:3
WORKDIR /app3
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "school_api.py"] 