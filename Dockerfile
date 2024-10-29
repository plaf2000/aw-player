FROM python:3.12.7-bookworm


WORKDIR /app
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]