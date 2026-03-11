FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY healthcare_dataset.csv .
COPY migrate.py .

# On remet la commande d'installation normale
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

CMD ["python", "migrate.py"]