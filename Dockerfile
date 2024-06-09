FROM python:3.11
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["fastapi", "run", "main.py"]