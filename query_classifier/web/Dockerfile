# Используем официальный образ Python
FROM python:3.12.4-slim

# Устанавливаем зависимости для работы Flask
RUN pip install --no-cache-dir flask

# Создаем рабочую директорию
WORKDIR /app

# Копируем содержимое локальной директории в контейнер
COPY . .

# Указываем команду для запуска Flask приложения
CMD ["python", "main.py"]
