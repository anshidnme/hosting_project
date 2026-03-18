# Webo Dashboard — Django Product Dashboard

## Quick Setup (Windows PowerShell)

```powershell
# 1. Navigate to project folder
cd webo_dashboard

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Run database migrations
python manage.py makemigrations accounts
python manage.py makemigrations products
python manage.py makemigrations cart
python manage.py migrate

# 5. Create admin superuser
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```

Then open: http://127.0.0.1:8000

---

## Google OAuth Setup

1. Go to https://console.cloud.google.com
2. Create a new project → APIs & Services → Credentials
3. Create OAuth 2.0 Client ID (Web application)
4. Add Authorized redirect URI:
   `http://localhost:8000/social-auth/complete/google-oauth2/`
5. Set environment variables before running:

```powershell
$env:GOOGLE_CLIENT_ID="your_client_id_here"
$env:GOOGLE_CLIENT_SECRET="your_client_secret_here"
python manage.py runserver
```

---

## Project Structure

```
webo_dashboard/
├── manage.py
├── requirements.txt
├── README.md
├── webo_dashboard/        ← Django config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/              ← Auth (login, register, Google OAuth)
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── products/              ← Product CRUD
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── cart/                  ← Cart, Checkout, Orders
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── context_processors.py
│   └── admin.py
├── templates/
│   ├── base.html
│   ├── registration/
│   │   ├── login.html
│   │   └── register.html
│   ├── products/
│   │   ├── list.html
│   │   ├── detail.html
│   │   ├── form.html
│   │   └── confirm_delete.html
│   └── cart/
│       ├── cart.html
│       ├── checkout.html
│       └── success.html
└── static/

```

## Features

- Google Social Login + standard registration with full validation
- Product dashboard: Add, Edit, Delete, View products with images
- Shopping cart with quantity management
- Checkout flow with order confirmation
- Animated success page
- Fully responsive Bootstrap 5 UI
- Django admin panel at /admin/
