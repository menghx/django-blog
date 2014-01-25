DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('menghx', 'mhxdev@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

USE_I18N = True

USE_L10N = False

USE_TZ = False

DATE_FORMAT = 'Y-m-d'

DATE_INPUT_FORMATS = ('Y-m-d',)

DATETIME_FORMAT = 'Y-m-d'
#DATETIME_FORMAT = 'Y-m-d H:M:S'

DATETIME_INPUT_FORMATS = ('Y-m-d H:M:S', )

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

import os
STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'static').replace('\\','/'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

SECRET_KEY = '&!+*ecyg7us9os231%@z__b9lm%6%+_j8o)z4zy6c)!^itl^ph'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mxsite.urls'

WSGI_APPLICATION = 'mxsite.wsgi.application'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'ckeditor',
    'mxblog',
)

CKEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), '..', 'static/ufiles').replace('\\', '/')
CKEDITOR_UPLOAD_PREFIX = "http://127.0.0.1:8000/static/ufiles/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 600,
        'width': 1000,
    },
}


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}