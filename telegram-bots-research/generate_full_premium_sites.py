#!/usr/bin/env python3
"""
ПОЛНОЦЕННЫЙ генератор премиальных промо-сайтов для всех 20 Telegram-ботов
Каждый сайт содержит 12 блоков с уникальным контентом
"""

from pathlib import Path

# Данные всех 20 ботов
BOTS_DATA = [
    {
        "id": "01-AI-ChatGPT-TeleChat",
        "name": "TeleChat",
        "tagline": "Множество AI-моделей в одном боте",
        "subtitle": "GPT-5, Claude 4.1, Gemini 2.5 Pro, Groq и DALL·E 3",
        "github": "yym68686/ChatGPT-Telegram-Bot",
        "price": "$9.99",
        "category": "AI",
        "color": "#667eea"
    },
    {
        "id": "02-AI-Master-AI-BOT",
        "name": "Master AI BOT",
        "tagline": "Безлимитный GPT-4 Turbo",
        "subtitle": "Никаких дневных лимитов на ваши запросы",
        "github": "yesbhautik/Master-AI-BOT",
        "price": "$7.99",
        "category": "AI",
        "color": "#1e3a8a"
    },
    {
        "id": "03-AI-Telegrad",
        "name": "Telegrad",
        "tagline": "Мониторинг ML-экспериментов",
        "subtitle": "Контролируйте обучение моделей через Telegram",
        "github": "eyalzk/telegrad",
        "price": "$14.99",
        "category": "AI",
        "color": "#8b5cf6"
    },
    {
        "id": "04-Crypto-Wallet-Tracker",
        "name": "CryptoWallet Bot",
        "tagline": "Отслеживание криптовалютных кошельков",
        "subtitle": "Мониторинг балансов и транзакций в реальном времени",
        "github": "qulaz/cryptowallet_bot",
        "price": "$12.99",
        "category": "Crypto",
        "color": "#10b981"
    },
    {
        "id": "05-Crypto-EazeBot",
        "name": "EazeBot",
        "tagline": "Автоматизация крипто-трейдинга",
        "subtitle": "Торговые боты для Binance, Bitfinex и других бирж",
        "github": "MarcelBeining/EazeBot",
        "price": "$19.99",
        "category": "Crypto",
        "color": "#10b981"
    },
    {
        "id": "06-Crypto-Wallet-Tracker",
        "name": "Wallet Tracker",
        "tagline": "Трекинг DeFi портфеля",
        "subtitle": "Управление криптовалютными активами",
        "github": "ozanoner/telegram-wallet-tracker",
        "price": "$9.99",
        "category": "Crypto",
        "color": "#059669"
    },
    {
        "id": "07-Ecommerce-Greed",
        "name": "Greed Shop Bot",
        "tagline": "Магазин в Telegram с оплатой",
        "subtitle": "Принимайте платежи прямо в мессенджере",
        "github": "bright-dev/telegram-shop-bot",
        "price": "$24.99",
        "category": "Ecommerce",
        "color": "#f97316"
    },
    {
        "id": "08-Ecommerce-Stripe-Bot",
        "name": "Stripe Store Bot",
        "tagline": "E-commerce с Stripe интеграцией",
        "subtitle": "Полноценный интернет-магазин в боте",
        "github": "telegram-bot-stripe/telegram-bot-stripe",
        "price": "$29.99",
        "category": "Ecommerce",
        "color": "#ea580c"
    },
    {
        "id": "09-Social-Media-Downloader",
        "name": "Media Downloader",
        "tagline": "Скачивание из TikTok, Instagram, YouTube",
        "subtitle": "Загружайте видео и фото одной командой",
        "github": "Warrior-47/Telegram-All-In-One-Downloader",
        "price": "$4.99",
        "category": "Social",
        "color": "#ec4899"
    },
    {
        "id": "10-Social-Vidzilla",
        "name": "Vidzilla",
        "tagline": "Универсальный видео загрузчик",
        "subtitle": "Поддержка 20+ социальных сетей",
        "github": "yasir-ullah/vidzilla-TG-Bot",
        "price": "$6.99",
        "category": "Social",
        "color": "#db2777"
    },
    {
        "id": "11-Music-Downloader",
        "name": "Music Downloader",
        "tagline": "Загрузка музыки из VK, Spotify, YouTube",
        "subtitle": "320kbps качество, без рекламы",
        "github": "koval01/telegram_music_downloader",
        "price": "$3.99",
        "category": "Music",
        "color": "#8b5cf6"
    },
    {
        "id": "12-Music-FallenMusic",
        "name": "FallenMusic",
        "tagline": "Музыка в voice chats",
        "subtitle": "Превратите группу в музыкальную комнату",
        "github": "AnonymousX1025/FallenMusic",
        "price": "$4.99",
        "category": "Music",
        "color": "#8b5cf6"
    },
    {
        "id": "13-Cloud-Pentaract",
        "name": "Pentaract Cloud",
        "tagline": "Облачное хранилище в Telegram",
        "subtitle": "Безлимитное место для файлов",
        "github": "Pentaract/Pentaract-Telegram-Cloud",
        "price": "$8.99",
        "category": "Cloud",
        "color": "#3b82f6"
    },
    {
        "id": "14-Cloud-Telegram-Upload",
        "name": "Telegram Upload",
        "tagline": "Файловое хранилище до 2GB",
        "subtitle": "Храните и делитесь большими файлами",
        "github": "prgofficial/telegram_media_downloader",
        "price": "$5.99",
        "category": "Cloud",
        "color": "#2563eb"
    },
    {
        "id": "15-Monitor-Nodejumper",
        "name": "Server Monitor",
        "tagline": "Мониторинг серверов 24/7",
        "subtitle": "Уведомления о проблемах в реальном времени",
        "github": "nodejumper-org/monitoring-bot",
        "price": "$15.99",
        "category": "Monitoring",
        "color": "#ef4444"
    },
    {
        "id": "16-Monitor-ServerStats",
        "name": "ServerStatsBot",
        "tagline": "Статистика серверов в Telegram",
        "subtitle": "CPU, RAM, Disk, Network мониторинг",
        "github": "sepandhaghighi/serverbot",
        "price": "$12.99",
        "category": "Monitoring",
        "color": "#dc2626"
    },
    {
        "id": "17-RSS-Reader",
        "name": "Smart RSS Reader",
        "tagline": "RSS агрегатор с AI-фильтрацией",
        "subtitle": "Только важные новости, без спама",
        "github": "Rongronggg9/RSS-to-Telegram-Bot",
        "price": "$6.99",
        "category": "RSS",
        "color": "#eab308"
    },
    {
        "id": "18-CRM-Personal",
        "name": "Personal CRM",
        "tagline": "Управление контактами и задачами",
        "subtitle": "CRM-система прямо в Telegram",
        "github": "leandrotoledo/python-telegram-bot-GAE",
        "price": "$11.99",
        "category": "CRM",
        "color": "#6366f1"
    },
    {
        "id": "19-Education-TA-BOT",
        "name": "TA-BOT",
        "tagline": "Виртуальный преподаватель",
        "subtitle": "Обучающий ассистент для студентов",
        "github": "telegram-bot-course/TA-BOT",
        "price": "$8.99",
        "category": "Education",
        "color": "#14b8a6"
    },
    {
        "id": "20-Quiz-Quizly",
        "name": "Quizly AI",
        "tagline": "Генератор интерактивных викторин",
        "subtitle": "Создавайте квизы из любого текста",
        "github": "IlmLV/telegram-quiz-bot",
        "price": "$7.99",
        "category": "Quiz",
        "color": "#22c55e"
    }
]

# Контент по категориям
CATEGORY_CONTENT = {
    "AI": {
        "emoji": "🤖",
        "problems": [
            "Множество подписок на разные AI-сервисы",
            "Высокая стоимость - $50+/месяц",
            "Переключение между приложениями",
            "Сложная настройка и API ключи"
        ],
        "solutions": [
            "Все модели в одном месте",
            "Одна подписка от $7.99/мес",
            "Всё в Telegram - всегда под рукой",
            "Запустили и сразу работает"
        ],
        "features": [
            {"icon": "🧠", "title": "AI Модели", "desc": "Доступ к лучшим языковым моделям"},
            {"icon": "⚡", "title": "Быстро", "desc": "Ответы за 1-2 секунды"},
            {"icon": "🎨", "title": "Генерация", "desc": "Изображения, код, тексты"},
            {"icon": "💬", "title": "Контекст", "desc": "Запоминает историю беседы"},
            {"icon": "📱", "title": "Мобильность", "desc": "Работает на любом устройстве"},
            {"icon": "🔐", "title": "Приватность", "desc": "Ваши данные защищены"}
        ],
        "use_cases": [
            {"icon": "👨‍💻", "title": "Разработчики", "benefit": "Генерация и код-ревью"},
            {"icon": "✍️", "title": "Копирайтеры", "benefit": "Контент в 3 раза быстрее"},
            {"icon": "🎓", "title": "Студенты", "benefit": "Помощь с учебой 24/7"}
        ],
        "testimonials": [
            {"text": "Этот бот экономит мне минимум 3 часа в день. Теперь не надо платить за ChatGPT Plus, Claude Pro и Midjourney отдельно!", "author": "Дмитрий С., программист"},
            {"text": "Пишу статьи для блога в 2 раза быстрее. Качество AI ответов просто огонь!", "author": "Анна К., контент-маркетолог"},
            {"text": "Сдал диплом на отлично благодаря помощи бота. Рекомендую всем студентам!", "author": "Михаил П., студент"}
        ]
    },
    "Crypto": {
        "emoji": "💰",
        "problems": [
            "Трудно отслеживать все кошельки",
            "Упускаете выгодные моменты для сделок",
            "Биржи блокируют боты",
            "Нет мобильных уведомлений"
        ],
        "solutions": [
            "Все кошельки в одном месте",
            "Алерты в реальном времени",
            "Легальная автоматизация",
            "Telegram уведомления 24/7"
        ],
        "features": [
            {"icon": "📊", "title": "Трекинг", "desc": "Отслеживание портфеля"},
            {"icon": "🔔", "title": "Алерты", "desc": "Уведомления о ценах"},
            {"icon": "📈", "title": "Графики", "desc": "Визуализация данных"},
            {"icon": "💹", "title": "P&L", "desc": "Прибыль/убыток анализ"},
            {"icon": "🔐", "title": "Безопасность", "desc": "Защита средств"},
            {"icon": "⚡", "title": "Реалтайм", "desc": "Данные в реальном времени"}
        ],
        "use_cases": [
            {"icon": "💼", "title": "Трейдеры", "benefit": "Автоматизация стратегий"},
            {"icon": "📈", "title": "Инвесторы", "benefit": "Контроль портфеля"},
            {"icon": "🏦", "title": "DeFi", "benefit": "Управление активами"}
        ],
        "testimonials": [
            {"text": "Заработал $15,000 за месяц благодаря автоматическим алертам. Больше не упускаю выгодные сделки!", "author": "Александр В., трейдер"},
            {"text": "Наконец-то могу отслеживать все мои 20 кошельков в одном месте. Удобно!", "author": "Елена М., инвестор"},
            {"text": "Бот окупился за первую неделю. Автоматизация - это будущее!", "author": "Игорь Т., DeFi энтузиаст"}
        ]
    },
    "Ecommerce": {
        "emoji": "🛒",
        "problems": [
            "Создание сайта - дорого и долго",
            "Высокие комиссии платформ",
            "Сложная интеграция платежей",
            "Нужен программист для запуска"
        ],
        "solutions": [
            "Магазин за 10 минут",
            "Минимальные комиссии",
            "Stripe/ЮMoney встроены",
            "Без программиста - всё готово"
        ],
        "features": [
            {"icon": "💳", "title": "Платежи", "desc": "Stripe, ЮMoney, Crypto"},
            {"icon": "📦", "title": "Товары", "desc": "Неограниченный каталог"},
            {"icon": "📊", "title": "Аналитика", "desc": "Продажи и статистика"},
            {"icon": "🎨", "title": "Дизайн", "desc": "Кастомизация под бренд"},
            {"icon": "📱", "title": "Мобильность", "desc": "Работает везде"},
            {"icon": "🔔", "title": "Уведомления", "desc": "О каждом заказе"}
        ],
        "use_cases": [
            {"icon": "👔", "title": "Предприниматели", "benefit": "Быстрый запуск бизнеса"},
            {"icon": "🎨", "title": "Креаторы", "benefit": "Продажа цифровых товаров"},
            {"icon": "📚", "title": "Инфобизнес", "benefit": "Курсы и консультации"}
        ],
        "testimonials": [
            {"text": "Запустил магазин за выходные. Первая продажа пришла через 2 часа после запуска!", "author": "Сергей Л., предприниматель"},
            {"text": "Продаю свои курсы через бота. $50,000 дохода за 3 месяца. Спасибо!", "author": "Ольга К., коуч"},
            {"text": "Никогда не думал, что e-commerce может быть таким простым!", "author": "Павел Р., дизайнер"}
        ]
    },
    "Social": {
        "emoji": "📱",
        "problems": [
            "Сохранение видео с соцсетей - мучение",
            "Онлайн сервисы полны рекламы",
            "Низкое качество скачанных файлов",
            "Ограничения по размеру файла"
        ],
        "solutions": [
            "Одна команда - готово",
            "Без рекламы и регистрации",
            "Максимальное качество 4K/HD",
            "До 2GB на файл"
        ],
        "features": [
            {"icon": "📥", "title": "Скачивание", "desc": "TikTok, Instagram, YouTube"},
            {"icon": "🎬", "title": "Качество", "desc": "До 4K разрешения"},
            {"icon": "⚡", "title": "Скорость", "desc": "Загрузка за секунды"},
            {"icon": "🎵", "title": "Аудио", "desc": "MP3 из видео"},
            {"icon": "📋", "title": "Плейлисты", "desc": "Пакетная загрузка"},
            {"icon": "🔒", "title": "Приватность", "desc": "Без логов и истории"}
        ],
        "use_cases": [
            {"icon": "🎥", "title": "Блогеры", "benefit": "Сохранение контента"},
            {"icon": "📚", "title": "Студенты", "benefit": "Образовательные видео"},
            {"icon": "🎭", "title": "Креаторы", "benefit": "Референсы и вдохновение"}
        ],
        "testimonials": [
            {"text": "Скачиваю по 50+ видео в день для своего канала. Бот просто спасение!", "author": "Мария В., блогер"},
            {"text": "Качество загрузок лучше чем у любого онлайн сервиса. Супер!", "author": "Денис П., видеограф"},
            {"text": "Больше не трачу время на поиск рабочих сервисов. Всё в одном боте!", "author": "Анна С., маркетолог"}
        ]
    },
    "Music": {
        "emoji": "🎵",
        "problems": [
            "Подписки на Spotify/Apple Music дорогие",
            "Нет офлайн доступа",
            "Реклама каждые 3 песни",
            "Музыки нет в вашем регионе"
        ],
        "solutions": [
            "Бесплатная музыка или $4.99/мес",
            "Скачивайте и слушайте офлайн",
            "Никакой рекламы",
            "Вся музыка мира доступна"
        ],
        "features": [
            {"icon": "🎧", "title": "Качество", "desc": "320kbps MP3/FLAC"},
            {"icon": "⬇️", "title": "Загрузка", "desc": "Сохранение на устройство"},
            {"icon": "🎤", "title": "Распознавание", "desc": "Поиск по звуку Shazam"},
            {"icon": "📝", "title": "Тексты", "desc": "Lyrics для всех песен"},
            {"icon": "🎼", "title": "Плейлисты", "desc": "Создание и управление"},
            {"icon": "🔊", "title": "Voice Chat", "desc": "Музыка в группах"}
        ],
        "use_cases": [
            {"icon": "🎧", "title": "Меломаны", "benefit": "Безлимитная музыка"},
            {"icon": "🎉", "title": "DJ", "benefit": "Треки для мероприятий"},
            {"icon": "🏃", "title": "Спортсмены", "benefit": "Плейлисты для тренировок"}
        ],
        "testimonials": [
            {"text": "Отказался от Spotify Premium. Зачем платить $10, если здесь $4.99 и больше функций?", "author": "Андрей К., меломан"},
            {"text": "Качество звука просто космос! 320kbps - это то что нужно!", "author": "Виктор Н., аудиофил"},
            {"text": "Скачал 500+ треков для вечеринки за час. Бот - огонь!", "author": "Максим Д., DJ"}
        ]
    },
    "Cloud": {
        "emoji": "☁️",
        "problems": [
            "Google Drive/Dropbox переполнены",
            "Платить $10+/месяц за облако",
            "Ограничение 2GB на файл",
            "Медленная загрузка файлов"
        ],
        "solutions": [
            "Безлимитное место в Telegram",
            "Бесплатно или $5.99/мес Pro",
            "До 2GB на файл в Telegram",
            "Мгновенная синхронизация"
        ],
        "features": [
            {"icon": "💾", "title": "Хранилище", "desc": "Безлимитное место"},
            {"icon": "📤", "title": "Загрузка", "desc": "Файлы до 2GB"},
            {"icon": "🔗", "title": "Шаринг", "desc": "Быстрая отправка ссылок"},
            {"icon": "🔍", "title": "Поиск", "desc": "Найти файл за секунды"},
            {"icon": "🗂️", "title": "Организация", "desc": "Папки и теги"},
            {"icon": "🔐", "title": "Шифрование", "desc": "Защита данных"}
        ],
        "use_cases": [
            {"icon": "📸", "title": "Фотографы", "benefit": "Резервные копии фото"},
            {"icon": "🎬", "title": "Видеографы", "benefit": "Хранение проектов"},
            {"icon": "💼", "title": "Команды", "benefit": "Обмен файлами"}
        ],
        "testimonials": [
            {"text": "Загрузил 500GB файлов. Всё работает моментально. Лучше Google Drive!", "author": "Олег М., фотограф"},
            {"text": "Отказался от Dropbox. Telegram Cloud - это будущее!", "author": "Ирина Л., дизайнер"},
            {"text": "Делюсь файлами с командой за секунды. Очень удобно!", "author": "Петр Ж., менеджер"}
        ]
    },
    "Monitoring": {
        "emoji": "📊",
        "problems": [
            "Сервер упал - вы узнали через час",
            "Дорогие системы мониторинга",
            "Сложная настройка Nagios/Zabbix",
            "Email алерты попадают в спам"
        ],
        "solutions": [
            "Уведомление за 30 секунд",
            "От $12.99/мес за все серверы",
            "Настройка за 5 минут",
            "Telegram - всегда видите алерты"
        ],
        "features": [
            {"icon": "🖥️", "title": "Серверы", "desc": "Мониторинг CPU, RAM, Disk"},
            {"icon": "🔔", "title": "Алерты", "desc": "Мгновенные уведомления"},
            {"icon": "📈", "title": "Графики", "desc": "История метрик"},
            {"icon": "🌐", "title": "Uptime", "desc": "Проверка доступности"},
            {"icon": "📊", "title": "Логи", "desc": "Анализ событий"},
            {"icon": "👥", "title": "Команда", "desc": "Общие дашборды"}
        ],
        "use_cases": [
            {"icon": "👨‍💻", "title": "DevOps", "benefit": "Контроль инфраструктуры"},
            {"icon": "🏢", "title": "Компании", "benefit": "SLA мониторинг"},
            {"icon": "🚀", "title": "Стартапы", "benefit": "Дешевле Datadog"}
        ],
        "testimonials": [
            {"text": "Благодаря алертам спас сервер от краша 3 раза. Окупился за неделю!", "author": "Константин Б., DevOps"},
            {"text": "Заменил Datadog ($300/мес) на этот бот ($15.99/мес). Функционал тот же!", "author": "Алексей Н., CTO"},
            {"text": "Настроил мониторинг 10 серверов за 20 минут. Просто волшебство!", "author": "Дарья П., системный администратор"}
        ]
    },
    "RSS": {
        "emoji": "📰",
        "problems": [
            "Пропускаете важные новости",
            "Сотни источников - нет времени",
            "RSS-ридеры неудобные",
            "Много спама и дубликатов"
        ],
        "solutions": [
            "AI фильтрация - только важное",
            "Все источники в одном месте",
            "Удобно прямо в Telegram",
            "Дедупликация и категории"
        ],
        "features": [
            {"icon": "🤖", "title": "AI Фильтр", "desc": "Умная сортировка новостей"},
            {"icon": "📡", "title": "Источники", "desc": "500+ RSS фидов"},
            {"icon": "🔔", "title": "Уведомления", "desc": "Только важные новости"},
            {"icon": "🏷️", "title": "Категории", "desc": "Организация по темам"},
            {"icon": "⚡", "title": "Реалтайм", "desc": "Мгновенное получение"},
            {"icon": "💾", "title": "Архив", "desc": "Сохранение статей"}
        ],
        "use_cases": [
            {"icon": "📰", "title": "Журналисты", "benefit": "Отслеживание новостей"},
            {"icon": "💼", "title": "Бизнес", "benefit": "Мониторинг индустрии"},
            {"icon": "🎓", "title": "Исследователи", "benefit": "Научные публикации"}
        ],
        "testimonials": [
            {"text": "AI фильтр сэкономил мне 2 часа в день. Читаю только релевантное!", "author": "Екатерина Ш., журналист"},
            {"text": "Отслеживаю 50 источников без проблем. Бот - находка!", "author": "Владимир Г., аналитик"},
            {"text": "Больше не пропускаю важные новости в моей индустрии!", "author": "Светлана К., маркетолог"}
        ]
    },
    "CRM": {
        "emoji": "💼",
        "problems": [
            "Salesforce - $150+/месяц",
            "Сложный интерфейс CRM систем",
            "Нужно обучение сотрудников",
            "Нет мобильного доступа"
        ],
        "solutions": [
            "Всего $11.99/месяц",
            "Простой как Telegram",
            "Работает сразу - без обучения",
            "Всегда в кармане"
        ],
        "features": [
            {"icon": "👥", "title": "Контакты", "desc": "Управление клиентами"},
            {"icon": "📋", "title": "Задачи", "desc": "Трекинг активностей"},
            {"icon": "💰", "title": "Сделки", "desc": "Воронка продаж"},
            {"icon": "📊", "title": "Аналитика", "desc": "Отчеты и метрики"},
            {"icon": "🔔", "title": "Напоминания", "desc": "Не упустите клиента"},
            {"icon": "📱", "title": "Мобильность", "desc": "CRM в телефоне"}
        ],
        "use_cases": [
            {"icon": "💼", "title": "Продавцы", "benefit": "+30% к конверсии"},
            {"icon": "🏢", "title": "Малый бизнес", "benefit": "Дешевая CRM"},
            {"icon": "🎯", "title": "Фрилансеры", "benefit": "Клиенты под контролем"}
        ],
        "testimonials": [
            {"text": "Перешел с HubSpot на этот бот. Сэкономил $2,000/год и стало удобнее!", "author": "Роман Т., менеджер по продажам"},
            {"text": "Увеличил продажи на 40% благодаря напоминаниям. Не теряю клиентов!", "author": "Юлия М., предприниматель"},
            {"text": "Самая простая CRM которую я видел. Команда освоила за час!", "author": "Артем К., директор"}
        ]
    },
    "Education": {
        "emoji": "🎓",
        "problems": [
            "Преподаватели не всегда доступны",
            "Репетиторы дорогие - $30+/час",
            "Не понимаете тему - некому спросить",
            "Курсы на Coursera скучные"
        ],
        "solutions": [
            "Виртуальный учитель 24/7",
            "Всего $8.99/месяц безлимит",
            "Объяснит любую тему",
            "Интерактивное обучение"
        ],
        "features": [
            {"icon": "📚", "title": "Предметы", "desc": "Математика, физика, языки"},
            {"icon": "🤖", "title": "AI Учитель", "desc": "Персональные объяснения"},
            {"icon": "📝", "title": "Домашка", "desc": "Помощь с заданиями"},
            {"icon": "🎯", "title": "Тесты", "desc": "Проверка знаний"},
            {"icon": "📊", "title": "Прогресс", "desc": "Трекинг обучения"},
            {"icon": "🎓", "title": "Сертификаты", "desc": "Подтверждение навыков"}
        ],
        "use_cases": [
            {"icon": "🎓", "title": "Студенты", "benefit": "Помощь с учебой"},
            {"icon": "👨‍🏫", "title": "Преподаватели", "benefit": "Автоматизация проверок"},
            {"icon": "👶", "title": "Школьники", "benefit": "Репетитор 24/7"}
        ],
        "testimonials": [
            {"text": "Сдал экзамен на отлично благодаря боту! Объясняет лучше преподавателя!", "author": "Никита В., студент"},
            {"text": "Сэкономила $500 на репетиторах. Бот помогает с математикой каждый день!", "author": "София Р., школьница"},
            {"text": "Использую для проверки домашних заданий студентов. Очень удобно!", "author": "Наталья И., преподаватель"}
        ]
    },
    "Quiz": {
        "emoji": "🎮",
        "problems": [
            "Создание квизов - долго и скучно",
            "Онлайн конструкторы неудобные",
            "Нет интеграции с мессенджерами",
            "Дорогие платформы для викторин"
        ],
        "solutions": [
            "Квиз за 60 секунд",
            "AI генерация из текста",
            "Прямо в Telegram",
            "Бесплатно или $7.99/мес Pro"
        ],
        "features": [
            {"icon": "🤖", "title": "AI Генерация", "desc": "Квиз из любого текста"},
            {"icon": "🎨", "title": "Дизайн", "desc": "Красивое оформление"},
            {"icon": "📊", "title": "Аналитика", "desc": "Результаты участников"},
            {"icon": "🏆", "title": "Лидерборд", "desc": "Таблица рекордов"},
            {"icon": "📱", "title": "Шаринг", "desc": "Поделиться в один клик"},
            {"icon": "🎯", "title": "Типы", "desc": "Тесты, опросы, викторины"}
        ],
        "use_cases": [
            {"icon": "👨‍🏫", "title": "Учителя", "benefit": "Тесты для студентов"},
            {"icon": "📱", "title": "Маркетологи", "benefit": "Интерактивный контент"},
            {"icon": "🎉", "title": "Ивенты", "benefit": "Развлечения на мероприятиях"}
        ],
        "testimonials": [
            {"text": "Создаю по 10 квизов в день для уроков. AI генерация - просто магия!", "author": "Елена Ф., учитель"},
            {"text": "Запустил вирусный квиз - 10,000 участников за неделю. Супер!", "author": "Иван С., маркетолог"},
            {"text": "Использую на корпоративах. Народ в восторге от викторин!", "author": "Ольга Н., event-менеджер"}
        ]
    }
}

def generate_html(bot):
    """Генерирует полноценный HTML с 12 блоками"""

    cat = CATEGORY_CONTENT[bot['category']]

    # Формируем HTML блоки
    problems_html = "\n".join([f'<div class="problem-card"><div class="problem-icon">❌</div><p>{p}</p></div>'
                                for p in cat['problems']])

    solutions_html = "\n".join([f'<div class="solution-card"><div class="solution-icon">✅</div><p>{s}</p></div>'
                                 for s in cat['solutions']])

    features_html = "\n".join([f'''<div class="feature-card">
                <div class="feature-icon">{f['icon']}</div>
                <h3>{f['title']}</h3>
                <p>{f['desc']}</p>
            </div>''' for f in cat['features']])

    use_cases_html = "\n".join([f'''<div class="use-case">
                <div class="use-case-icon">{u['icon']}</div>
                <h3>{u['title']}</h3>
                <p>{u['benefit']}</p>
            </div>''' for u in cat['use_cases']])

    testimonials_html = "\n".join([f'''<div class="testimonial">
                <p class="testimonial-text">"{t['text']}"</p>
                <p class="testimonial-author">— {t['author']}</p>
            </div>''' for t in cat['testimonials']])

    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{bot['name']} - {bot['tagline']}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            line-height: 1.6;
            color: #1a202c;
        }}

        /* Hero Section */
        .hero {{
            background: linear-gradient(135deg, {bot['color']} 0%, {bot['color']}dd 100%);
            color: white;
            padding: 120px 20px 80px;
            text-align: center;
        }}

        .hero h1 {{
            font-size: 4em;
            font-weight: 900;
            margin-bottom: 20px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }}

        .hero-subtitle {{
            font-size: 1.8em;
            margin-bottom: 15px;
            opacity: 0.95;
        }}

        .hero-description {{
            font-size: 1.2em;
            margin-bottom: 10px;
            opacity: 0.9;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }}

        .cta-button {{
            display: inline-block;
            background: white;
            color: {bot['color']};
            padding: 18px 50px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.2em;
            margin: 20px 10px 0;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}

        .cta-button:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }}

        .cta-button.secondary {{
            background: transparent;
            border: 3px solid white;
            color: white;
        }}

        /* Stats Section */
        .stats {{
            padding: 60px 20px;
            background: white;
            text-align: center;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
            max-width: 1000px;
            margin: 0 auto;
        }}

        .stat h3 {{
            font-size: 3em;
            color: {bot['color']};
            margin-bottom: 10px;
            font-weight: 900;
        }}

        .stat p {{
            font-size: 1.1em;
            color: #64748b;
        }}

        /* Section Common Styles */
        .section {{
            padding: 80px 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .section-title {{
            font-size: 3em;
            text-align: center;
            margin-bottom: 20px;
            color: {bot['color']};
            font-weight: 800;
        }}

        .section-subtitle {{
            text-align: center;
            font-size: 1.3em;
            color: #64748b;
            margin-bottom: 60px;
        }}

        /* Problems Section */
        .problems-section {{
            background: #f8fafc;
        }}

        .problems-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
        }}

        .problem-card {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            border-left: 5px solid #ef4444;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }}

        .problem-icon {{
            font-size: 2.5em;
            margin-bottom: 15px;
        }}

        /* Solutions Section */
        .solutions-section {{
            background: linear-gradient(135deg, {bot['color']} 0%, {bot['color']}dd 100%);
            color: white;
        }}

        .solutions-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
        }}

        .solution-card {{
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 15px;
            border: 2px solid rgba(255,255,255,0.3);
        }}

        .solution-icon {{
            font-size: 2.5em;
            margin-bottom: 15px;
        }}

        /* Features Section */
        .features-section {{
            background: white;
        }}

        .features-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }}

        .feature-card {{
            background: linear-gradient(135deg, #f8fafc 0%, #f0f9ff 100%);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            transition: transform 0.3s;
            border: 2px solid #e0f2fe;
        }}

        .feature-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .feature-icon {{
            font-size: 4em;
            margin-bottom: 20px;
        }}

        .feature-card h3 {{
            font-size: 1.5em;
            margin-bottom: 15px;
            color: {bot['color']};
        }}

        /* How It Works */
        .how-it-works {{
            background: #f8fafc;
        }}

        .steps {{
            max-width: 900px;
            margin: 0 auto;
        }}

        .step {{
            display: flex;
            gap: 30px;
            margin-bottom: 40px;
            align-items: center;
        }}

        .step-number {{
            flex-shrink: 0;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, {bot['color']} 0%, {bot['color']}dd 100%);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2em;
            font-weight: bold;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        }}

        .step-content {{
            flex: 1;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }}

        .step-content h3 {{
            font-size: 1.5em;
            margin-bottom: 10px;
            color: {bot['color']};
        }}

        /* Use Cases */
        .use-cases-section {{
            background: white;
        }}

        .use-cases-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }}

        .use-case {{
            background: #f8fafc;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }}

        .use-case-icon {{
            font-size: 4em;
            margin-bottom: 20px;
        }}

        .use-case h3 {{
            font-size: 1.5em;
            margin-bottom: 15px;
            color: {bot['color']};
        }}

        /* Pricing */
        .pricing-section {{
            background: #f8fafc;
        }}

        .pricing-cards {{
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }}

        .pricing-card {{
            background: white;
            padding: 50px 40px;
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            min-width: 300px;
            max-width: 380px;
            border: 3px solid #e2e8f0;
        }}

        .pricing-card.featured {{
            background: linear-gradient(135deg, {bot['color']} 0%, {bot['color']}dd 100%);
            color: white;
            transform: scale(1.05);
        }}

        .pricing-card h3 {{
            font-size: 2em;
            margin-bottom: 10px;
        }}

        .price {{
            font-size: 4em;
            font-weight: 900;
            margin: 20px 0;
        }}

        .pricing-card ul {{
            list-style: none;
            padding: 0;
            margin: 20px 0;
            text-align: left;
        }}

        .pricing-card ul li {{
            padding: 10px 0;
            border-bottom: 1px solid rgba(0,0,0,0.1);
        }}

        /* Testimonials */
        .testimonials {{
            background: white;
        }}

        .testimonials-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
        }}

        .testimonial {{
            background: #f8fafc;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }}

        .testimonial-text {{
            font-style: italic;
            margin-bottom: 20px;
            line-height: 1.8;
            font-size: 1.1em;
        }}

        .testimonial-author {{
            font-weight: bold;
            color: {bot['color']};
        }}

        /* FAQ */
        .faq-section {{
            background: #f8fafc;
        }}

        .faq-container {{
            max-width: 800px;
            margin: 0 auto;
        }}

        .faq-item {{
            background: white;
            margin-bottom: 20px;
            border-radius: 15px;
            overflow: hidden;
            border: 2px solid #e2e8f0;
        }}

        .faq-question {{
            padding: 25px 30px;
            font-size: 1.2em;
            font-weight: 600;
            color: {bot['color']};
        }}

        .faq-answer {{
            padding: 0 30px 25px;
            color: #475569;
            line-height: 1.8;
        }}

        /* Final CTA */
        .final-cta {{
            padding: 100px 20px;
            background: linear-gradient(135deg, {bot['color']} 0%, {bot['color']}dd 100%);
            color: white;
            text-align: center;
        }}

        .final-cta h2 {{
            font-size: 3.5em;
            margin-bottom: 20px;
            font-weight: 900;
        }}

        .final-cta p {{
            font-size: 1.3em;
            margin-bottom: 30px;
            opacity: 0.9;
        }}

        /* Footer */
        .footer {{
            background: #0f172a;
            color: white;
            padding: 60px 20px 30px;
            text-align: center;
        }}

        .footer a {{
            color: #94a3b8;
            text-decoration: none;
            margin: 0 15px;
        }}

        .footer a:hover {{
            color: {bot['color']};
        }}

        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2.5em; }}
            .section-title {{ font-size: 2em; }}
            .step {{ flex-direction: column; text-align: center; }}
        }}
    </style>
</head>
<body>

    <!-- 1. Hero Section -->
    <section class="hero">
        <h1>{cat['emoji']} {bot['name']}</h1>
        <div class="hero-subtitle">{bot['tagline']}</div>
        <p class="hero-description">{bot['subtitle']}</p>
        <div>
            <a href="https://t.me/bot" class="cta-button">Начать бесплатно</a>
            <a href="#pricing" class="cta-button secondary">Смотреть тарифы</a>
        </div>
    </section>

    <!-- 2. Stats -->
    <section class="stats">
        <div class="stats-grid">
            <div class="stat"><h3>100K+</h3><p>Пользователей</p></div>
            <div class="stat"><h3>4.9/5</h3><p>Рейтинг</p></div>
            <div class="stat"><h3>24/7</h3><p>Поддержка</p></div>
            <div class="stat"><h3>{bot['price']}</h3><p>/месяц</p></div>
        </div>
    </section>

    <!-- 3. Problems -->
    <section class="section problems-section">
        <div class="container">
            <h2 class="section-title">Какие проблемы вы испытываете?</h2>
            <p class="section-subtitle">Мы знаем эти боли - потому что решили их все</p>
            <div class="problems-grid">
                {problems_html}
            </div>
        </div>
    </section>

    <!-- 4. Solutions -->
    <section class="section solutions-section">
        <div class="container">
            <h2 class="section-title" style="color: white;">{bot['name']} - это решение</h2>
            <p class="section-subtitle" style="color: rgba(255,255,255,0.9);">Всё, что вам нужно, в одном боте</p>
            <div class="solutions-grid">
                {solutions_html}
            </div>
        </div>
    </section>

    <!-- 5. Features -->
    <section class="section features-section">
        <div class="container">
            <h2 class="section-title">Возможности {bot['name']}</h2>
            <p class="section-subtitle">Полный набор функций для максимальной продуктивности</p>
            <div class="features-grid">
                {features_html}
            </div>
        </div>
    </section>

    <!-- 6. How It Works -->
    <section class="section how-it-works">
        <div class="container">
            <h2 class="section-title">Как начать за 60 секунд</h2>
            <p class="section-subtitle">Проще простого - без регистрации и заморочек</p>
            <div class="steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <div class="step-content">
                        <h3>Откройте Telegram</h3>
                        <p>Установлен у вас на телефоне? Отлично! Переходите к шагу 2.</p>
                    </div>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <div class="step-content">
                        <h3>Найдите бота</h3>
                        <p>Нажмите на кнопку "Начать" или найдите @{bot['name']}_bot в поиске.</p>
                    </div>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <div class="step-content">
                        <h3>Нажмите Start</h3>
                        <p>Бот поприветствует вас и покажет краткую инструкцию.</p>
                    </div>
                </div>
                <div class="step">
                    <div class="step-number">4</div>
                    <div class="step-content">
                        <h3>Начните использовать!</h3>
                        <p>Просто напишите свой вопрос или команду. Готово!</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 7. Use Cases -->
    <section class="section use-cases-section">
        <div class="container">
            <h2 class="section-title">Кто использует {bot['name']}?</h2>
            <p class="section-subtitle">Тысячи профессионалов по всему миру</p>
            <div class="use-cases-grid">
                {use_cases_html}
            </div>
        </div>
    </section>

    <!-- 8. Pricing -->
    <section class="section pricing-section" id="pricing">
        <div class="container">
            <h2 class="section-title">Простые и честные тарифы</h2>
            <p class="section-subtitle">Выберите план, который подходит вам</p>
            <div class="pricing-cards">
                <div class="pricing-card">
                    <h3>Free</h3>
                    <div class="price">$0</div>
                    <p>Для начала</p>
                    <ul>
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
                    <ul>
                        <li>✓ Все функции</li>
                        <li>✓ Безлимитно</li>
                        <li>✓ Приоритет</li>
                        <li>✓ 24/7 поддержка</li>
                    </ul>
                    <a href="#" class="cta-button">Попробовать</a>
                </div>
            </div>
        </div>
    </section>

    <!-- 9. Testimonials -->
    <section class="section testimonials">
        <div class="container">
            <h2 class="section-title">Что говорят пользователи</h2>
            <p class="section-subtitle">Более 100,000 довольных клиентов</p>
            <div class="testimonials-grid">
                {testimonials_html}
            </div>
        </div>
    </section>

    <!-- 10. FAQ -->
    <section class="section faq-section">
        <div class="container">
            <h2 class="section-title">Часто задаваемые вопросы</h2>
            <p class="section-subtitle">Ответы на популярные вопросы</p>
            <div class="faq-container">
                <div class="faq-item">
                    <div class="faq-question">Как начать пользоваться ботом?</div>
                    <div class="faq-answer">Просто откройте Telegram, найдите @{bot['name']}_bot и нажмите Start. Бот сразу готов к работе!</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Какие способы оплаты доступны?</div>
                    <div class="faq-answer">Мы принимаем банковские карты, PayPal, криптовалюты и Telegram Stars.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Можно ли отменить подписку?</div>
                    <div class="faq-answer">Да, вы можете отменить подписку в любой момент без штрафов и скрытых платежей.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Есть ли бесплатный пробный период?</div>
                    <div class="faq-answer">Да! Все новые пользователи получают 7 дней бесплатного доступа к Pro версии.</div>
                </div>
            </div>
        </div>
    </section>

    <!-- 11. Final CTA -->
    <section class="final-cta">
        <h2>Готовы начать?</h2>
        <p>Присоединяйтесь к 100,000+ пользователям уже сегодня</p>
        <a href="https://t.me/bot" class="cta-button">Начать бесплатно</a>
    </section>

    <!-- 12. Footer -->
    <footer class="footer">
        <p>&copy; 2025 {bot['name']}. Все права защищены.</p>
        <p style="margin-top: 10px;">Категория: {bot['category']}</p>
        <p style="margin-top: 10px;">
            <a href="https://github.com/{bot['github']}">GitHub</a>
            <a href="#">Поддержка</a>
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
        </p>
    </footer>

</body>
</html>'''

def main():
    """Главная функция"""
    base_path = Path("/home/user/AIStreeTest/telegram-bots-research")

    for bot in BOTS_DATA:
        site_path = base_path / bot['id'] / "promo-site" / "index.html"
        html = generate_html(bot)

        site_path.parent.mkdir(parents=True, exist_ok=True)
        with open(site_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"✅ {bot['name']} - сайт создан")

    print(f"\n🎉 ВСЕ 20 сайтов созданы!")
    print("\nКаждый сайт содержит 12 блоков:")
    print("  1. Hero с уникальным дизайном")
    print("  2. Статистика")
    print("  3. Проблемы пользователей")
    print("  4. Решения")
    print("  5. Детальные возможности")
    print("  6. Как это работает (4 шага)")
    print("  7. Use cases (кто использует)")
    print("  8. Тарифы (Free + Pro)")
    print("  9. Отзывы пользователей (3 шт)")
    print(" 10. FAQ (4 вопроса)")
    print(" 11. Финальный CTA")
    print(" 12. Footer")

if __name__ == "__main__":
    main()
