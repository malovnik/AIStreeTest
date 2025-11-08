export const CATEGORY_CONTENT = {
  AI: {
    emoji: "🤖",
    color: "#667eea",
    gradient: "from-purple-500 to-indigo-600",
    problems: [
      "Множество подписок на разные AI-сервисы",
      "Высокая стоимость - $50+/месяц",
      "Переключение между приложениями",
      "Сложная настройка и API ключи"
    ],
    solutions: [
      "Все модели в одном месте",
      "Одна подписка от $7.99/мес",
      "Всё в Telegram - всегда под рукой",
      "Запустили и сразу работает"
    ],
    features: [
      { icon: "🧠", title: "AI Модели", desc: "Доступ к лучшим языковым моделям" },
      { icon: "⚡", title: "Быстро", desc: "Ответы за 1-2 секунды" },
      { icon: "🎨", title: "Генерация", desc: "Изображения, код, тексты" },
      { icon: "💬", title: "Контекст", desc: "Запоминает историю беседы" },
      { icon: "📱", title: "Мобильность", desc: "Работает на любом устройстве" },
      { icon: "🔐", title: "Приватность", desc: "Ваши данные защищены" }
    ],
    testimonials: [
      { text: "Этот бот экономит мне минимум 3 часа в день. Теперь не надо платить за ChatGPT Plus, Claude Pro и Midjourney отдельно!", author: "Дмитрий С., программист" },
      { text: "Пишу статьи для блога в 2 раза быстрее. Качество AI ответов просто огонь!", author: "Анна К., контент-маркетолог" },
      { text: "Сдал диплом на отлично благодаря помощи бота. Рекомендую всем студентам!", author: "Михаил П., студент" }
    ]
  },
  Crypto: {
    emoji: "💰",
    color: "#10b981",
    gradient: "from-green-500 to-emerald-600",
    problems: [
      "Трудно отслеживать все кошельки",
      "Упускаете выгодные моменты для сделок",
      "Биржи блокируют боты",
      "Нет мобильных уведомлений"
    ],
    solutions: [
      "Все кошельки в одном месте",
      "Алерты в реальном времени",
      "Легальная автоматизация",
      "Telegram уведомления 24/7"
    ],
    features: [
      { icon: "📊", title: "Трекинг", desc: "Отслеживание портфеля" },
      { icon: "🔔", title: "Алерты", desc: "Уведомления о ценах" },
      { icon: "📈", title: "Графики", desc: "Визуализация данных" },
      { icon: "💹", title: "P&L", desc: "Прибыль/убыток анализ" },
      { icon: "🔐", title: "Безопасность", desc: "Защита средств" },
      { icon: "⚡", title: "Реалтайм", desc: "Данные в реальном времени" }
    ],
    testimonials: [
      { text: "Заработал $15,000 за месяц благодаря автоматическим алертам. Больше не упускаю выгодные сделки!", author: "Александр В., трейдер" },
      { text: "Наконец-то могу отслеживать все мои 20 кошельков в одном месте. Удобно!", author: "Елена М., инвестор" },
      { text: "Бот окупился за первую неделю. Автоматизация - это будущее!", author: "Игорь Т., DeFi энтузиаст" }
    ]
  },
  Ecommerce: {
    emoji: "🛒",
    color: "#f97316",
    gradient: "from-orange-500 to-red-600",
    problems: [
      "Создание сайта - дорого и долго",
      "Высокие комиссии платформ",
      "Сложная интеграция платежей",
      "Нужен программист для запуска"
    ],
    solutions: [
      "Магазин за 10 минут",
      "Минимальные комиссии",
      "Stripe/ЮMoney встроены",
      "Без программиста - всё готово"
    ],
    features: [
      { icon: "💳", title: "Платежи", desc: "Stripe, ЮMoney, Crypto" },
      { icon: "📦", title: "Товары", desc: "Неограниченный каталог" },
      { icon: "📊", title: "Аналитика", desc: "Продажи и статистика" },
      { icon: "🎨", title: "Дизайн", desc: "Кастомизация под бренд" },
      { icon: "📱", title: "Мобильность", desc: "Работает везде" },
      { icon: "🔔", title: "Уведомления", desc: "О каждом заказе" }
    ],
    testimonials: [
      { text: "Запустил магазин за выходные. Первая продажа пришла через 2 часа после запуска!", author: "Сергей Л., предприниматель" },
      { text: "Продаю свои курсы через бота. $50,000 дохода за 3 месяца. Спасибо!", author: "Ольга К., коуч" },
      { text: "Никогда не думал, что e-commerce может быть таким простым!", author: "Павел Р., дизайнер" }
    ]
  },
  Social: {
    emoji: "📱",
    color: "#ec4899",
    gradient: "from-pink-500 to-rose-600",
    problems: [
      "Сохранение видео с соцсетей - мучение",
      "Онлайн сервисы полны рекламы",
      "Низкое качество скачанных файлов",
      "Ограничения по размеру файла"
    ],
    solutions: [
      "Одна команда - готово",
      "Без рекламы и регистрации",
      "Максимальное качество 4K/HD",
      "До 2GB на файл"
    ],
    features: [
      { icon: "📥", title: "Скачивание", desc: "TikTok, Instagram, YouTube" },
      { icon: "🎬", title: "Качество", desc: "До 4K разрешения" },
      { icon: "⚡", title: "Скорость", desc: "Загрузка за секунды" },
      { icon: "🎵", title: "Аудио", desc: "MP3 из видео" },
      { icon: "📋", title: "Плейлисты", desc: "Пакетная загрузка" },
      { icon: "🔒", title: "Приватность", desc: "Без логов и истории" }
    ],
    testimonials: [
      { text: "Скачиваю по 50+ видео в день для своего канала. Бот просто спасение!", author: "Мария В., блогер" },
      { text: "Качество загрузок лучше чем у любого онлайн сервиса. Супер!", author: "Денис П., видеограф" },
      { text: "Больше не трачу время на поиск рабочих сервисов. Всё в одном боте!", author: "Анна С., маркетолог" }
    ]
  },
  Music: {
    emoji: "🎵",
    color: "#8b5cf6",
    gradient: "from-purple-500 to-violet-600",
    problems: [
      "Подписки на Spotify/Apple Music дорогие",
      "Нет офлайн доступа",
      "Реклама каждые 3 песни",
      "Музыки нет в вашем регионе"
    ],
    solutions: [
      "Бесплатная музыка или $4.99/мес",
      "Скачивайте и слушайте офлайн",
      "Никакой рекламы",
      "Вся музыка мира доступна"
    ],
    features: [
      { icon: "🎧", title: "Качество", desc: "320kbps MP3/FLAC" },
      { icon: "⬇️", title: "Загрузка", desc: "Сохранение на устройство" },
      { icon: "🎤", title: "Распознавание", desc: "Поиск по звуку Shazam" },
      { icon: "📝", title: "Тексты", desc: "Lyrics для всех песен" },
      { icon: "🎼", title: "Плейлисты", desc: "Создание и управление" },
      { icon: "🔊", title: "Voice Chat", desc: "Музыка в группах" }
    ],
    testimonials: [
      { text: "Отказался от Spotify Premium. Зачем платить $10, если здесь $4.99 и больше функций?", author: "Андрей К., меломан" },
      { text: "Качество звука просто космос! 320kbps - это то что нужно!", author: "Виктор Н., аудиофил" },
      { text: "Скачал 500+ треков для вечеринки за час. Бот - огонь!", author: "Максим Д., DJ" }
    ]
  },
  Cloud: {
    emoji: "☁️",
    color: "#3b82f6",
    gradient: "from-blue-500 to-cyan-600",
    problems: [
      "Google Drive/Dropbox переполнены",
      "Платить $10+/месяц за облако",
      "Ограничение 2GB на файл",
      "Медленная загрузка файлов"
    ],
    solutions: [
      "Безлимитное место в Telegram",
      "Бесплатно или $5.99/мес Pro",
      "До 2GB на файл в Telegram",
      "Мгновенная синхронизация"
    ],
    features: [
      { icon: "💾", title: "Хранилище", desc: "Безлимитное место" },
      { icon: "📤", title: "Загрузка", desc: "Файлы до 2GB" },
      { icon: "🔗", title: "Шаринг", desc: "Быстрая отправка ссылок" },
      { icon: "🔍", title: "Поиск", desc: "Найти файл за секунды" },
      { icon: "🗂️", title: "Организация", desc: "Папки и теги" },
      { icon: "🔐", title: "Шифрование", desc: "Защита данных" }
    ],
    testimonials: [
      { text: "Загрузил 500GB файлов. Всё работает моментально. Лучше Google Drive!", author: "Олег М., фотограф" },
      { text: "Отказался от Dropbox. Telegram Cloud - это будущее!", author: "Ирина Л., дизайнер" },
      { text: "Делюсь файлами с командой за секунды. Очень удобно!", author: "Петр Ж., менеджер" }
    ]
  },
  Monitoring: {
    emoji: "📊",
    color: "#ef4444",
    gradient: "from-red-500 to-rose-600",
    problems: [
      "Сервер упал - вы узнали через час",
      "Дорогие системы мониторинга",
      "Сложная настройка Nagios/Zabbix",
      "Email алерты попадают в спам"
    ],
    solutions: [
      "Уведомление за 30 секунд",
      "От $12.99/мес за все серверы",
      "Настройка за 5 минут",
      "Telegram - всегда видите алерты"
    ],
    features: [
      { icon: "🖥️", title: "Серверы", desc: "Мониторинг CPU, RAM, Disk" },
      { icon: "🔔", title: "Алерты", desc: "Мгновенные уведомления" },
      { icon: "📈", title: "Графики", desc: "История метрик" },
      { icon: "🌐", title: "Uptime", desc: "Проверка доступности" },
      { icon: "📊", title: "Логи", desc: "Анализ событий" },
      { icon: "👥", title: "Команда", desc: "Общие дашборды" }
    ],
    testimonials: [
      { text: "Благодаря алертам спас сервер от краша 3 раза. Окупился за неделю!", author: "Константин Б., DevOps" },
      { text: "Заменил Datadog ($300/мес) на этот бот ($15.99/мес). Функционал тот же!", author: "Алексей Н., CTO" },
      { text: "Настроил мониторинг 10 серверов за 20 минут. Просто волшебство!", author: "Дарья П., системный администратор" }
    ]
  },
  RSS: {
    emoji: "📰",
    color: "#eab308",
    gradient: "from-yellow-500 to-amber-600",
    problems: [
      "Пропускаете важные новости",
      "Сотни источников - нет времени",
      "RSS-ридеры неудобные",
      "Много спама и дубликатов"
    ],
    solutions: [
      "AI фильтрация - только важное",
      "Все источники в одном месте",
      "Удобно прямо в Telegram",
      "Дедупликация и категории"
    ],
    features: [
      { icon: "🤖", title: "AI Фильтр", desc: "Умная сортировка новостей" },
      { icon: "📡", title: "Источники", desc: "500+ RSS фидов" },
      { icon: "🔔", title: "Уведомления", desc: "Только важные новости" },
      { icon: "🏷️", title: "Категории", desc: "Организация по темам" },
      { icon: "⚡", title: "Реалтайм", desc: "Мгновенное получение" },
      { icon: "💾", title: "Архив", desc: "Сохранение статей" }
    ],
    testimonials: [
      { text: "AI фильтр сэкономил мне 2 часа в день. Читаю только релевантное!", author: "Екатерина Ш., журналист" },
      { text: "Отслеживаю 50 источников без проблем. Бот - находка!", author: "Владимир Г., аналитик" },
      { text: "Больше не пропускаю важные новости в моей индустрии!", author: "Светлана К., маркетолог" }
    ]
  },
  CRM: {
    emoji: "💼",
    color: "#6366f1",
    gradient: "from-indigo-500 to-blue-600",
    problems: [
      "Salesforce - $150+/месяц",
      "Сложный интерфейс CRM систем",
      "Нужно обучение сотрудников",
      "Нет мобильного доступа"
    ],
    solutions: [
      "Всего $11.99/месяц",
      "Простой как Telegram",
      "Работает сразу - без обучения",
      "Всегда в кармане"
    ],
    features: [
      { icon: "👥", title: "Контакты", desc: "Управление клиентами" },
      { icon: "📋", title: "Задачи", desc: "Трекинг активностей" },
      { icon: "💰", title: "Сделки", desc: "Воронка продаж" },
      { icon: "📊", title: "Аналитика", desc: "Отчеты и метрики" },
      { icon: "🔔", title: "Напоминания", desc: "Не упустите клиента" },
      { icon: "📱", title: "Мобильность", desc: "CRM в телефоне" }
    ],
    testimonials: [
      { text: "Перешел с HubSpot на этот бот. Сэкономил $2,000/год и стало удобнее!", author: "Роман Т., менеджер по продажам" },
      { text: "Увеличил продажи на 40% благодаря напоминаниям. Не теряю клиентов!", author: "Юлия М., предприниматель" },
      { text: "Самая простая CRM которую я видел. Команда освоила за час!", author: "Артем К., директор" }
    ]
  },
  Education: {
    emoji: "🎓",
    color: "#14b8a6",
    gradient: "from-teal-500 to-cyan-600",
    problems: [
      "Преподаватели не всегда доступны",
      "Репетиторы дорогие - $30+/час",
      "Не понимаете тему - некому спросить",
      "Курсы на Coursera скучные"
    ],
    solutions: [
      "Виртуальный учитель 24/7",
      "Всего $8.99/месяц безлимит",
      "Объяснит любую тему",
      "Интерактивное обучение"
    ],
    features: [
      { icon: "📚", title: "Предметы", desc: "Математика, физика, языки" },
      { icon: "🤖", title: "AI Учитель", desc: "Персональные объяснения" },
      { icon: "📝", title: "Домашка", desc: "Помощь с заданиями" },
      { icon: "🎯", title: "Тесты", desc: "Проверка знаний" },
      { icon: "📊", title: "Прогресс", desc: "Трекинг обучения" },
      { icon: "🎓", title: "Сертификаты", desc: "Подтверждение навыков" }
    ],
    testimonials: [
      { text: "Сдал экзамен на отлично благодаря боту! Объясняет лучше преподавателя!", author: "Никита В., студент" },
      { text: "Сэкономила $500 на репетиторах. Бот помогает с математикой каждый день!", author: "София Р., школьница" },
      { text: "Использую для проверки домашних заданий студентов. Очень удобно!", author: "Наталья И., преподаватель" }
    ]
  },
  Quiz: {
    emoji: "🎮",
    color: "#22c55e",
    gradient: "from-green-500 to-lime-600",
    problems: [
      "Создание квизов - долго и скучно",
      "Онлайн конструкторы неудобные",
      "Нет интеграции с мессенджерами",
      "Дорогие платформы для викторин"
    ],
    solutions: [
      "Квиз за 60 секунд",
      "AI генерация из текста",
      "Прямо в Telegram",
      "Бесплатно или $7.99/мес Pro"
    ],
    features: [
      { icon: "🤖", title: "AI Генерация", desc: "Квиз из любого текста" },
      { icon: "🎨", title: "Дизайн", desc: "Красивое оформление" },
      { icon: "📊", title: "Аналитика", desc: "Результаты участников" },
      { icon: "🏆", title: "Лидерборд", desc: "Таблица рекордов" },
      { icon: "📱", title: "Шаринг", desc: "Поделиться в один клик" },
      { icon: "🎯", title: "Типы", desc: "Тесты, опросы, викторины" }
    ],
    testimonials: [
      { text: "Создаю по 10 квизов в день для уроков. AI генерация - просто магия!", author: "Елена Ф., учитель" },
      { text: "Запустил вирусный квиз - 10,000 участников за неделю. Супер!", author: "Иван С., маркетолог" },
      { text: "Использую на корпоративах. Народ в восторге от викторин!", author: "Ольга Н., event-менеджер" }
    ]
  }
};

export const BOTS = [
  {
    id: "01-ai-telechat",
    name: "TeleChat",
    tagline: "Множество AI-моделей в одном боте",
    subtitle: "GPT-5, Claude 4.1, Gemini 2.5 Pro, Groq и DALL·E 3",
    github: "yym68686/ChatGPT-Telegram-Bot",
    price: "$9.99",
    category: "AI"
  },
  {
    id: "02-ai-master",
    name: "Master AI BOT",
    tagline: "Безлимитный GPT-4 Turbo",
    subtitle: "Никаких дневных лимитов на ваши запросы",
    github: "yesbhautik/Master-AI-BOT",
    price: "$7.99",
    category: "AI"
  },
  {
    id: "03-ai-telegrad",
    name: "Telegrad",
    tagline: "Мониторинг ML-экспериментов",
    subtitle: "Контролируйте обучение моделей через Telegram",
    github: "eyalzk/telegrad",
    price: "$14.99",
    category: "AI"
  },
  {
    id: "04-crypto-wallet",
    name: "CryptoWallet Bot",
    tagline: "Отслеживание криптовалютных кошельков",
    subtitle: "Мониторинг балансов и транзакций в реальном времени",
    github: "qulaz/cryptowallet_bot",
    price: "$12.99",
    category: "Crypto"
  },
  {
    id: "05-crypto-eazebot",
    name: "EazeBot",
    tagline: "Автоматизация крипто-трейдинга",
    subtitle: "Торговые боты для Binance, Bitfinex и других бирж",
    github: "MarcelBeining/EazeBot",
    price: "$19.99",
    category: "Crypto"
  },
  {
    id: "06-crypto-tracker",
    name: "Wallet Tracker",
    tagline: "Трекинг DeFi портфеля",
    subtitle: "Управление криптовалютными активами",
    github: "ozanoner/telegram-wallet-tracker",
    price: "$9.99",
    category: "Crypto"
  },
  {
    id: "07-ecommerce-greed",
    name: "Greed Shop Bot",
    tagline: "Магазин в Telegram с оплатой",
    subtitle: "Принимайте платежи прямо в мессенджере",
    github: "bright-dev/telegram-shop-bot",
    price: "$24.99",
    category: "Ecommerce"
  },
  {
    id: "08-ecommerce-stripe",
    name: "Stripe Store Bot",
    tagline: "E-commerce с Stripe интеграцией",
    subtitle: "Полноценный интернет-магазин в боте",
    github: "telegram-bot-stripe/telegram-bot-stripe",
    price: "$29.99",
    category: "Ecommerce"
  },
  {
    id: "09-social-downloader",
    name: "Media Downloader",
    tagline: "Скачивание из TikTok, Instagram, YouTube",
    subtitle: "Загружайте видео и фото одной командой",
    github: "Warrior-47/Telegram-All-In-One-Downloader",
    price: "$4.99",
    category: "Social"
  },
  {
    id: "10-social-vidzilla",
    name: "Vidzilla",
    tagline: "Универсальный видео загрузчик",
    subtitle: "Поддержка 20+ социальных сетей",
    github: "yasir-ullah/vidzilla-TG-Bot",
    price: "$6.99",
    category: "Social"
  },
  {
    id: "11-music-downloader",
    name: "Music Downloader",
    tagline: "Загрузка музыки из VK, Spotify, YouTube",
    subtitle: "320kbps качество, без рекламы",
    github: "koval01/telegram_music_downloader",
    price: "$3.99",
    category: "Music"
  },
  {
    id: "12-music-fallen",
    name: "FallenMusic",
    tagline: "Музыка в voice chats",
    subtitle: "Превратите группу в музыкальную комнату",
    github: "AnonymousX1025/FallenMusic",
    price: "$4.99",
    category: "Music"
  },
  {
    id: "13-cloud-pentaract",
    name: "Pentaract Cloud",
    tagline: "Облачное хранилище в Telegram",
    subtitle: "Безлимитное место для файлов",
    github: "Pentaract/Pentaract-Telegram-Cloud",
    price: "$8.99",
    category: "Cloud"
  },
  {
    id: "14-cloud-upload",
    name: "Telegram Upload",
    tagline: "Файловое хранилище до 2GB",
    subtitle: "Храните и делитесь большими файлами",
    github: "prgofficial/telegram_media_downloader",
    price: "$5.99",
    category: "Cloud"
  },
  {
    id: "15-monitor-server",
    name: "Server Monitor",
    tagline: "Мониторинг серверов 24/7",
    subtitle: "Уведомления о проблемах в реальном времени",
    github: "nodejumper-org/monitoring-bot",
    price: "$15.99",
    category: "Monitoring"
  },
  {
    id: "16-monitor-stats",
    name: "ServerStatsBot",
    tagline: "Статистика серверов в Telegram",
    subtitle: "CPU, RAM, Disk, Network мониторинг",
    github: "sepandhaghighi/serverbot",
    price: "$12.99",
    category: "Monitoring"
  },
  {
    id: "17-rss-reader",
    name: "Smart RSS Reader",
    tagline: "RSS агрегатор с AI-фильтрацией",
    subtitle: "Только важные новости, без спама",
    github: "Rongronggg9/RSS-to-Telegram-Bot",
    price: "$6.99",
    category: "RSS"
  },
  {
    id: "18-crm-personal",
    name: "Personal CRM",
    tagline: "Управление контактами и задачами",
    subtitle: "CRM-система прямо в Telegram",
    github: "leandrotoledo/python-telegram-bot-GAE",
    price: "$11.99",
    category: "CRM"
  },
  {
    id: "19-education-ta",
    name: "TA-BOT",
    tagline: "Виртуальный преподаватель",
    subtitle: "Обучающий ассистент для студентов",
    github: "telegram-bot-course/TA-BOT",
    price: "$8.99",
    category: "Education"
  },
  {
    id: "20-quiz-quizly",
    name: "Quizly AI",
    tagline: "Генератор интерактивных викторин",
    subtitle: "Создавайте квизы из любого текста",
    github: "IlmLV/telegram-quiz-bot",
    price: "$7.99",
    category: "Quiz"
  }
];
