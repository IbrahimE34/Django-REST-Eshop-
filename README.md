Eshop API —  проект интернет-магазина, разработанный с использованием Django REST Framework. Проект включает систему регистрации пользователей, JWT-аутентификацию, управление товарами, корзиной и заказами, а также реализует бизнес-логику обработки заказов с использованием транзакций.

# 🛒 Eshop API

REST API интернет-магазина, разработанный на Django REST Framework.

## 🚀 Возможности

- Регистрация пользователей
- JWT-аутентификация
- CRUD товаров
- Категории товаров
- Корзина пользователя
- Добавление товаров в корзину
- Очистка корзины
- Оформление заказа
- Изменение статусов заказа
- Отмена заказа
- Проверка остатков товаров
- Автоматическое уменьшение количества товаров на складе
- Транзакции при оформлении заказа (`transaction.atomic`)
- Поиск товаров
- Фильтрация
- Сортировка
- Пагинация

---

# 🛠 Используемые технологии

- Python 3
- Django
- Django REST Framework
- SQLite
- Simple JWT
- Django Filter
- python-decouple

---

# 📂 Структура проекта

```text
Eshop
│
├── product
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
│
├── order
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── admin.py
│   └── urls.py
│
├── user
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── requirements.txt
├── manage.py
└── README.md
```

---

# 🔐 JWT

Получить Access и Refresh Token

```
POST /api/token/
```

Обновить Access Token

```
POST /api/token/refresh/
```

Проверить Token

```
POST /api/token/verify/
```

---

# 📦 Основные API

## Product

```
GET     /api/products/
GET     /api/products/{id}/
POST    /api/products/
PUT     /api/products/{id}/
DELETE  /api/products/{id}/
```

---

## Cart

```
GET     /api/carts/
POST    /api/carts/
POST    /api/carts/{id}/clear/
POST    /api/carts/{id}/checkout/
```

---

## Order

```
GET     /api/orders/
POST    /api/orders/{id}/pay/
POST    /api/orders/{id}/processing/
POST    /api/orders/{id}/ship/
POST    /api/orders/{id}/deliver/
POST    /api/orders/{id}/cancel/
```

---

# ⚙ Установка

Клонировать репозиторий

```bash
git clone https://github.com/your_username/Eshop.git
```

Перейти в папку проекта

```bash
cd Eshop
```

Создать виртуальное окружение

```bash
python -m venv venv
```

Активировать окружение

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Установить зависимости

```bash
pip install -r requirements.txt
```

Создать файл `.env`

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

Применить миграции

```bash
python manage.py migrate
```

Запустить сервер

```bash
python manage.py runserver
```

---

# 👨‍💻 Автор

Backend разработчик на Python / Django REST Framework.
