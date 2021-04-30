# Kindergarden external

## Team
AM: it21840  
AM: it21848  
AM: it21666  

# Clone and run project

```bash
git clone https://github.com/vasKatevas/DS-2020-External
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cp kinder/.env.example kinder/.env
```
edit kinder/.env file to define
```vim
SECRET_KEY='test123'
DATABASE_URL=mysql://djangouser:p@sSword123@localhost:3306/kindergartenExternal
INTERNAL_SYSTEM_IP='http://localhost:8080'
```
# Run test
(requires [SpringBoot project](https://github.com/vasKatevas/springBoot))
```bash
python manage.py test
```

# Run development server
```bash
python manage.py runserver
```
