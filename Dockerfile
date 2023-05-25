# Utiliza una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /src

# Establece el archivo requirements.txt
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el codigo base del proyecto
COPY /app ./app
COPY run.py .

# Expone el puerto 5000 (puerto predeterminado para Flask)
EXPOSE 5000

ENV PYTHONHTTPSVERIFY=0

CMD ["python", "run.py", "--host=0.0.0.0"]