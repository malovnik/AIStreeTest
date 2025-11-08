#!/usr/bin/env python3
"""
УМНЫЙ генератор промо-сайтов для ВСЕХ 20 Telegram-ботов
Автоматически создает уникальный контент для каждого бота
"""

from pathlib import Path

# Полная информация о всех 20 ботах из исследования
BOTS_DATA = [
    {"id": "01-AI-ChatGPT-TeleChat", "name": "TeleChat", "github": "yym68686/ChatGPT-Telegram-Bot",
     "desc": "Множество AI-моделей в одном боте", "price": "$9.99", "category": "AI", "color": "#667eea"},

    {"id": "02-AI-Master-AI-BOT", "name": "Master AI BOT", "github": "yesbhautik/Master-AI-BOT",
     "desc": "Безлимитный GPT-4 Turbo", "price": "$7.99", "category": "AI", "color": "#1e3a8a"},

    {"id": "03-AI-Telegrad", "name": "Telegrad", "github": "eyalzk/telegrad",
     "desc": "Мониторинг ML-экспериментов", "price": "$14.99", "category": "AI", "color": "#8b5cf6"},

    {"id": "04-Crypto-Wallet-Tracker", "name": "CryptoWallet Bot", "github": "alberto-rota/CryptoWallet-TelegramBot",
     "desc": "Трекинг крипто-портфеля", "price": "$4.99", "category": "Crypto", "color": "#f59e0b"},

    {"id": "05-Crypto-EazeBot", "name": "EazeBot", "github": "MarcelBeining/EazeBot",
     "desc": "Автоматизация крипто-трейдинга", "price": "$19.99", "category": "Crypto", "color": "#10b981"},

    {"id": "06-Crypto-Wallet-Tracker", "name": "Wallet Tracker", "github": "dorukyy/telegram-wallet-tracker",
     "desc": "Мониторинг кошельков", "price": "$3.99", "category": "Crypto", "color": "#06b6d4"},

    {"id": "07-Ecommerce-Greed", "name": "Greed Shop Bot", "github": "Steffo99/greed",
     "desc": "Ваш магазин в Telegram", "price": "$29.99", "category": "Ecommerce", "color": "#ec4899"},

    {"id": "08-Ecommerce-Stripe-Bot", "name": "Stripe Store Bot", "github": "levklon/ecommerce_telegram_bot",
     "desc": "E-commerce с Stripe", "price": "$24.99", "category": "Ecommerce", "color": "#8b5cf6"},

    {"id": "09-Social-Media-Downloader", "name": "Media Downloader", "github": "Krxuv/Social-Media-Downloader",
     "desc": "7 соцсетей в одном боте", "price": "$2.99", "category": "Social", "color": "#ef4444"},

    {"id": "10-Social-Vidzilla", "name": "Vidzilla", "github": "zerox9dev/Vidzilla",
     "desc": "Загрузчик видео", "price": "$1.99", "category": "Social", "color": "#f97316"},

    {"id": "11-Music-Downloader", "name": "Music Downloader", "github": "LeninInLoop/MusicDownloader-Telegram-Bot",
     "desc": "Spotify и YouTube", "price": "$3.99", "category": "Music", "color": "#06b6d4"},

    {"id": "12-Music-FallenMusic", "name": "FallenMusic", "github": "AnonymousX1025/FallenMusic",
     "desc": "Музыка в voice chats", "price": "$4.99", "category": "Music", "color": "#8b5cf6"},

    {"id": "13-Cloud-Pentaract", "name": "Pentaract Cloud", "github": "Dominux/Pentaract",
     "desc": "Безлимитное облако", "price": "Free", "category": "Cloud", "color": "#3b82f6"},

    {"id": "14-Cloud-Telegram-Upload", "name": "Telegram Upload", "github": "Nekmo/telegram-upload",
     "desc": "CLI для больших файлов", "price": "$9.99", "category": "Cloud", "color": "#6366f1"},

    {"id": "15-Monitor-Nodejumper", "name": "Server Monitor", "github": "nodejumper-org/monitoring-tool",
     "desc": "Мониторинг серверов", "price": "$14.99", "category": "Monitoring", "color": "#14b8a6"},

    {"id": "16-Monitor-ServerStats", "name": "ServerStatsBot", "github": "geekbeard/ServerStatsBot",
     "desc": "Статистика сервера", "price": "$9.99", "category": "Monitoring", "color": "#10b981"},

    {"id": "17-RSS-Reader", "name": "Smart RSS Reader", "github": "Rongronggg9/RSS-to-Telegram-Bot",
     "desc": "Умный RSS ридер", "price": "$1.99", "category": "RSS", "color": "#f59e0b"},

    {"id": "18-CRM-Personal", "name": "Personal CRM", "github": "vicgalle/personalCRMbot",
     "desc": "Управление отношениями", "price": "$6.99", "category": "CRM", "color": "#8b5cf6"},

    {"id": "19-Education-TA-BOT", "name": "TA-BOT", "github": "Amirparsa-Sal/TA-BOT",
     "desc": "Ассистент преподавателя", "price": "$99", "category": "Education", "color": "#06b6d4"},

    {"id": "20-Quiz-Quizly", "name": "Quizly AI", "github": "ShahbazCoder1/QuizBot",
     "desc": "Квизы с AI", "price": "$2.99", "category": "Quiz", "color": "#ec4899"},
]

def generate_full_html(bot):
    """Генерирует полный HTML-сайт для бота"""

    # Определяем контент на основе категории
    category_content = {
        "AI": {
            "emoji": "🤖",
            "features": [
                {"icon": "🧠", "title": "AI Модели", "desc": "Новейшие языковые модели"},
                {"icon": "⚡", "title": "Быстро", "desc": "Ответы за секунды"},
                {"icon": "🎨", "title": "Генерация", "desc": "Тексты и изображения"},
                {"icon": "💬", "title": "Чаты", "desc": "Групповая работа"},
                {"icon": "📚", "title": "Знания", "desc": "Обширная база знаний"},
                {"icon": "🔒", "title": "Безопасно", "desc": "Защита данных"}
            ]
        },
        "Crypto": {
            "emoji": "💰",
            "features": [
                {"icon": "📊", "title": "Трекинг", "desc": "Отслеживание портфеля"},
                {"icon": "🔔", "title": "Алерты", "desc": "Уведомления о ценах"},
                {"icon": "📈", "title": "Графики", "desc": "Визуализация данных"},
                {"icon": "💹", "title": "P&L", "desc": "Прибыль/убыток"},
                {"icon": "🔐", "title": "Безопасность", "desc": "Защита средств"},
                {"icon": "⚡", "title": "Реалтайм", "desc": "Данные в реальном времени"}
            ]
        },
        "Ecommerce": {
            "emoji": "🛍️",
            "features": [
                {"icon": "💳", "title": "Платежи", "desc": "Прием оплаты"},
                {"icon": "📦", "title": "Товары", "desc": "Управление каталогом"},
                {"icon": "🛒", "title": "Корзина", "desc": "Удобные покупки"},
                {"icon": "📊", "title": "Аналитика", "desc": "Статистика продаж"},
                {"icon": "🌍", "title": "Мультиязычность", "desc": "Разные языки"},
                {"icon": "🔒", "title": "Безопасность", "desc": "Защита платежей"}
            ]
        },
        "Social": {
            "emoji": "📱",
            "features": [
                {"icon": "⬇️", "title": "Загрузка", "desc": "Скачивание контента"},
                {"icon": "🎥", "title": "Видео", "desc": "Все форматы"},
                {"icon": "🖼️", "title": "Фото", "desc": "Высокое качество"},
                {"icon": "⚡", "title": "Быстро", "desc": "Мгновенная загрузка"},
                {"icon": "🌐", "title": "Платформы", "desc": "Все соцсети"},
                {"icon": "💾", "title": "Хранение", "desc": "Сохранение файлов"}
            ]
        },
        "Music": {
            "emoji": "🎵",
            "features": [
                {"icon": "🎧", "title": "Качество", "desc": "HD аудио"},
                {"icon": "⬇️", "title": "Загрузка", "desc": "Скачивание треков"},
                {"icon": "🎤", "title": "Распознавание", "desc": "Поиск по звуку"},
                {"icon": "📝", "title": "Тексты", "desc": "Lyrics для песен"},
                {"icon": "🎼", "title": "Плейлисты", "desc": "Управление списками"},
                {"icon": "🔊", "title": "Стриминг", "desc": "Онлайн проигрывание"}
            ]
        },
        "Cloud": {
            "emoji": "☁️",
            "features": [
                {"icon": "💾", "title": "Хранилище", "desc": "Безлимитное пространство"},
                {"icon": "⬆️", "title": "Загрузка", "desc": "Файлы до 4GB"},
                {"icon": "🔒", "title": "Безопасность", "desc": "Шифрование"},
                {"icon": "📱", "title": "Доступ", "desc": "С любого устройства"},
                {"icon": "🔗", "title": "Ссылки", "desc": "Легкая отправка"},
                {"icon": "⚡", "title": "Скорость", "desc": "Быстрая синхронизация"}
            ]
        },
        "Monitoring": {
            "emoji": "📊",
            "features": [
                {"icon": "🖥️", "title": "Серверы", "desc": "Мониторинг 24/7"},
                {"icon": "🔔", "title": "Алерты", "desc": "Мгновенные уведомления"},
                {"icon": "📈", "title": "Метрики", "desc": "CPU, RAM, Disk"},
                {"icon": "📊", "title": "Графики", "desc": "Визуализация данных"},
                {"icon": "⚠️", "title": "Проблемы", "desc": "Раннее обнаружение"},
                {"icon": "📱", "title": "Мобильно", "desc": "Контроль на ходу"}
            ]
        },
        "RSS": {
            "emoji": "📰",
            "features": [
                {"icon": "📡", "title": "Фиды", "desc": "Множество источников"},
                {"icon": "🎨", "title": "Форматирование", "desc": "Красивый вывод"},
                {"icon": "⏰", "title": "Расписание", "desc": "Авто-обновление"},
                {"icon": "🔍", "title": "Фильтры", "desc": "Только нужное"},
                {"icon": "📱", "title": "Удобство", "desc": "Чтение в Telegram"},
                {"icon": "🌐", "title": "Языки", "desc": "Мультиязычность"}
            ]
        },
        "CRM": {
            "emoji": "👥",
            "features": [
                {"icon": "📇", "title": "Контакты", "desc": "База клиентов"},
                {"icon": "📅", "title": "Встречи", "desc": "Календарь событий"},
                {"icon": "📝", "title": "Заметки", "desc": "История общения"},
                {"icon": "🔔", "title": "Напоминания", "desc": "Не забывайте"},
                {"icon": "📊", "title": "Аналитика", "desc": "Отчеты и метрики"},
                {"icon": "🔗", "title": "Интеграции", "desc": "Связь с сервисами"}
            ]
        },
        "Education": {
            "emoji": "🎓",
            "features": [
                {"icon": "📚", "title": "Курсы", "desc": "Управление материалами"},
                {"icon": "✅", "title": "Задания", "desc": "Домашние работы"},
                {"icon": "📊", "title": "Оценки", "desc": "Система баллов"},
                {"icon": "💬", "title": "Общение", "desc": "Чат со студентами"},
                {"icon": "📅", "title": "Расписание", "desc": "Календарь занятий"},
                {"icon": "📈", "title": "Прогресс", "desc": "Отслеживание успехов"}
            ]
        },
        "Quiz": {
            "emoji": "🎯",
            "features": [
                {"icon": "❓", "title": "Вопросы", "desc": "AI-генерация"},
                {"icon": "🎮", "title": "Игры", "desc": "Интерактивность"},
                {"icon": "🏆", "title": "Рейтинги", "desc": "Таблицы лидеров"},
                {"icon": "📊", "title": "Статистика", "desc": "Прогресс обучения"},
                {"icon": "👥", "title": "Группы", "desc": "Командные квизы"},
                {"icon": "🎨", "title": "Темы", "desc": "Разные категории"}
            ]
        }
    }

    category = bot.get("category", "AI")
    content = category_content.get(category, category_content["AI"])
    emoji = content["emoji"]
    features = content["features"]

    # Генерируем features HTML
    features_html = "\n".join([
        f'''<div class="feature-card">
            <div class="feature-icon">{f['icon']}</div>
            <h3>{f['title']}</h3>
            <p>{f['desc']}</p>
        </div>'''
        for f in features
    ])

    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{bot['name']} - {bot['desc']}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6; color: #1a1a1a;
        }}
        .hero {{
            background: linear-gradient(135deg, {bot['color']} 0%, {bot['color']}dd 100%);
            color: white; padding: 100px 20px; text-align: center;
        }}
        .hero h1 {{ font-size: 4em; font-weight: 900; margin-bottom: 20px; }}
        .hero p {{ font-size: 1.5em; margin-bottom: 30px; opacity: 0.9; }}
        .cta-button {{
            display: inline-block; background: white; color: {bot['color']};
            padding: 18px 50px; border-radius: 50px; text-decoration: none;
            font-weight: bold; font-size: 1.3em; margin: 10px;
            transition: transform 0.3s; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        .cta-button:hover {{ transform: translateY(-5px); }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 80px 20px; }}
        .section-title {{ font-size: 3em; text-align: center; margin-bottom: 20px; color: {bot['color']}; font-weight: 800; }}
        .section-subtitle {{ text-align: center; font-size: 1.3em; color: #64748b; margin-bottom: 60px; }}
        .features-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }}
        .feature-card {{
            background: linear-gradient(135deg, #f8fafc 0%, #f0f9ff 100%);
            padding: 40px; border-radius: 20px; text-align: center;
            transition: transform 0.3s; border: 2px solid #e0f2fe;
        }}
        .feature-card:hover {{ transform: translateY(-10px); }}
        .feature-icon {{ font-size: 4em; margin-bottom: 20px; }}
        .feature-card h3 {{ font-size: 1.5em; margin-bottom: 15px; color: {bot['color']}; }}
        .stats {{ padding: 60px 20px; background: white; text-align: center; }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; max-width: 1000px; margin: 0 auto; }}
        .stat h3 {{ font-size: 3em; color: {bot['color']}; margin-bottom: 10px; }}
        .pricing {{ padding: 80px 20px; background: #f8fafc; }}
        .pricing-cards {{ display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; }}
        .pricing-card {{
            background: white; padding: 50px 40px; border-radius: 25px;
            min-width: 300px; max-width: 380px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        .pricing-card.featured {{
            background: linear-gradient(135deg, {bot['color']} 0%, {bot['color']}dd 100%);
            color: white; transform: scale(1.05);
        }}
        .price {{ font-size: 4em; font-weight: 900; margin: 20px 0; }}
        .footer {{ background: #0f172a; color: white; text-align: center; padding: 60px 20px; }}
        @media (max-width: 768px) {{ .hero h1 {{ font-size: 2.5em; }} .section-title {{ font-size: 2em; }} }}
    </style>
</head>
<body>
    <section class="hero">
        <h1>{emoji} {bot['name']}</h1>
        <p>{bot['desc']}</p>
        <a href="https://t.me/bot" class="cta-button">Начать бесплатно</a>
        <a href="#pricing" class="cta-button" style="background: transparent; border: 2px solid white; color: white;">Тарифы</a>
    </section>

    <section class="stats">
        <div class="stats-grid">
            <div class="stat"><h3>100K+</h3><p>Пользователей</p></div>
            <div class="stat"><h3>4.9/5</h3><p>Рейтинг</p></div>
            <div class="stat"><h3>24/7</h3><p>Поддержка</p></div>
            <div class="stat"><h3>{bot['price']}</h3><p>/месяц</p></div>
        </div>
    </section>

    <div class="container">
        <h2 class="section-title">Возможности {bot['name']}</h2>
        <p class="section-subtitle">Всё, что нужно для эффективной работы</p>
        <div class="features-grid">
            {features_html}
        </div>
    </div>

    <section class="pricing" id="pricing">
        <div class="container">
            <h2 class="section-title">Тарифы</h2>
            <p class="section-subtitle">Выберите подходящий план</p>
            <div class="pricing-cards">
                <div class="pricing-card">
                    <h3>Free</h3>
                    <div class="price">$0</div>
                    <p>Для начала</p>
                    <ul style="list-style: none; padding: 0; margin: 20px 0;">
                        <li>✓ Базовые функции</li>
                        <li>✓ 20 запросов/день</li>
                        <li>✓ Email поддержка</li>
                    </ul>
                    <a href="#" class="cta-button">Начать</a>
                </div>
                <div class="pricing-card featured">
                    <h3>Pro ⭐</h3>
                    <div class="price">{bot['price']}</div>
                    <p>Для профессионалов</p>
                    <ul style="list-style: none; padding: 0; margin: 20px 0;">
                        <li>✓ Все функции</li>
                        <li>✓ Безлимитно</li>
                        <li>✓ Приоритет</li>
                        <li>✓ Поддержка 24/7</li>
                    </ul>
                    <a href="#" class="cta-button">Попробовать</a>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer">
        <p>&copy; 2025 {bot['name']}. Все права защищены.</p>
        <p style="margin-top: 10px;">Категория: {category}</p>
        <p style="margin-top: 5px;">
            GitHub: <a href="https://github.com/{bot['github']}" style="color: {bot['color']};">{bot['github']}</a>
        </p>
    </footer>
</body>
</html>'''


def main():
    base_path = Path("/home/user/AIStreeTest/telegram-bots-research")

    for bot in BOTS_DATA:
        site_path = base_path / bot['id'] / "promo-site" / "index.html"
        site_path.parent.mkdir(parents=True, exist_ok=True)

        html = generate_full_html(bot)
        with open(site_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"✅ {bot['name']} - сайт создан")

    print(f"\n🎉 ВСЕ 20 сайтов созданы!")


if __name__ == "__main__":
    main()
