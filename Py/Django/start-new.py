#'Start a new Django project

# Create et access project folder
~$  mkdir project_name
~$  cd project_name

# Create Python virtual env 
~$  python3 -m venv venv

# Activate virtual env
~$  source venv/bin/activate

# Deactivate virtual env
~$  deactivate

# If requirements already exist
~$  pip install -r requirements.txt

# Freeze requirements in a file
~$  pip freeze > requirements.txt

# Install django
~$  pip install django~=3.1.0 

# New django project (from project_name folder)
~$  django-admin startproject config .

# Create app (from project_name folder)
~$  python manage.py startapp app_name

# Migration
~$  python manage.py makemigrations 
~$  python manage.py migrate

# Create superuser
~$  python manage.py createsuperuser

# Start server
~$  python manage.py runserver  => ex.  http://127.0.0.1:8000

# Current project shell example
~$ python manage.py shell
 >>> from app_name.models import User
 >>> user1 = User.objects.first()

# Prepare static folders fpor production
$ python manage.py collectstatic

# Take all data from app blog and export in json
python manage.py dumpdata blog >myapp.json

# Take all data in json file and import in app data table
python manage.py loaddata myapp.json