FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY healthcare_dataset.csv .
COPY migrate.py .
COPY test_migration.py .

# 1. On met à jour pip pour régler les bugs de certificats SSL
RUN pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org

# On remet la commande d'installation normale
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

CMD ["python", "migrate.py"]