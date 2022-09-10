#'Project config

# Add app to settings.py
INSTALLED_APPS = [ … , 'app_name' ]

# App templates folder
create folder appfolder/templates/appname

# Project templates folder: 
create folder projectname/templates

# settings.py template config
Project templates settings.py: 
    TEMPLATES = [
        { …
                'DIRS': [BASE_DIR / 'templates', ],
        … }

# Create Static folder: 
project_name\static\

# Static folder (settings.py): 
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ] 
STATIC_ROOT = 'static_root'

# To use PostgresSQL
# pip install psycopg2
# settings.py
DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'admin',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432'