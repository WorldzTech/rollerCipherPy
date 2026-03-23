# Подготовка окружения: виртуальное окружение и установка requests

Чтобы работать с сервером задания (отправлять запросы на шифрование и расшифровку), вам понадобится библиотека `requests`. Рекомендуется использовать **виртуальное окружение**, чтобы не засорять глобальную установку Python.

### Шаг 1: Проверьте, что Python установлен
Откройте терминал (Command Prompt / PowerShell на Windows, Terminal на macOS/Linux) и выполните:

```bash
python --version
# или
python3 --version
```
Должен отобразиться Python 3.8 или выше. Если нет — скачайте и установите с https://www.python.org/downloads/

### Шаг 2: Создайте папку для проекта
Создайте папку на рабочем столе через VS Code и откройте ее

### Шаг 3: Создайте виртуальное окружение
```bash
# На Windows:
python -m venv venv

# На macOS / Linux:
python3 -m venv venv
```

### Шаг 4: Активируйте виртуальное окружение
```bash
# Windows (Command Prompt):
venv\Scripts\activate

# Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# macOS / Linux:
source venv/bin/activate
```

### Шаг 5: Установите библиотеку requests
```bash
pip install requests
```

### Шаг 6: Пример простого скрипта (можно сохранить как test.py)
```python
import requests

url = "https://roller.worldz.tech/flag"
response = requests.get(url)
print(response.json())  # увидите зашифрованный флаг как список чисел
```