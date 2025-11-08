import { useState } from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { BOTS, CATEGORY_CONTENT } from '../data/bots';

const HomePage = () => {
  const [selectedCategory, setSelectedCategory] = useState('ALL');

  const categories = ['ALL', ...new Set(BOTS.map(bot => bot.category))];

  const filteredBots = selectedCategory === 'ALL'
    ? BOTS
    : BOTS.filter(bot => bot.category === selectedCategory);

  return (
    <div className="min-h-screen">
      {/* Hero Section with Animated Background */}
      <section className="relative bg-gradient-to-br from-purple-900 via-blue-900 to-pink-900 text-white py-32 overflow-hidden">
        {/* Animated Background Elements */}
        <div className="absolute inset-0 opacity-20">
          {[...Array(20)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute bg-white rounded-full"
              style={{
                width: Math.random() * 100 + 50,
                height: Math.random() * 100 + 50,
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
              }}
              animate={{
                y: [0, -30, 0],
                opacity: [0.3, 0.6, 0.3],
              }}
              transition={{
                duration: Math.random() * 3 + 2,
                repeat: Infinity,
                delay: Math.random() * 2,
              }}
            />
          ))}
        </div>

        <div className="container mx-auto px-4 relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center"
          >
            <motion.h1
              className="text-6xl md:text-8xl font-black mb-6"
              initial={{ scale: 0.5 }}
              animate={{ scale: 1 }}
              transition={{ duration: 0.5 }}
            >
              🤖 20 Лучших
              <br />
              <span className="text-gradient from-yellow-300 to-pink-300">
                Telegram Ботов
              </span>
            </motion.h1>

            <motion.p
              className="text-xl md:text-2xl mb-8 opacity-90"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.3 }}
            >
              Автоматизируйте бизнес, экономьте время, увеличивайте прибыль
            </motion.p>

            <motion.div
              className="flex justify-center gap-4"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.5 }}
            >
              <motion.a
                href="#catalog"
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.95 }}
                className="bg-white text-purple-900 px-8 py-4 rounded-full font-bold text-lg shadow-2xl hover:shadow-3xl transition"
              >
                Смотреть каталог
              </motion.a>
            </motion.div>

            {/* Stats */}
            <motion.div
              className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-16"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.7 }}
            >
              {[
                { num: '20', label: 'Ботов' },
                { num: '11', label: 'Категорий' },
                { num: '100K+', label: 'Пользователей' },
                { num: '4.9/5', label: 'Рейтинг' },
              ].map((stat, i) => (
                <motion.div
                  key={i}
                  className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20"
                  whileHover={{ scale: 1.05 }}
                >
                  <h3 className="text-4xl font-black text-yellow-300">{stat.num}</h3>
                  <p className="text-sm opacity-80">{stat.label}</p>
                </motion.div>
              ))}
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* Category Filter */}
      <section id="categories" className="py-12 bg-gray-100">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            className="flex flex-wrap justify-center gap-4"
          >
            {categories.map((cat) => (
              <motion.button
                key={cat}
                onClick={() => setSelectedCategory(cat)}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className={`px-6 py-3 rounded-full font-semibold transition ${
                  selectedCategory === cat
                    ? 'bg-gradient-to-r from-purple-600 to-pink-600 text-white shadow-lg'
                    : 'bg-white text-gray-700 hover:bg-gray-50'
                }`}
              >
                {cat === 'ALL' ? '🌟 Все' : `${CATEGORY_CONTENT[cat]?.emoji || ''} ${cat}`}
              </motion.button>
            ))}
          </motion.div>
        </div>
      </section>

      {/* Bots Grid */}
      <section id="catalog" className="py-20">
        <div className="container mx-auto px-4">
          <motion.div
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8"
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            transition={{ staggerChildren: 0.1 }}
          >
            {filteredBots.map((bot, index) => {
              const categoryData = CATEGORY_CONTENT[bot.category];
              return (
                <motion.div
                  key={bot.id}
                  initial={{ opacity: 0, y: 50 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.05 }}
                  viewport={{ once: true }}
                >
                  <Link to={`/bot/${bot.id}`}>
                    <motion.div
                      className="bg-white rounded-3xl shadow-xl overflow-hidden h-full hover:shadow-2xl transition-all duration-300 border-2 border-transparent hover:border-purple-300"
                      whileHover={{ y: -10, scale: 1.02 }}
                      style={{
                        background: `linear-gradient(135deg, ${categoryData?.color}15 0%, white 100%)`,
                      }}
                    >
                      {/* Header with Category Color */}
                      <div
                        className="p-6 text-white relative overflow-hidden"
                        style={{
                          background: `linear-gradient(135deg, ${categoryData?.color} 0%, ${categoryData?.color}dd 100%)`,
                        }}
                      >
                        <div className="absolute top-0 right-0 text-9xl opacity-10">
                          {categoryData?.emoji}
                        </div>
                        <div className="relative z-10">
                          <span className="text-5xl mb-2 block">{categoryData?.emoji}</span>
                          <h3 className="text-2xl font-bold mb-2">{bot.name}</h3>
                          <p className="text-sm opacity-90">{bot.category}</p>
                        </div>
                      </div>

                      {/* Content */}
                      <div className="p-6">
                        <p className="text-lg font-semibold text-gray-800 mb-2">
                          {bot.tagline}
                        </p>
                        <p className="text-sm text-gray-600 mb-4">{bot.subtitle}</p>

                        {/* Price Badge */}
                        <div className="flex items-center justify-between">
                          <span
                            className="px-4 py-2 rounded-full text-white font-bold text-lg"
                            style={{ backgroundColor: categoryData?.color }}
                          >
                            {bot.price}/мес
                          </span>
                          <motion.span
                            whileHover={{ x: 5 }}
                            className="text-2xl"
                          >
                            →
                          </motion.span>
                        </div>
                      </div>
                    </motion.div>
                  </Link>
                </motion.div>
              );
            })}
          </motion.div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
