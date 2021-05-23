from pathlib import Path
import os
import environ

env = environ.Env()
environ.Env.read_env()
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY= env('SECRET_KEY')
DEBUG=True
ALLOWED_HOSTS=['172.25.0.2', '127.0.0.1', 'localhost']
GARTEN_POST_API=env('INTERNAL_SYSTEM_IP')
INSTALLED_APPS=[
    'garten.apps.GartenConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MIDDLEWARE=[
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF='kindergarten.urls'
TEMPLATES=[{
        'BACKEND':'django.template.backends.django.DjangoTemplates',
        'DIRS':[os.path.join(BASE_DIR,'templates')],
        'APP_DIRS':True,
        'OPTIONS':{
            'context_processors':[
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION='kindergarten.wsgi.application'
DATABASES={
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
    # read os.environ['SQLITE_URL']
    'extra': env.db('SQLITE_URL', default='sqlite:///.db.sqlite3')

}
AUTH_PASSWORD_VALIDATORS=[{
        'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },{
        'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator',
    },{
        'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator',
    },{
        'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
USE_I18N=True
USE_L10N=True
USE_TZ=True
STATIC_URL='/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
STATIC_ROOT=os.path.join(BASE_DIR,'assets')
MEDIA_URL='/images/'
MEDIA_ROOT=os.path.join(BASE_DIR,'images')
