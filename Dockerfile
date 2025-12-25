# Используем легкий образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Сначала копируем только список зависимостей (для кэширования слоев)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код проекта
COPY . .

# Команда для запуска (замени app.py на свой стартовый файл)
CMD ["python", "app.py"]