# Image slim : petite, basée sur Debian, compatible avec la plupart des paquets Python
FROM python:3.12-slim

WORKDIR /app

# 1) Dépendances d'abord : couche mise en cache tant que requirements.txt ne change pas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) Code ensuite : change souvent, donc en dernier
COPY app.py .

# Utilisateur non-root
RUN adduser --disabled-password --no-create-home appuser
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]