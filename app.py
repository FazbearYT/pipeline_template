import os
import sqlite3
import subprocess

# 1. SECRET SCANNING TRIGGER
# Gitleaks ищет паттерны AKIA... (AWS Access Keys)
# Этот ключ не настоящий, но формат сработает как "утечка"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def get_user_data(username):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # 2. SAST TRIGGER (SQL Injection)
    # Semgrep ищет f-строки внутри cursor.execute
    # Это классическая уязвимость CWE-89
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchone()


def process_file(filename):
    # 3. SAST TRIGGER (Command Injection)
    # Semgrep/CodeQL ищут os.system с f-строками или конкатенацией
    # Это позволяет выполнить любой код в системе (CWE-78)
    os.system(f"cat {filename}")

    # Альтернативный вариант, который тоже ловится:
    # subprocess.call(f"ls -la {filename}", shell=True)


if __name__ == "__main__":
    print("Этот файл создан для тестирования CI/CD пайплайна")
    print("В нём заведомо есть уязвимости!")