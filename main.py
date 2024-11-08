import os
import time

# Укажите директорию для обхода
directory = '.'  # текущая директория

visited_dirs = set()  # Множество для отслеживания посещенных директорий

for root, dirs, files in os.walk(directory):
    # Проверяем, является ли директория символической ссылкой
    if os.path.islink(root):
        continue  # Пропускаем символические ссылки

    # Добавляем текущую директорию в множество посещенных
    visited_dirs.add(root)

    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Форматируем время
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

