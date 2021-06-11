# Kindergarden external

## Team
AM: it21840  
AM: it21848  
AM: it21666  

# Clone and run project


```bash
git clone https://github.com/vasKatevas/kindergarten-External
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cp kindergartent/kindergarten/.env.development kindergartent/kindergarten/.env
```
edit kindergartent/kindergarten/.env file to define
```vim
SECRET_KEY='test123'
DATABASE_URL=mysql://djangouser:p@sSword123@localhost:3306/kindergartenExternal
INTERNAL_SYSTEM_IP='http://localhost:8080'
```
## Run test
(requires [kindergarten-Internal](https://github.com/vasKatevas/kindergarten-Internal))
```bash
python manage.py test
```

## Run development server
```bash
cd kindergartent
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Run with gunicorn
```bash
cd kindergartent
chmod u+x app.sh
./app.sh
```
