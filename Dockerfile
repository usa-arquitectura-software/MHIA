# Usa una imagen base de Python 3.10
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copia y instala las dependencias
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia todo el código fuente dentro del contenedor
COPY . /code

# Comando para ejecutar FastAPI con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
