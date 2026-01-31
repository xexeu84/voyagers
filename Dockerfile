FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask google-api-python-client
# Comando para lanzar los 4 bots y el servidor web en paralelo
CMD python app_server.py & python aki_engine.py & python valentina_engine.py & python lukas_engine.py & python business_plan_engine.py
