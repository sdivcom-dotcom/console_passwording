import requests
import time

# Указываем адрес и порт, на которых запущен T-Rex
trex_host = 'localhost'
trex_port = 4500

# Формируем URL для получения статистики T-Rex
stats_url = f'http://{trex_host}:{trex_port}/stats'

# Определяем интервал времени для сбора статистики (в секундах)
interval = 1

# Бесконечный цикл сбора статистики
while True:
    try:
        # Отправляем запрос на получение статистики T-Rex
        response = requests.get(stats_url)

        # Проверяем успешность запроса
        if response.status_code == 200:
            stats = response.json()
            # Извлекаем интересующую нас статистику, например, пропускную способность
            throughput = stats['total']['tx_bps']
            print(f'Throughput: {throughput} bps')

        else:
            print(f'Error: {response.status_code} - {response.text}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

    # Задержка перед следующим запросом на сбор статистики
    time.sleep(interval)