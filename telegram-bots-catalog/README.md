# 🤖 Telegram Bots Catalog

Современный каталог из 20 лучших Telegram ботов с анимациями и уникальным дизайном для каждой категории.

## ✨ Особенности

- 📱 **Адаптивный дизайн** - идеально работает на мобильных, планшетах и десктопах
- 🎨 **11 уникальных категорий** - AI, Crypto, E-commerce, Social, Music, Cloud, Monitoring, RSS, CRM, Education, Quiz
- ✨ **Плавные анимации** - Framer Motion анимации на каждой странице
- 🎭 **Интерактивные элементы** - Hover эффекты, анимированные фоны, парящие элементы
- 🚀 **Быстрая загрузка** - Построено на Vite для максимальной производительности
- 🎯 **10+ секций** на каждой странице бота для максимальной конверсии

## 🛠 Технологии

- **Frontend**: React 19 + Vite
- **Стили**: Tailwind CSS 3
- **Анимации**: Framer Motion
- **Роутинг**: React Router v7
- **Иконки**: React Icons
- **Деплой**: Railway (ready to deploy)

## 📦 Установка

```bash
# Перейдите в директорию
cd telegram-bots-catalog

# Установите зависимости
npm install

# Запустите dev server
npm run dev
```

Откройте [http://localhost:5173](http://localhost:5173) в браузере.

## 🚀 Деплой на Railway

### Шаг 1: Подготовка проекта

Проект уже настроен для Railway с файлами:
- `railway.json` - конфигурация Railway
- `nixpacks.toml` - настройки сборки

### Шаг 2: Деплой

1. Зарегистрируйтесь на [Railway.app](https://railway.app)
2. Нажмите "New Project"
3. Выберите "Deploy from GitHub repo"
4. Выберите этот репозиторий
5. Railway автоматически:
   - Обнаружит `nixpacks.toml`
   - Установит зависимости (`npm ci`)
   - Соберет проект (`npm run build`)
   - Запустит preview server (`npm run preview`)

### Шаг 3: Настройки (опционально)

В Railway dashboard можно настроить:
- **Custom Domain** - привязать свой домен
- **Environment Variables** - если понадобятся
- **Auto-deploys** - автоматический деплой при пуше в Git

## 📁 Структура проекта

```
telegram-bots-catalog/
├── src/
│   ├── components/
│   │   └── layout/
│   │       ├── Header.jsx        # Хедер с навигацией
│   │       └── Footer.jsx        # Футер с ссылками
│   ├── pages/
│   │   ├── HomePage.jsx          # Главная с каталогом
│   │   └── BotDetailsPage.jsx   # Детальная страница бота
│   ├── data/
│   │   └── bots.js              # Данные всех 20 ботов
│   ├── App.jsx                  # Основной компонент с роутингом
│   ├── main.jsx                 # Точка входа
│   └── index.css                # Глобальные стили
├── public/                       # Статические файлы
├── railway.json                  # Конфиг Railway
├── nixpacks.toml                 # Конфиг сборки
├── tailwind.config.js            # Настройки Tailwind
└── vite.config.js                # Настройки Vite
```

## 🎨 Категории и цвета

| Категория | Эмодзи | Цвет | Примеры ботов |
|-----------|--------|------|---------------|
| AI | 🤖 | Purple (#667eea) | TeleChat, Master AI BOT, Telegrad |
| Crypto | 💰 | Green (#10b981) | EazeBot, Wallet Tracker |
| Ecommerce | 🛒 | Orange (#f97316) | Greed Shop, Stripe Store |
| Social | 📱 | Pink (#ec4899) | Media Downloader, Vidzilla |
| Music | 🎵 | Violet (#8b5cf6) | Music Downloader, FallenMusic |
| Cloud | ☁️ | Blue (#3b82f6) | Pentaract Cloud, Telegram Upload |
| Monitoring | 📊 | Red (#ef4444) | Server Monitor, ServerStatsBot |
| RSS | 📰 | Yellow (#eab308) | Smart RSS Reader |
| CRM | 💼 | Indigo (#6366f1) | Personal CRM |
| Education | 🎓 | Teal (#14b8a6) | TA-BOT |
| Quiz | 🎮 | Lime (#22c55e) | Quizly AI |

## 🔧 Разработка

```bash
# Dev server с hot reload
npm run dev

# Сборка для продакшена
npm run build

# Preview production build
npm run preview

# Линтинг
npm run lint
```

## 📝 Добавление нового бота

1. Откройте `src/data/bots.js`
2. Добавьте объект бота в массив `BOTS`:

```javascript
{
  id: "21-category-name",
  name: "Bot Name",
  tagline: "Короткое описание",
  subtitle: "Подробное описание",
  github: "username/repo",
  price: "$9.99",
  category: "AI" // или другая категория
}
```

3. Если нужна новая категория, добавьте её в `CATEGORY_CONTENT`

## 🌟 Фичи для улучшения

- [ ] Добавить поиск по ботам
- [ ] Сортировка (по цене, рейтингу, популярности)
- [ ] Dark/Light mode toggle
- [ ] Сравнение ботов side-by-side
- [ ] Фильтр по цене
- [ ] Добавить больше анимированных фонов (Three.js?)
- [ ] Интеграция с реальными API ботов
- [ ] Система отзывов пользователей

## 📄 Лицензия

MIT
