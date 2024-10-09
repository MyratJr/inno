from django.urls import reverse_lazy
from django.templatetags.static import static
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-t2ov=ys0nxuaa_o))6bafm#kti#x1dw)l=q76u$axteqf_ibge'

DEBUG = True

ALLOWED_HOSTS = ["*"]



INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "Nis_app"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Nis.urls'


UNFOLD = {
    "SITE_TITLE": "Innovation system",
    "SITE_HEADER": "Innovation system",
    "SITE_URL": "/",
    "SITE_ICON": lambda request: static("unfold/images/green-energy.png"),
    "SITE_LOGO": lambda request: static("unfold/images/green-energy.png"),
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": None,
    "LOGIN": {
        # "image": lambda request: static("unfold/images/aadwords.png"),
        "redirect_after": lambda request: reverse_lazy("admin:index"),
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "ru": lambda request: static("unfold/images/russia.png"),
                "tk": "TM",
                "en": "🇬🇧",
            },
        },
    },
    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": False,
        "navigation": [
            {
                "items": [
                    {
                        "title": "Home",
                        "icon": "home",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": "Users",
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": "Countries",
                        "icon": "flag",
                        "link": reverse_lazy("admin:Nis_app_country_changelist"),
                    },
                    {
                        "title": "Innovation Practices",
                        "icon": "monitoring",
                        "link": reverse_lazy("admin:Nis_app_innovationpractice_changelist"),
                    },
                    {
                        "title": "Messages",
                        "icon": "mail",
                        "link": reverse_lazy("admin:Nis_app_message_changelist"),
                    },
                ]
            },
        ],
    },
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Nis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = 'static/'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'