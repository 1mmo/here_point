FROM python:3.9

# рабочай директория внутри проекта
WORKDIR /opt/here-point

# переменные окружения для python
# Python не будет создавать файлы кэша.рус
ENV PYTHONDONTWRITEBYTECODE 1 
# не помещает в буфер потоки stdout и stderr
ENV PYTHONNUNBUFFERED 1

# Устанавливаем зависимости для Postgres
RUN apt-get update \
        && apt-get install -y --no-install-recommends build-essential libffi-dev locales-all

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .
