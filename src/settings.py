from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-dydz0tayt3f672*ewbrylq%fx8^9sms50uvpref@37#ya6$@*i"

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "users",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware", #這一段放在第一位
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "src.urls"
AUTH_USER_MODEL = 'users.CustomUser'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  #SMTP伺服器
EMAIL_PORT = 587  #TLS通訊埠號
EMAIL_USE_TLS = True  #開啟TLS(傳輸層安全性)
EMAIL_HOST_USER = 'ryowu0329@gmail.com'  #寄件者電子郵件
EMAIL_HOST_PASSWORD = 'xuypqcnbsmmxaypo'  #Gmail應用程式的密碼(不是登入密碼哦、16個字)


CSRF_TRUSTED_ORIGINS = [
    "http://ryowuandjanet-bug-free-couscous-9gpg49q9wwfpgjq-3000.preview.app.github.dev",
    "https://ryowuandjanet-bug-free-couscous-9gpg49q9wwfpgjq-3000.preview.app.github.dev",
] #發起請求的URL要求添加埠和http

CORS_ALLOWED_ORIGINS = [
    "http://ryowuandjanet-bug-free-couscous-9gpg49q9wwfpgjq-3000.preview.app.github.dev",
    "https://ryowuandjanet-bug-free-couscous-9gpg49q9wwfpgjq-3000.preview.app.github.dev",
] # 發起請求的位址，不需要添加http和埠

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "src.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
