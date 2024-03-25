import requests

# URL веб-приложения, куда будет отправлен запрос.
url = 'http://62.173.140.174:16039/'

# Начальное значение для тестирования
initial_payload = 'hacker'

# Функция для отправки POST-запроса
def send_request(payload):
    # Кодирование данных для POST-запроса
    data = {'word': payload}
    # Отправка POST-запроса
    response = requests.post(url, data=data)
    # Возвращаем текст ответа
    return response.text

# Основной цикл отправки запросов
for i in range(1, 10):  # Предположим, что мы хотим попробовать до 10 повторений
    # Создаем полезную нагрузку с повторяющимся словом "hacker"
    payload = initial_payload * i
    print(f"Отправка: {payload}")
    response = send_request(payload)
    print(f"Ответ: {response}")
