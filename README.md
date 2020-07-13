### REST API for managing thread posts

#### Deploy locally

```
#!/bin/bash

git clone https://github.com/thestics/thread_api_django.git thread_api
cd thread_api
docker-compose up
```

#### Add user with write permissions

- Find django containter id
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
c795553f1809        thread_api          "python3 manage.py r…"   42 minutes ago      Up 40 minutes       0.0.0.0:8000->8000/tcp   thread_api_web_1
9c8e7c962c52        postgres            "docker-entrypoint.s…"   42 minutes ago      Up 40 minutes       0.0.0.0:5432->5432/tcp   thread_api_db_1
````
In this case id is `c795553f1809`

- Add superuser user
```
docker exec -it <CONTAINER_ID> python3 manage.py createsuperuser
```

#### Deployed version on heroku can be found [here](https://django-thread-rest-api.herokuapp.com/)
