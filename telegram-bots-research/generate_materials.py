#!/usr/bin/env python3
"""
Скрипт для генерации маркетинговых материалов для Telegram-ботов
"""

import os
from pathlib import Path

# Конфигурация ботов
BOTS = [
    {
        "id": "02-AI-Master-AI-BOT",
        "name": "Master AI BOT",
        "github": "yesbhautik/Master-AI-BOT",
        "tagline": "Безлимитный доступ к GPT-4 Turbo и DALL·E 2",
        "description": "Мощный AI-бот с неограниченными запросами и генерацией изображений",
        "category": "AI",
        "price": "$7.99/месяц"
    },
    {
        "id": "03-AI-Telegrad",
        "name": "Telegrad",
        "github": "eyalzk/telegrad",
        "tagline": "Мониторинг ML экспериментов через Telegram",
        "description": "Контролируйте обучение нейросетей прямо из мессенджера",
        "category": "AI/ML",
        "price": "$14.99/месяц"
    },
    {
        "id": "04-Crypto-Wallet-Tracker",
        "name": "CryptoWallet Bot",
        "github": "alberto-rota/CryptoWallet-TelegramBot",
        "tagline": "Отслеживание криптопортфеля с умными алертами",
        "description": "Получайте уведомления о резких изменениях цен ваших активов",
        "category": "Crypto",
        "price": "$4.99/месяц"
    },
    {
        "id": "05-Crypto-EazeBot",
        "name": "EazeBot",
        "github": "MarcelBeining/EazeBot",
        "tagline": "Автоматизация криптовалютной торговли",
        "description": "Создавайте торговые стратегии и исполняйте их автоматически",
        "category": "Crypto Trading",
        "price": "$19.99/месяц + комиссия"
    },
    {
        "id": "06-Crypto-Wallet-Tracker",
        "name": "Wallet Tracker",
        "github": "dorukyy/telegram-wallet-tracker",
        "tagline": "Мониторинг кошельков всех блокчейнов",
        "description": "Bitcoin, Ethereum, Solana - все в одном боте",
        "category": "Crypto",
        "price": "$3.99/месяц"
    },
    {
        "id": "07-Ecommerce-Greed",
        "name": "Greed Shop Bot",
        "github": "Steffo99/greed",
        "tagline": "Ваш магазин в Telegram за 5 минут",
        "description": "Многоязычное e-commerce решение с поддержкой платежей",
        "category": "E-commerce",
        "price": "$29.99/месяц или 2% с продаж"
    },
    {
        "id": "08-Ecommerce-Stripe-Bot",
        "name": "Stripe Store Bot",
        "github": "levklon/ecommerce_telegram_bot",
        "tagline": "E-commerce с Stripe интеграцией",
        "description": "Принимайте платежи безопасно через Stripe",
        "category": "E-commerce",
        "price": "$24.99/месяц"
    },
    {
        "id": "09-Social-Media-Downloader",
        "name": "Universal Media Downloader",
        "github": "Krxuv/Social-Media-Downloader",
        "tagline": "7 соцсетей - 1 бот",
        "description": "YouTube, Spotify, TikTok, Instagram, Facebook, Twitter, Pinterest",
        "category": "Social Media",
        "price": "$2.99/месяц для HD"
    },
    {
        "id": "10-Social-Vidzilla",
        "name": "Vidzilla",
        "github": "zerox9dev/Vidzilla",
        "tagline": "Загрузчик видео из любой соцсети",
        "description": "Скачивайте видео в высоком качестве без ограничений",
        "category": "Social Media",
        "price": "$1.99/месяц"
    },
    {
        "id": "11-Music-Downloader",
        "name": "Music Downloader Pro",
        "github": "LeninInLoop/MusicDownloader-Telegram-Bot",
        "tagline": "Spotify и YouTube в вашем кармане",
        "description": "Скачивайте музыку, распознавайте треки, получайте тексты",
        "category": "Music",
        "price": "$3.99/месяц"
    },
    {
        "id": "12-Music-FallenMusic",
        "name": "FallenMusic",
        "github": "AnonymousX1025/FallenMusic",
        "tagline": "Музыка в голосовых чатах Telegram",
        "description": "Превратите ваш чат в музыкальную комнату",
        "category": "Music",
        "price": "$4.99/месяц для групп"
    },
    {
        "id": "13-Cloud-Pentaract",
        "name": "Pentaract Cloud",
        "github": "Dominux/Pentaract",
        "tagline": "Безлимитное облачное хранилище",
        "description": "Используйте Telegram как бесплатное облако",
        "category": "Cloud Storage",
        "price": "Бесплатно / $2.99 Premium"
    },
    {
        "id": "14-Cloud-Telegram-Upload",
        "name": "Telegram Upload CLI",
        "github": "Nekmo/telegram-upload",
        "tagline": "Загрузка файлов до 4GB через CLI",
        "description": "Автоматизируйте загрузку больших файлов",
        "category": "Cloud Storage",
        "price": "Open source / $9.99 Pro"
    },
    {
        "id": "15-Monitor-Nodejumper",
        "name": "Server Monitor Pro",
        "github": "nodejumper-org/monitoring-tool",
        "tagline": "Мониторинг серверов и validator nodes",
        "description": "Получайте алерты о проблемах сервера мгновенно",
        "category": "Monitoring",
        "price": "$14.99/месяц"
    },
    {
        "id": "16-Monitor-ServerStats",
        "name": "ServerStatsBot",
        "github": "geekbeard/ServerStatsBot",
        "tagline": "Статистика сервера в реальном времени",
        "description": "CPU, RAM, Disk, Network - всё под контролем",
        "category": "Monitoring",
        "price": "$9.99/месяц"
    },
    {
        "id": "17-RSS-Reader",
        "name": "Smart RSS Reader",
        "github": "Rongronggg9/RSS-to-Telegram-Bot",
        "tagline": "Читайте новости красиво",
        "description": "RSS-ридер с лучшим форматированием",
        "category": "RSS/News",
        "price": "$1.99/месяц"
    },
    {
        "id": "18-CRM-Personal",
        "name": "Personal CRM Bot",
        "github": "vicgalle/personalCRMbot",
        "tagline": "Управляйте отношениями эффективно",
        "description": "Персональный CRM для networking профессионалов",
        "category": "CRM",
        "price": "$6.99/месяц"
    },
    {
        "id": "19-Education-TA-BOT",
        "name": "TA-BOT",
        "github": "Amirparsa-Sal/TA-BOT",
        "tagline": "Ваш цифровой ассистент преподавателя",
        "description": "Управление домашними заданиями, оценками и коммуникацией",
        "category": "Education",
        "price": "$99/месяц для учебных заведений"
    },
    {
        "id": "20-Quiz-Quizly",
        "name": "Quizly AI",
        "github": "ShahbazCoder1/QuizBot",
        "tagline": "Квизы на любую тему с AI",
        "description": "Генерация вопросов через Gemini AI",
        "category": "Entertainment",
        "price": "$2.99/месяц"
    }
]

def generate_promo_site(bot):
    """Генерирует промо-сайт для бота"""
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{bot['name']} - {bot['tagline']}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6; color: #333;
        }}
        .hero {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; padding: 80px 20px; text-align: center;
        }}
        .hero h1 {{ font-size: 3em; margin-bottom: 20px; }}
        .hero p {{ font-size: 1.3em; margin-bottom: 30px; }}
        .cta-button {{
            display: inline-block; background: white; color: #667eea;
            padding: 15px 40px; border-radius: 50px; text-decoration: none;
            font-weight: bold; font-size: 1.2em; transition: all 0.3s;
        }}
        .cta-button:hover {{ transform: translateY(-3px); box-shadow: 0 10px 25px rgba(0,0,0,0.2); }}
        .features {{ padding: 60px 20px; max-width: 1200px; margin: 0 auto; }}
        .features h2 {{ text-align: center; font-size: 2.5em; margin-bottom: 40px; }}
        .footer {{ background: #2d3748; color: white; text-align: center; padding: 40px 20px; }}
    </style>
</head>
<body>
    <section class="hero">
        <h1>{bot['name']}</h1>
        <p>{bot['tagline']}</p>
        <p>{bot['description']}</p>
        <a href="https://t.me/yourbot" class="cta-button">Начать использовать</a>
    </section>

    <section class="features">
        <h2>Категория: {bot['category']}</h2>
        <p style="text-align: center; font-size: 1.2em;">GitHub: {bot['github']}</p>
        <p style="text-align: center; font-size: 1.5em; margin-top: 20px; color: #667eea;">
            <strong>{bot['price']}</strong>
        </p>
    </section>

    <footer class="footer">
        <p>&copy; 2025 {bot['name']}. Все права защищены.</p>
    </footer>
</body>
</html>"""

def generate_email_welcome(bot):
    """Генерирует приветственное email"""
    return f"""# Email 1: Приветственное письмо - {bot['name']}

**Тема:** Добро пожаловать в {bot['name']}! 🚀

---

Привет!

Спасибо, что присоединились к **{bot['name']}** — {bot['tagline'].lower()}.

## Что вы получаете:

{bot['description']}

## Специальное предложение

**7 дней бесплатно** для всех новых пользователей!

➡️ [Активировать пробный период](https://t.me/yourbot?start=trial)

## Следующие шаги:

1. Активируйте пробный период
2. Попробуйте основные функции
3. Оцените результат

Цена после пробного периода: **{bot['price']}**

GitHub: {bot['github']}

С уважением,
Команда {bot['name']}
"""

def generate_email_value(bot):
    """Генерирует письмо о ценности"""
    return f"""# Email 2: Демонстрация ценности - {bot['name']}

**Тема:** Как {bot['name']} экономит 10+ часов в неделю

---

Привет!

Сегодня расскажу, как {bot['name']} помогает пользователям достигать больше.

## Проблема

{bot['description']} - это именно то, что нужно современным пользователям.

## Решение: {bot['name']}

Категория: {bot['category']}
GitHub: {bot['github']}

## Результаты

Пользователи экономят:
- ✅ Время
- ✅ Деньги
- ✅ Нервы

## Готовы попробовать?

➡️ [Начать бесплатно](https://t.me/yourbot?start=trial)

Всего **{bot['price']}** после пробного периода.

С уважением,
Команда {bot['name']}
"""

def generate_email_urgency(bot):
    """Генерирует письмо со срочностью"""
    # Обработка цены со скидкой
    try:
        price_value = float(bot['price'].replace('$', '').split('/')[0].strip())
        discount_price = f"${price_value * 0.7:.2f}/месяц"
        price_text = f"""Обычная цена: {bot['price']}
Со скидкой 30%: {discount_price}"""
    except (ValueError, AttributeError):
        price_text = f"Специальная цена: {bot['price']}"

    return f"""# Email 3: Создание срочности - {bot['name']}

**Тема:** [Последний день] Специальное предложение для {bot['name']} ⏰

---

Привет!

Это последнее напоминание о нашей специальной акции.

## Специальная цена

{price_text}

**Через 24 часа акция закончится.**

## Что вы получаете:

{bot['description']}

Категория: {bot['category']}
Open Source: {bot['github']}

## Не упустите шанс!

➡️ [Активировать скидку сейчас](https://t.me/yourbot?start=discount)

## Гарантия возврата

30 дней - полный возврат денег, без вопросов.

С уважением,
Команда {bot['name']}

---

P.S. После 24 часов цена вернется к обычной.
"""

def generate_lead_magnet(bot):
    """Генерирует лид-магнит"""
    return f"""# 🎁 БЕСПЛАТНЫЙ ГИД: Максимум от {bot['name']}

## Введение

**{bot['name']}** - {bot['tagline'].lower()}

{bot['description']}

---

## 📚 Содержание

### 1. Быстрый старт

Как начать работу с {bot['name']} за 5 минут:

1. Откройте Telegram
2. Найдите бота
3. Нажмите /start
4. Следуйте инструкциям

### 2. Основные функции

Категория: **{bot['category']}**

Что умеет бот:
- Функция 1
- Функция 2
- Функция 3

### 3. Продвинутые возможности

Используйте бота на 100%:
- Автоматизация
- Интеграции
- Кастомизация

### 4. Лучшие практики

10 советов для эффективного использования {bot['name']}.

### 5. Часто задаваемые вопросы

**Q: Сколько стоит?**
A: {bot['price']}

**Q: Есть ли бесплатная версия?**
A: Да, 7 дней бесплатно!

**Q: Открытый исходный код?**
A: Да! GitHub: {bot['github']}

---

## 🚀 Следующие шаги

1. [Активировать бота](https://t.me/yourbot)
2. Попробовать 7 дней бесплатно
3. Оценить результаты

---

## 💡 Бонус

Специальный промокод для читателей этого гида:

**GUIDE30** - скидка 30% на первый месяц!

[Активировать →](https://t.me/yourbot?start=GUIDE30)

---

**© 2025 {bot['name']}. Все права защищены.**

GitHub: https://github.com/{bot['github']}
"""

def main():
    """Главная функция"""
    base_path = Path("/home/user/AIStreeTest/telegram-bots-research")

    for bot in BOTS:
        bot_path = base_path / bot['id']

        # Создаём директории если не существуют
        (bot_path / "promo-site").mkdir(parents=True, exist_ok=True)
        (bot_path / "email-campaigns").mkdir(parents=True, exist_ok=True)
        (bot_path / "lead-magnet").mkdir(parents=True, exist_ok=True)

        # Генерируем и сохраняем файлы
        with open(bot_path / "promo-site" / "index.html", "w", encoding="utf-8") as f:
            f.write(generate_promo_site(bot))

        with open(bot_path / "email-campaigns" / "email-1-welcome.md", "w", encoding="utf-8") as f:
            f.write(generate_email_welcome(bot))

        with open(bot_path / "email-campaigns" / "email-2-value.md", "w", encoding="utf-8") as f:
            f.write(generate_email_value(bot))

        with open(bot_path / "email-campaigns" / "email-3-urgency.md", "w", encoding="utf-8") as f:
            f.write(generate_email_urgency(bot))

        with open(bot_path / "lead-magnet" / "lead-magnet.md", "w", encoding="utf-8") as f:
            f.write(generate_lead_magnet(bot))

        print(f"✅ Материалы для {bot['name']} созданы")

if __name__ == "__main__":
    main()
    print("\n🎉 Все материалы успешно созданы!")
