import os

import requests

from config.settings.base import *


DEBUG = True

ALLOWED_HOSTS += ['*']

try:
    EC2_PRIVATE_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout=0.1).text
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)
except requests.exceptions.RequestException as e:
    print('no ec2 instance')

CORS_ALLOW_ALL_ORIGINS = True

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'admin123!'
DB_PORT = '5432'
DB_WRITER_HOST = 'database-2.cxhta3eej7on.ap-northeast-2.rds.amazonaws.com'
DB_READER_HOST = 'database-2.cxhta3eej7on.ap-northeast-2.rds.amazonaws.com'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_WRITER_HOST,
        'PORT': DB_PORT,
    },
    'reader': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_READER_HOST,
        'PORT': DB_PORT,
    },
}

# REDIS
REDIS_HOST = os.getenv('REDIS_HOST')

# CHANNELS
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(REDIS_HOST, 6379)],
        },
    },
}

# CELERY
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:6379/0'


# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'sensitive_filter': {
            '()': 'config.filters.SensitiveFilter',
        },
    },
    'formatters': {
        'app_formatter': {
            'format': '[{levelname}] [{name}:{lineno} {funcName}] {message}',
            'style': '{',
        },
        'request_formatter': {
            'format': '[{levelname}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'app_console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'app_formatter',
        },
        'request_console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'request_formatter',
            'filters': ['sensitive_filter'],
        },
    },
    'loggers': {
        'app': {
            'handlers': ['app_console'],
            'level': 'INFO',
        },
        'request': {
            'handlers': ['request_console'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['app_console'],
            'level': 'ERROR',
        },
    },
}