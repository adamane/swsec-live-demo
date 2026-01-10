# Basisimage für Python
FROM python:3.9-slim

# Arbeitsverzeichnis im Container erstellen
WORKDIR /app

# Abhängigkeiten in die Container-Umgebung kopieren (falls notwendig)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere das Python-Skript in den Container
COPY my_workload.py .

# Standardbefehl, um das Python-Skript auszuführen
CMD ["python3", "my_workload.py"]
