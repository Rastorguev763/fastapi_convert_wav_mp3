# Используйте официальный образ Python в качестве базового образа
FROM python:3.9

# Установите FFmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Установите рабочую директорию в контейнере
WORKDIR /app

# Копируйте зависимости проекта в контейнер
COPY requirements.txt .

# Установите зависимости
RUN pip install -r requirements.txt

# Копируйте остальные файлы проекта в контейнер
COPY . .

# Укажите порт, на котором будет работать ваше приложение
EXPOSE 8000

# Запустите приложение при старте контейнера
CMD ["uvicorn", "main_web:app", "--host", "0.0.0.0", "--port", "8000"]
