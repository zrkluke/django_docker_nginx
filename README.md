# Dockerizing Django + PostgreSQL + Nginx in local environment
---
## Environment Variables
For convenience of demostration, environment variables have been listed in .env files.



**Change SECRET_KEY for security.**
```
# python manage.py shell
from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
print(secret_key)
```


**Replace SECRET_KEY value in settings.py**
```
# core/settings.py

SECRET_KEY = secret_key
```


---
## Install
Install [Docker](https://docs.docker.com/get-docker/), if you don't have it before.

Build Docker image and run containers:
```
$ docker-compose up -d --build
```

Open browser to http://localhost/ to view the login page.
![localhost image](https://imageupload.io/ib/7rh6pXReHx86cBS_1698435938.png)

---
## Bonus: employee_user
Use (account, password) = (employee_user, initium) login, "You are 'Employee'" will be displayed.
![employee login image](https://imageupload.io/ib/hRHDj2OmiHmfFVs_1698436016.png)
