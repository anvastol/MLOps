# Используем базовый образ Python
FROM python:3.8

# Устанавливаем все необходимые библиотеки
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Копируем файлы проекта
COPY model.py /app/model.py
COPY app.py /app/app.py

# Команда запуска Flask приложения
CMD ["python", "app.py"]