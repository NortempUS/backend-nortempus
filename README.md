# backend-nortempus

## Deploy

Clone repository

```bash
 git clone https://github.com/Task4Task/backend-task4task.git
 cd backend-task4task
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
python manage.py makemigrations category chat chatmess services users userservice
python manage.py migrate
python manage.py runserver
```
