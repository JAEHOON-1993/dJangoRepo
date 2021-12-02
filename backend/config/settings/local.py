from config.settings.base import *


DEBUG = True

ALLOWED_HOSTS += ['*']

CORS_ALLOW_ALL_ORIGINS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'admin123!',
#         'HOST': 'database-2.cxhta3eej7on.ap-northeast-2.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }


# REDIS
REDIS_HOST = 'localhost'

# CHANNELS
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(REDIS_HOST, 6379)],
        },
    },
}

# CELERY
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:6379/0'

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'app_formatter': {
            'format': '[{levelname}] [{name}:{lineno} {funcName}] {message}',
            'style': '{',
        },
        'simple_formatter': {
            'format': '{message}',
            'style': '{',
        }
    },
    'handlers': {
        'app_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'app_formatter',
        },
        'simple_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple_formatter',
        },
    },
    'loggers': {
        'app': {
            'handlers': ['app_console'],
            'level': 'DEBUG',
        },
        'request': {
            'handlers': ['simple_console'],
            'level': 'INFO',
        },
        'django.request': {
            'level': 'ERROR',
        },
        'django.db.backends': {
            'handlers': ['simple_console'],
            'level': 'DEBUG',
        },
    },
}
