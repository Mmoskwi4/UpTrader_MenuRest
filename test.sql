-- Очистка существующих данных
DELETE FROM menu_app_menuitem;

-- Сброс автоинкремента
UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'menu_app_menuitem';

-- Основное меню (main_menu)
INSERT INTO menu_app_menuitem (name, menu_name, url, named_url, parent_id, order) VALUES
-- Главная страница
('Главная', 'main_menu', '', 'home', NULL, 0),

-- О компании
('О компании', 'main_menu', '', '', NULL, 1),
('О нас', 'main_menu', '/about/', '', 2, 0),
('Команда', 'main_menu', '/team/', '', 2, 1),
('Вакансии', 'main_menu', '/careers/', '', 2, 2),

-- Услуги
('Услуги', 'main_menu', '', '', NULL, 2),
('Веб-разработка', 'main_menu', '/services/web/', '', 6, 0),
('Мобильные приложения', 'main_menu', '/services/mobile/', '', 6, 1),
('Дизайн', 'main_menu', '/services/design/', '', 6, 2),
('Консультации', 'main_menu', '/services/consulting/', '', 6, 3),

-- Портфолио
('Портфолио', 'main_menu', '/portfolio/', '', NULL, 3),

-- Блог
('Блог', 'main_menu', '', '', NULL, 4),
('Все статьи', 'main_menu', '/blog/', '', 12, 0),
('Технологии', 'main_menu', '/blog/tech/', '', 12, 1),
('Дизайн', 'main_menu', '/blog/design/', '', 12, 2),
('Маркетинг', 'main_menu', '/blog/marketing/', '', 12, 3),

-- Контакты
('Контакты', 'main_menu', '/contact/', '', NULL, 5);

-- Боковое меню (sidebar_menu)
INSERT INTO menu_app_menuitem (name, menu_name, url, named_url, parent_id, order) VALUES
('Категории', 'sidebar_menu', '', '', NULL, 0),
('Программирование', 'sidebar_menu', '/categories/programming/', '', 18, 0),
('Python', 'sidebar_menu', '/categories/python/', '', 19, 0),
('Django', 'sidebar_menu', '/categories/django/', '', 19, 1),
('JavaScript', 'sidebar_menu', '/categories/javascript/', '', 19, 2),
('Дизайн', 'sidebar_menu', '/categories/design/', '', 18, 1),
('UI/UX', 'sidebar_menu', '/categories/ui-ux/', '', 23, 0),
('Графический дизайн', 'sidebar_menu', '/categories/graphic-design/', '', 23, 1),
('Маркетинг', 'sidebar_menu', '/categories/marketing/', '', 18, 2);

-- Футер меню (footer_menu)
INSERT INTO menu_app_menuitem (name, menu_name, url, named_url, parent_id, order) VALUES
('Правовая информация', 'footer_menu', '', '', NULL, 0),
('Политика конфиденциальности', 'footer_menu', '/privacy/', '', 27, 0),
('Условия использования', 'footer_menu', '/terms/', '', 27, 1),
('Cookie', 'footer_menu', '/cookie/', '', 27, 2),
('Поддержка', 'footer_menu', '', '', NULL, 1),
('Помощь', 'footer_menu', '/help/', '', 31, 0),
('FAQ', 'footer_menu', '/faq/', '', 31, 1),
('Сообщество', 'footer_menu', '/community/', '', 31, 2);