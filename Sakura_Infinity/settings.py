# -*- coding: utf-8 -*-

import os
import sys
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

SECRET_KEY = 'django-insecure-j**=7l4rg&zqyjbui9qyoe^#c(-5a#2^(iu%2jz0@)fjfn9%rm'

DEBUG = True

ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = "oauth.Users"

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'bootstrap4',
    'crispy_forms',
    'rest_framework',
    'django_celery_beat',  # 定时任务
    'django_celery_results',  # 查看 celery 执行结果
    'rest_framework.authtoken',
    'django_filters',
    'apps.oauth',
    'apps.project',
    'apps.element',
    'apps.tool'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 注意顺序，必须放在这儿
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'Sakura_Infinity.urls'

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

WSGI_APPLICATION = 'Sakura_Infinity.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sakura_infinity',
        'USER': 'sakura_infinity',
        'PASSWORD': 'admin',
        'HOST': '120.79.24.202',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8'}
    }
}

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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

REST_FRAMEWORK = {
    # 用户认证
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication', ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',  # 分页功能
    'PAGE_SIZE': 50  # 一页可现实数据条数
}

# check 扫描相关
CHECK_SHELL_PATH = '/Users/reda-flight/Desktop/djwork/Sakura_Infinity/toolsrc/dependency-check/bin/dependency-check.sh'  # check.sh 脚本路径 task 执行时的路径

#  celery 定时任务
CELERY_BEAT_SCHEDULE = {
    'update_checktask_table_task': {  # 更新任务表任务
        'task': 'tool.tasks.update_checktask_table_task',
        'schedule': timedelta(seconds=10),  # 每10秒执行一次
    },
    'delete_result_data_task': {  # 删除数据任务
        'task': 'tool.tasks.delete_result_data_task',  # AppName应用的tasks.py文件中的方法名
        'schedule': timedelta(hours=1),  # 每1小时执行
    }
}

############### 工具相关配置

# AES加解密 默认参数配置
KEY = '0000000000000000'
IV = 'aaaaaaaaaaaaaaaa'

# ftp工具下载路径
FTP_PATH = '/upload/tool/FTPdownload.zip'

############### celery 相关配置

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
DJANGO_CELERY_BEAT_TZ_AWARE = False
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'  # celery 结果返回，可用于跟踪结果
CELERY_RESULT_BACKEND = 'django-db'  # 使用 database 作为结果存储
CELERY_CACHE_BACKEND = 'django-cache'  # celery 后端缓存
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERYD_MAX_TASKS_PER_CHILD = 50  # 由于长期运行会导致内存不释放，需要设置池子回收
CELERYD_CONCURRENCY = 5  # worker的并发数

###### 日志相关
cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)  # 如果不存在这个logs文件夹，就自动创建一个

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s]--%(message)s'
        },
    },
    'handlers': {
        # 输出日志的控制台
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        # 输出日志到文件，按日期滚动
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/Sakura_Infinity.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 100,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        # 不同的logger
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
