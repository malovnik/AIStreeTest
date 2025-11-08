import { FaGithub, FaTelegram, FaTwitter } from 'react-icons/fa';

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white py-12 mt-20">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="text-xl font-bold mb-4">📱 Telegram Bots Catalog</h3>
            <p className="text-gray-400">
              Лучшая коллекция Telegram ботов для автоматизации бизнеса и повышения продуктивности.
            </p>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4">Категории</h4>
            <ul className="space-y-2 text-gray-400">
              <li className="hover:text-white transition">🤖 AI & Machine Learning</li>
              <li className="hover:text-white transition">💰 Криптовалюты</li>
              <li className="hover:text-white transition">🛒 E-commerce</li>
              <li className="hover:text-white transition">📱 Социальные сети</li>
              <li className="hover:text-white transition">🎵 Музыка</li>
            </ul>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4">Связь</h4>
            <div className="flex space-x-4">
              <a
                href="https://github.com"
                target="_blank"
                rel="noopener noreferrer"
                className="text-2xl hover:text-purple-400 transition"
              >
                <FaGithub />
              </a>
              <a
                href="https://t.me"
                target="_blank"
                rel="noopener noreferrer"
                className="text-2xl hover:text-blue-400 transition"
              >
                <FaTelegram />
              </a>
              <a
                href="https://twitter.com"
                target="_blank"
                rel="noopener noreferrer"
                className="text-2xl hover:text-sky-400 transition"
              >
                <FaTwitter />
              </a>
            </div>
          </div>
        </div>

        <div className="border-t border-gray-800 mt-8 pt-6 text-center text-gray-400">
          <p>&copy; 2025 Telegram Bots Catalog. Все права защищены.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
