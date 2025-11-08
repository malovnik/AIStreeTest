import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';

const Header = () => {
  return (
    <motion.header
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      className="bg-gradient-to-r from-purple-600 via-pink-600 to-blue-600 text-white shadow-lg sticky top-0 z-50"
    >
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <Link to="/">
            <motion.div
              whileHover={{ scale: 1.05 }}
              className="flex items-center space-x-3"
            >
              <span className="text-4xl">🤖</span>
              <div>
                <h1 className="text-2xl font-bold">Telegram Bots Catalog</h1>
                <p className="text-sm opacity-90">20 лучших ботов для бизнеса</p>
              </div>
            </motion.div>
          </Link>

          <nav className="hidden md:flex space-x-6">
            <Link
              to="/"
              className="hover:text-yellow-300 transition duration-300"
            >
              Главная
            </Link>
            <a
              href="#categories"
              className="hover:text-yellow-300 transition duration-300"
            >
              Категории
            </a>
            <a
              href="https://github.com"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-yellow-300 transition duration-300"
            >
              GitHub
            </a>
          </nav>
        </div>
      </div>
    </motion.header>
  );
};

export default Header;
