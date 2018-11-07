# django-bind

Try POC:

You need Python3 (tested with 3.6 - but 3.5+ should work) and virtualenv.

```
git clone https://github.com/mathiasertl/django-bind.git
cd django-bind
virtualenv -p /usr/bin/python3 .
source bin/activate
pip install -U pip setuptools
pip install -r requirements.txt

cd bind
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata testdata.json 
python manage.py runserver
```

And visit http://localhost:8000/admin/:

* See macros you can define at will: http://localhost:8000/admin/django_bind/macro/
* See zones you can create: http://localhost:8000/admin/django_bind/zone/
