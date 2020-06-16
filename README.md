# matific

this project is created for the matific assignment 

## documents
	data_structure.xlsx - contains project data structure
	ERD.jpeg - ERD visualization 
	
## rest-api
	contains the python project files

## database 
	this project is configured to run with mysqldb
	to change the database please change thee below section in `settings.py`
	
	`DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'sample',
			'USER': 'root',
			'PASSWORD': 'secret',
			'HOST': 'localhost',
			'PORT': '3306',
		}
	}`
	
###	to start service : 
	`cd <rest-api>`
	`virtualenv venv --python=python3`
	`pip install -r requrements.txt` -  to install required dependacies
	`python manage.py makemigrations`  - to generate db scripts
	
	`python manage.py migrate` - to create database tables
	
	`python manage.py createsuperuser ` - to create super user 
	
	`python manage.py runserver` - to start the server