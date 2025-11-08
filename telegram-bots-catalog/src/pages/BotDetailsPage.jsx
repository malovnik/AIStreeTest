import { useParams, Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { BOTS, CATEGORY_CONTENT } from '../data/bots';
import { FaGithub, FaArrowLeft } from 'react-icons/fa';

const BotDetailsPage = () => {
  const { botId } = useParams();
  const bot = BOTS.find(b => b.id === botId);

  if (!bot) {
    return (
      <div className="container mx-auto px-4 py-20 text-center">
        <h1 className="text-4xl font-bold mb-4">Бот не найден</h1>
        <Link to="/" className="text-purple-600 hover:underline">
          ← Вернуться на главную
        </Link>
      </div>
    );
  }

  const categoryData = CATEGORY_CONTENT[bot.category];

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: { staggerChildren: 0.1 }
    }
  };

  const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1
    }
  };

  return (
    <div className="min-h-screen">
      {/* Back Button */}
      <div className="container mx-auto px-4 py-6">
        <Link to="/">
          <motion.button
            whileHover={{ x: -5 }}
            className="flex items-center space-x-2 text-purple-600 hover:text-purple-800 font-semibold"
          >
            <FaArrowLeft />
            <span>Назад к каталогу</span>
          </motion.button>
        </Link>
      </div>

      {/* 1. Hero Section */}
      <section
        className="relative text-white py-32 overflow-hidden"
        style={{
          background: `linear-gradient(135deg, ${categoryData.color} 0%, ${categoryData.color}dd 100%)`,
        }}
      >
        {/* Animated Background */}
        <div className="absolute inset-0 opacity-20">
          {[...Array(15)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute text-9xl"
              style={{
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
              }}
              animate={{
                y: [0, -50, 0],
                rotate: [0, 360],
                opacity: [0.2, 0.4, 0.2],
              }}
              transition={{
                duration: Math.random() * 5 + 3,
                repeat: Infinity,
                delay: Math.random() * 2,
              }}
            >
              {categoryData.emoji}
            </motion.div>
          ))}
        </div>

        <div className="container mx-auto px-4 relative z-10">
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.5 }}
            className="text-center max-w-4xl mx-auto"
          >
            <motion.div
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ type: "spring", stiffness: 200 }}
              className="text-9xl mb-6"
            >
              {categoryData.emoji}
            </motion.div>
            <h1 className="text-6xl md:text-8xl font-black mb-4">{bot.name}</h1>
            <p className="text-2xl md:text-3xl mb-4 opacity-95">{bot.tagline}</p>
            <p className="text-xl opacity-90 mb-8">{bot.subtitle}</p>

            <div className="flex flex-wrap justify-center gap-4">
              <motion.a
                href="https://t.me/bot"
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.95 }}
                className="bg-white text-gray-900 px-10 py-4 rounded-full font-bold text-lg shadow-2xl"
              >
                Начать бесплатно
              </motion.a>
              <motion.a
                href={`https://github.com/${bot.github}`}
                target="_blank"
                rel="noopener noreferrer"
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.95 }}
                className="bg-white/20 backdrop-blur-lg border-2 border-white px-10 py-4 rounded-full font-bold text-lg flex items-center space-x-2"
              >
                <FaGithub />
                <span>GitHub</span>
              </motion.a>
            </div>
          </motion.div>
        </div>
      </section>

      {/* 2. Stats */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4">
          <motion.div
            className="grid grid-cols-2 md:grid-cols-4 gap-6"
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true }}
          >
            {[
              { num: '100K+', label: 'Пользователей' },
              { num: '4.9/5', label: 'Рейтинг' },
              { num: '24/7', label: 'Поддержка' },
              { num: bot.price, label: '/месяц' },
            ].map((stat, i) => (
              <motion.div
                key={i}
                variants={itemVariants}
                whileHover={{ scale: 1.05 }}
                className="text-center p-6 rounded-2xl bg-gradient-to-br from-gray-50 to-white shadow-lg"
              >
                <h3 className="text-5xl font-black mb-2" style={{ color: categoryData.color }}>
                  {stat.num}
                </h3>
                <p className="text-gray-600">{stat.label}</p>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* 3. Problems */}
      <section className="py-20 bg-gray-50">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <h2 className="text-5xl font-black mb-4">Какие проблемы вы испытываете?</h2>
            <p className="text-xl text-gray-600">Мы знаем эти боли - потому что решили их все</p>
          </motion.div>

          <motion.div
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true }}
          >
            {categoryData.problems.map((problem, i) => (
              <motion.div
                key={i}
                variants={itemVariants}
                whileHover={{ y: -10 }}
                className="bg-white p-6 rounded-2xl border-l-4 border-red-500 shadow-lg"
              >
                <div className="text-4xl mb-3">❌</div>
                <p className="text-gray-800">{problem}</p>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* 4. Solutions */}
      <section
        className="py-20 text-white"
        style={{
          background: `linear-gradient(135deg, ${categoryData.color} 0%, ${categoryData.color}dd 100%)`,
        }}
      >
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <h2 className="text-5xl font-black mb-4">{bot.name} - это решение</h2>
            <p className="text-xl opacity-90">Всё, что вам нужно, в одном боте</p>
          </motion.div>

          <motion.div
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true }}
          >
            {categoryData.solutions.map((solution, i) => (
              <motion.div
                key={i}
                variants={itemVariants}
                whileHover={{ scale: 1.05 }}
                className="bg-white/10 backdrop-blur-lg border-2 border-white/30 p-6 rounded-2xl"
              >
                <div className="text-4xl mb-3">✅</div>
                <p>{solution}</p>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* 5. Features */}
      <section className="py-20 bg-white">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <h2 className="text-5xl font-black mb-4">Возможности {bot.name}</h2>
            <p className="text-xl text-gray-600">Полный набор функций для максимальной продуктивности</p>
          </motion.div>

          <motion.div
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true }}
          >
            {categoryData.features.map((feature, i) => (
              <motion.div
                key={i}
                variants={itemVariants}
                whileHover={{ y: -10, scale: 1.03 }}
                className="bg-gradient-to-br from-gray-50 to-white p-8 rounded-3xl shadow-xl text-center border-2 border-gray-100"
              >
                <motion.div
                  className="text-6xl mb-4"
                  whileHover={{ rotate: 360 }}
                  transition={{ duration: 0.5 }}
                >
                  {feature.icon}
                </motion.div>
                <h3 className="text-2xl font-bold mb-2" style={{ color: categoryData.color }}>
                  {feature.title}
                </h3>
                <p className="text-gray-600">{feature.desc}</p>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* 6. How It Works */}
      <section className="py-20 bg-gray-50">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <h2 className="text-5xl font-black mb-4">Как начать за 60 секунд</h2>
            <p className="text-xl text-gray-600">Проще простого - без регистрации и заморочек</p>
          </motion.div>

          <div className="max-w-3xl mx-auto space-y-8">
            {[
              { num: 1, title: 'Откройте Telegram', desc: 'Установлен у вас на телефоне? Отлично! Переходите к шагу 2.' },
              { num: 2, title: 'Найдите бота', desc: `Нажмите на кнопку "Начать" или найдите @${bot.name}_bot в поиске.` },
              { num: 3, title: 'Нажмите Start', desc: 'Бот поприветствует вас и покажет краткую инструкцию.' },
              { num: 4, title: 'Начните использовать!', desc: 'Просто напишите свой вопрос или команду. Готово!' },
            ].map((step, i) => (
              <motion.div
                key={i}
                initial={{ x: -50, opacity: 0 }}
                whileInView={{ x: 0, opacity: 1 }}
                transition={{ delay: i * 0.1 }}
                viewport={{ once: true }}
                className="flex items-center space-x-6"
              >
                <motion.div
                  whileHover={{ scale: 1.1, rotate: 360 }}
                  className="flex-shrink-0 w-20 h-20 rounded-full flex items-center justify-center text-3xl font-black text-white shadow-2xl"
                  style={{ background: categoryData.color }}
                >
                  {step.num}
                </motion.div>
                <div className="flex-1 bg-white p-6 rounded-2xl shadow-lg">
                  <h3 className="text-2xl font-bold mb-2" style={{ color: categoryData.color }}>
                    {step.title}
                  </h3>
                  <p className="text-gray-600">{step.desc}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* 7. Pricing */}
      <section className="py-20 bg-white">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <h2 className="text-5xl font-black mb-4">Простые и честные тарифы</h2>
            <p className="text-xl text-gray-600">Выберите план, который подходит вам</p>
          </motion.div>

          <div className="flex flex-wrap justify-center gap-8">
            {/* Free Plan */}
            <motion.div
              whileHover={{ y: -10 }}
              className="bg-white border-2 border-gray-200 p-10 rounded-3xl shadow-xl max-w-sm"
            >
              <h3 className="text-3xl font-bold mb-4">Free</h3>
              <div className="text-6xl font-black mb-6">$0</div>
              <p className="text-gray-600 mb-6">Для начала</p>
              <ul className="space-y-3 mb-8 text-left">
                <li className="flex items-center space-x-2">
                  <span className="text-green-500">✓</span>
                  <span>Базовые функции</span>
                </li>
                <li className="flex items-center space-x-2">
                  <span className="text-green-500">✓</span>
                  <span>20 запросов/день</span>
                </li>
                <li className="flex items-center space-x-2">
                  <span className="text-green-500">✓</span>
                  <span>Email поддержка</span>
                </li>
              </ul>
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="w-full bg-gray-200 text-gray-800 py-4 rounded-full font-bold text-lg"
              >
                Начать
              </motion.button>
            </motion.div>

            {/* Pro Plan */}
            <motion.div
              whileHover={{ y: -10, scale: 1.05 }}
              className="text-white p-10 rounded-3xl shadow-2xl max-w-sm relative overflow-hidden"
              style={{
                background: `linear-gradient(135deg, ${categoryData.color} 0%, ${categoryData.color}dd 100%)`,
              }}
            >
              <div className="absolute top-4 right-4 bg-yellow-400 text-gray-900 px-4 py-1 rounded-full text-sm font-bold">
                ⭐ Популярный
              </div>
              <h3 className="text-3xl font-bold mb-4">Pro</h3>
              <div className="text-6xl font-black mb-6">{bot.price}</div>
              <p className="opacity-90 mb-6">Для профессионалов</p>
              <ul className="space-y-3 mb-8 text-left">
                <li className="flex items-center space-x-2">
                  <span>✓</span>
                  <span>Все функции</span>
                </li>
                <li className="flex items-center space-x-2">
                  <span>✓</span>
                  <span>Безлимитно</span>
                </li>
                <li className="flex items-center space-x-2">
                  <span>✓</span>
                  <span>Приоритет</span>
                </li>
                <li className="flex items-center space-x-2">
                  <span>✓</span>
                  <span>24/7 поддержка</span>
                </li>
              </ul>
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="w-full bg-white text-gray-900 py-4 rounded-full font-bold text-lg shadow-xl"
              >
                Попробовать
              </motion.button>
            </motion.div>
          </div>
        </div>
      </section>

      {/* 8. Testimonials */}
      <section className="py-20 bg-gray-50">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <h2 className="text-5xl font-black mb-4">Что говорят пользователи</h2>
            <p className="text-xl text-gray-600">Более 100,000 довольных клиентов</p>
          </motion.div>

          <motion.div
            className="grid grid-cols-1 md:grid-cols-3 gap-8"
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true }}
          >
            {categoryData.testimonials.map((testimonial, i) => (
              <motion.div
                key={i}
                variants={itemVariants}
                whileHover={{ y: -10 }}
                className="bg-white p-8 rounded-3xl shadow-xl"
              >
                <div className="text-5xl mb-4">💬</div>
                <p className="text-lg italic mb-4 text-gray-700">"{testimonial.text}"</p>
                <p className="font-bold" style={{ color: categoryData.color }}>
                  — {testimonial.author}
                </p>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* 9. FAQ */}
      <section className="py-20 bg-white">
        <div className="container mx-auto px-4 max-w-4xl">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <h2 className="text-5xl font-black mb-4">Часто задаваемые вопросы</h2>
            <p className="text-xl text-gray-600">Ответы на популярные вопросы</p>
          </motion.div>

          <div className="space-y-4">
            {[
              { q: 'Как начать пользоваться ботом?', a: `Просто откройте Telegram, найдите @${bot.name}_bot и нажмите Start. Бот сразу готов к работе!` },
              { q: 'Какие способы оплаты доступны?', a: 'Мы принимаем банковские карты, PayPal, криптовалюты и Telegram Stars.' },
              { q: 'Можно ли отменить подписку?', a: 'Да, вы можете отменить подписку в любой момент без штрафов и скрытых платежей.' },
              { q: 'Есть ли бесплатный пробный период?', a: 'Да! Все новые пользователи получают 7 дней бесплатного доступа к Pro версии.' },
            ].map((faq, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                transition={{ delay: i * 0.1 }}
                viewport={{ once: true }}
                className="bg-gray-50 rounded-2xl overflow-hidden border-2 border-gray-100"
              >
                <div className="p-6 font-bold text-xl" style={{ color: categoryData.color }}>
                  {faq.q}
                </div>
                <div className="px-6 pb-6 text-gray-700">
                  {faq.a}
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* 10. Final CTA */}
      <section
        className="py-32 text-white text-center"
        style={{
          background: `linear-gradient(135deg, ${categoryData.color} 0%, ${categoryData.color}dd 100%)`,
        }}
      >
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            whileInView={{ scale: 1, opacity: 1 }}
            viewport={{ once: true }}
          >
            <h2 className="text-6xl font-black mb-6">Готовы начать?</h2>
            <p className="text-2xl mb-8 opacity-90">
              Присоединяйтесь к 100,000+ пользователям уже сегодня
            </p>
            <motion.a
              href="https://t.me/bot"
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.95 }}
              className="inline-block bg-white text-gray-900 px-12 py-5 rounded-full font-bold text-xl shadow-2xl"
            >
              Начать бесплатно
            </motion.a>
          </motion.div>
        </div>
      </section>
    </div>
  );
};

export default BotDetailsPage;
