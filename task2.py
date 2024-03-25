import requests
from bs4 import BeautifulSoup 

for i in range(1, 100000):  # Начинаем с 1
    string = 'hacker' * i
    requests.get('http://62.173.140.174:16039/')
    try:
        response = requests.post('http://62.173.140.174:16039/', data={'word': string})
        if response.status_code == 200:  # Проверяем, что статус-код ответа 200 (OK)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            all_text = soup.get_text()
            print(f"Current interation: {i}")
            if 'Something went wrong' not in all_text:  # Исправленное условие
                print(f"Успешно на итерации: {i}")
                break
        else:
            print(f"Ошибка HTTP: {response.status_code} на итерации {i}")
    except Exception as e:
        print(f"Ошибка запроса на итерации {i}: {e}")
