import os
from pathlib import Path
import re
from datetime import datetime
import random

def get_new_user_greeting():
    """Возвращает случайное приветствие для нового пользователя"""
    new_user_greetings = [
        "🎉 Добро пожаловать в систему! Обнаружен новый студент!",
        "✨ Приветствуем нового участника! Давайте создадим ваш профиль!",
        "🚀 Отличные новости! К нам присоединился новый студент!",
        "👋 Привет! Рады видеть нового студента в системе!",
        "📚 Отлично! Найден новый студент для добавления!",
        "🌟 Добро пожаловать! Начинаем создание вашего отчета!",
        "🤖 Приветствую нового пользователя! Готовы к работе?",
        "🌞 Здравствуйте! Создадим ваш первый отчет по практике!",
        "📖 Добро пожаловать! Начнем заполнение ваших данных!",
        "💻 Отлично! Новый студент в системе! Приступим к созданию файла!"
    ]
    return random.choice(new_user_greetings)

def get_existing_user_greeting(username):
    """Возвращает случайное приветствие для существующего пользователя"""
    existing_user_greetings = [
        f"👋 Рады снова видеть! Студент '{username}' уже существует!",
        f"✅ Отлично! Студент '{username}' уже зарегистрирован в системе!",
        f"📚 Приветствуем возвращение! Студент '{username}' уже есть в базе!",
        f"👍 Отлично! Студент '{username}' уже находится в системе!",
        f"🔍 Найдено! Студент '{username}' уже имеет файл README!",
        f"🎉 С возвращением, {username}! Ваш файл уже существует!",
        f"✨ Привет, {username}! Рады видеть вас снова!",
        f"🚀 Отлично! {username} уже в системе! Продолжаем работу!",
        f"🌟 Здравствуйте, {username}! Ваши данные найдены!",
        f"🤖 Приветствую, {username}! Система готова к работе с вашими файлами!"
    ]
    return random.choice(existing_user_greetings)

def get_general_greeting():
    """Возвращает общее приветствие при запуске программы"""
    general_greetings = [
        "📚 Добро пожаловать в систему управления отчетами по практике!",
        "🎉 Приветствуем в системе автоматизации создания README файлов!",
        "✨ Здравствуйте! Готовы работать с отчетами по практике?",
        "🚀 Система управления студенческими отчетами запущена!",
        "👋 Добро пожаловать! Начнем работу с отчетами!",
        "🌟 Приветствуем в программе для создания учебных отчетов!",
        "🤖 Система готова к работе! Приступим к управлению отчетами!",
        "📖 Добро пожаловать в инструмент для студентов!",
        "💻 Программа для автоматизации учебной документации запущена!",
        "🌞 Добрый день! Готовы создать или найти отчет по практике?"
    ]
    return random.choice(general_greetings)

def find_readme_files():
    """Находит все возможные README файлы в текущей директории"""
    readme_files = []
    possible_names = ['README1.md', 'README2.md', 'READMY1.md', 'READMY2.md', 'ReadMe.md', 'README.md', 'readme.md']
    
    for file_name in possible_names:
        if Path(file_name).exists():
            readme_files.append(file_name)
    
    # Также ищем все файлы с паттерном README_*.md
    for file in Path('.').glob('README_*.md'):
        if file.name not in readme_files:
            readme_files.append(file.name)
    
    return readme_files

def extract_name_from_readme(file_path):
    """Извлекает имя из ФИО в README файле"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Паттерны для поиска ФИО (более специфичные)
            fio_patterns = [
                r'ФИО[:\s\-]+\**([А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+)',
                r'фио[:\s\-]+\**([А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+)',
                r'ФИО[:\s\-]+\**([^\n\r\(\)\[\]]+)',
                r'фио[:\s\-]+\**([^\n\r\(\)\[\]]+)',
            ]
            
            for pattern in fio_patterns:
                match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
                if match:
                    fio = match.group(1).strip()
                    # Очищаем от лишних символов и форматирования
                    fio = re.sub(r'[*_\-:]+', '', fio).strip()
                    fio = re.sub(r'[^А-Яа-яЁё\s]', '', fio).strip()
                    fio_parts = fio.split()
                    
                    if len(fio_parts) >= 3:
                        return fio_parts[1]  # Возвращаем имя (второе слово)
                    elif len(fio_parts) >= 1:
                        return fio_parts[0]  # Возвращаем первое слово
            
            # Дополнительный поиск по общему паттерну ФИО
            general_pattern = r'([А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+)'
            match = re.search(general_pattern, content)
            if match:
                fio = match.group(1).strip()
                fio_parts = fio.split()
                if len(fio_parts) >= 3:
                    return fio_parts[1]
            
            return None
            
    except Exception as e:
        print(f"❌ Ошибка при чтении файла {file_path}: {e}")
        return None

def create_user_metrics_file():
    """Создает новый файл с метриками пользователя"""
    print("\n" + "=" * 60)
    print("📝 СОЗДАНИЕ НОВОГО ФАЙЛА С МЕТРИКАМИ ПОЛЬЗОВАТЕЛЯ")
    print("=" * 60)
    
    # Выводим приветствие для нового пользователя
    print(get_new_user_greeting())
    print("Заполните информацию:\n")
    
    # Запрашиваем данные у пользователя
    group = input("Группа: ").strip()
    fio = input("ФИО (полностью): ").strip()
    practice_type = input("Вид практики: ").strip()
    practice_number = input("Номер практики: ").strip()
    specialty_code = input("Код специальности: ").strip()
    specialty_name = input("Название специальности: ").strip()
    
    # Генерируем имя файла на основе ФИО
    fio_parts = fio.split()
    if len(fio_parts) >= 3:
        filename = f"README_{fio_parts[0]}_{fio_parts[1][0]}{fio_parts[2][0]}.md"
    else:
        filename = f"README_{fio.replace(' ', '_')}.md"
    
    # Проверяем, не существует ли уже такой файл
    counter = 1
    original_filename = filename
    while Path(filename).exists():
        filename = f"{original_filename[:-3]}_{counter}.md"
        counter += 1
    
    # Создаем содержимое файла в формате Markdown
    content = f"""# Отчет по практике

## Метрики студента

- **Группа**: {group}
- **ФИО**: {fio}
- **Вид практики**: {practice_type}
- **Номер практики**: {practice_number}
- **Код специальности**: {specialty_code}
- **Название специальности**: {specialty_name}
"""
    
    # Сохраняем файл
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"\n✅ Файл '{filename}' успешно создан!")
        print(f"📁 Файл содержит все введенные метрики в формате Markdown")
        return filename
    except Exception as e:
        print(f"❌ Ошибка при создании файла: {e}")
        return None

def main():
    """Основная функция с циклом запроса имени"""
    
    # Выводим общее приветствие при запуске
    print(get_general_greeting())
    print("=" * 60)
    print("📚 СИСТЕМА УПРАВЛЕНИЯ ОТЧЕТАМИ ПО ПРАКТИКЕ")
    print("=" * 60)
    
    # Находим все README файлы
    readme_files = find_readme_files()
    
    if not readme_files:
        print("❌ Не найдено ни одного README файла в текущей директории")
        
        # Сразу предлагаем создать новый файл
        new_file = create_user_metrics_file()
        if new_file:
            readme_files = [new_file]
        else:
            return
    
    # Извлекаем имена из всех файлов (убираем дубликаты)
    names_from_files = {}
    unique_names = set()
    
    for file_path in readme_files:
        name = extract_name_from_readme(file_path)
        if name:
            # Проверяем, нет ли уже такого имени
            if name not in unique_names:
                names_from_files[file_path] = name
                unique_names.add(name)
    
    # Если ни одного имени не найдено, сразу создаем файл
    if not names_from_files:
        print("\n❌ Ни в одном файле не найдено подходящее ФИО")
        new_file = create_user_metrics_file()
        if new_file:
            # Перезагружаем список файлов и извлекаем имя из нового файла
            readme_files = find_readme_files()
            name = extract_name_from_readme(new_file)
            if name:
                names_from_files[new_file] = name
        else:
            return
    
    # Бесконечный цикл запроса имени
    while True:
        try:
            print("\nВведите имя для проверки (или 'выход' для завершения):")
            input_name = input(">>> ").strip()
            
            if input_name.lower() in ['выход', 'exit', 'quit', 'q']:
                print("👋 До свидания!")
                break
            
            if not input_name:
                print("⚠️  Пожалуйста, введите имя")
                continue
            
            # Проверяем совпадение с именами из файлов
            matched = False
            for file_path, file_name in names_from_files.items():
                if input_name.lower() == file_name.lower():
                    # Приветствуем существующего пользователя
                    print(get_existing_user_greeting(file_name))
                    print(f"   Имя найдено в файле: {file_path}")
                    matched = True
                    break
            
            if not matched:
                print(f"❌ Имя '{input_name}' не совпадает с именами из файлов")
                print(f"   Доступные имена: {', '.join(names_from_files.values())}")
                
                # Сразу предлагаем создать новый файл
                print("\nПохоже, вы новый пользователь. Давайте создадим файл с вашими метриками.")
                new_file = create_user_metrics_file()
                if new_file:
                    # Добавляем новый файл в список
                    name = extract_name_from_readme(new_file)
                    if name:
                        names_from_files[new_file] = name
                        print(f"✅ Новое имя добавлено: '{name}'")
                        print(f"🎉 Теперь доступные имена: {', '.join(names_from_files.values())}")
                
        except KeyboardInterrupt:
            print("\n👋 Программа завершена по запросу пользователя")
            break
        except Exception as e:
            print(f"❌ Произошла ошибка: {e}")

if __name__ == "__main__":
    main()