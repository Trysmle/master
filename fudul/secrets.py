SECRET_KEY = '8#P$gR&2uJr^xT@k9!N$Yjz#VbFz^tL$w'
DEBUG = True  # أو False في بيئة الإنتاج
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'your-database-name.sqlite3',
    }
}
