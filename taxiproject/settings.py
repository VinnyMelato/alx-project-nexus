"""
Django settings for taxiproject project.
"""

import os
from pathlib import Path
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔑 Security
SECRET_KEY = config("DJANGO_SECRET_KEY")

# 🛠️ Debug mode (default: False if not in .env)
DEBUG = config("DEBUG", default=False, cast=bool)

# 🌍 Allowed hosts (comma-separated in .env)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost").split(",")

# 💾 Database
DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="sqlite:///db.sqlite3")
    )
}

# Application definition
INSTALLED_APPS = [
    "taxi_app",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Static file handling
]

ROOT_URLCONF = "taxiproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "taxiproject.context_processors.google_maps_api_key",
            ],
        },
    },
]

WSGI_APPLICATION = "taxiproject.wsgi.application"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 📁 Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "taxi_app/static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# 📁 Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
