import requests
import time

TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"


class CryptoAlertBot:
    def __init__(self, currencies, percentage_drop):
        self.currencies = currencies
        self.percentage_drop = percentage_drop
        self.last_prices = {currency: None for currency in currencies}

    def get_current_price(self, currency):
        api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={currency}&vs_currencies=usd"
        response = requests.get(api_url)
        response_data = response.json()
        return response_data[currency]['usd']

    def send_telegram_message(self, message):
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }
        requests.post(telegram_url, data=payload)

    def monitor_prices(self):
        while True:
            for currency in self.currencies:
                current_price = self.get_current_price(currency)

                if self.last_prices[currency]:
                    percentage_change = ((self.last_prices[currency] - current_price) / self.last_prices[
                        currency]) * 100
                    if percentage_change >= self.percentage_drop:
                        message = f"Цена {currency} упала на {percentage_change:.2f}%! Текущая цена: ${current_price}"
                        self.send_telegram_message(message)

                self.last_prices[currency] = current_price
                time.sleep(30)  # Задержка между проверкой разных монет.
            time.sleep(60)  # Задержка между циклами проверки.


if __name__ == "__main__":
    currencies = ["bitcoin", "ethereum", "ripple"]  # Список монет для наблюдения.
    percentage_drop = 5.0  # Уведомлять, если цена упала на 5% или больше.

    bot = CryptoAlertBot(currencies, percentage_drop)
    bot.monitor_prices()
