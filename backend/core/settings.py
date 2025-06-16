import os
from pathlib import Path
import pymysql

# Use PyMySQL as MySQLdb replacement
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-change-this-in-production')

# Debug settings - MUST BE AT THE TOP
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*']  # Added * for debugging

# Force disable all HTTPS redirects for development
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = None
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'corsheaders',

    # Third-party apps
    'crispy_forms',
    'crispy_bootstrap5',
    'widget_tweaks',
    'rest_framework',

    # Local apps
    'accounts.apps.AccountsConfig',
    'companies.apps.CompaniesConfig',
    'employees.apps.EmployeesConfig',
]

# Debug middleware class
class DebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if DEBUG:
            print(f"DEBUG: Request method: {request.method}")
            print(f"DEBUG: Request path: {request.path}")
            print(f"DEBUG: Request scheme: {request.scheme}")
            print(f"DEBUG: Request is_secure: {request.is_secure()}")
            print(f"DEBUG: HTTP_X_FORWARDED_PROTO: {request.META.get('HTTP_X_FORWARDED_PROTO', 'Not set')}")
        
        response = self.get_response(request)
        
        if DEBUG:
            print(f"DEBUG: Response status: {response.status_code}")
            if hasattr(response, 'url'):
                print(f"DEBUG: Response redirect URL: {response.url}")
        
        return response

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'core.settings.DebugMiddleware',  # Debug middleware first
    # 'django.middleware.security.SecurityMiddleware',  # COMMENTED OUT FOR DEBUGGING
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Always use MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'erp'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'Prachi@8287'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}

# Add debug database logging
if DEBUG:
    print(f"DEBUG: settings.DATABASES = {DATABASES}")

# Custom user model
AUTH_USER_MODEL = 'accounts.User'

# Password validation - simplified for debugging
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Simplified static files handling for debugging
if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Login/Logout URLs
# LOGIN_REDIRECT_URL = 'accounts:dashboard'
# LOGOUT_REDIRECT_URL = 'accounts:account_login'
# LOGIN_URL = 'accounts:account_login'

# Email settings - simplified for debugging
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Sites Framework
SITE_ID = 1

# Debug toolbar

# Production security settings (only if not in debug mode)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
    "http://localhost:3002",
    "http://127.0.0.1:3002",
]

CORS_ALLOW_CREDENTIALS = True

# # Django REST Framework settings
# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#     ],
#     'DEFAULT_PARSER_CLASSES': [
#         'rest_framework.parsers.JSONParser',
#     ],
#     'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     )
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

print(f"DEBUG MODE: {DEBUG}")
print(f"SECURE_SSL_REDIRECT: {SECURE_SSL_REDIRECT}")
print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'django.request': {
        'handlers': ['console'],
        'level': 'DEBUG',  # Set to DEBUG to see all request logs
        'propagate': False,
    },
}