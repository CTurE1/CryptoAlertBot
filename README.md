# **Крипто-бот для уведомлений о падении цены**

[![Follow me on Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/VadimWright)
[![Discord: @vadimwright](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](@vadimwright)
[![Me on Telegram](https://img.shields.io/badge/Telegram-%235865F2.svg?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Vadim_Wright)


Этот бот отслеживает цены выбранных криптовалют и отправляет уведомления через Telegram, если цена какой-либо из отслеживаемых монет упадет на указанный процент или больше.

## **Настройка:**

1. **Установите необходимые библиотеки:**

   ```
   Copy code
   pip install requests
   ```

2. **Настройте Telegram бота:**

   - Создайте нового бота в Telegram через [@BotFather](https://t.me/botfather).
   - Сохраните токен бота.
   - Напишите своему боту в Telegram, чтобы начать чат.
   - Получите `CHAT_ID` через https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates (замените `YOUR_BOT_TOKEN` на ваш токен).

3. **Настройте скрипт:**

   - Замените `YOUR_TELEGRAM_BOT_TOKEN` на ваш токен Telegram бота.
   - Замените `YOUR_TELEGRAM_CHAT_ID` на ваш `CHAT_ID`.

## **Запуск:**

Просто запустите скрипт:

```
cssCopy code
python main.py
```

## **Кастомизация:**

- **Добавление новых монет для наблюдения:**
  Добавьте идентификаторы монет в список `currencies` в блоке `if __name__ == "__main__":`.
- **Изменение процентного порога уведомления:**
  Измените значение `percentage_drop` в блоке `if __name__ == "__main__":`.