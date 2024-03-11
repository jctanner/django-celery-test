Validating Django + DRF + Celery integration for 2024.


`docker compose build && docker compose up`

```
curl -u admin:admin -X POST -d '[1,2,3,4]' -H 'Content-Type: application/json' http://localhost:8000/api/xsum/ ; echo ""
curl -u admin:admin  http://localhost:8000/api/tasks/445816c9-5d71-4c9b-81b3-846d58f9c94a/; echo ""
```

```
.
├── bin
│   └── entrypoint.sh
├── django_celery_test
│   ├── django_celery_test  # This is the project
│   │   ├── asgi.py
│   │   ├── celery.py       # the celery app is defined here
│   │   ├── __init__.py     # the celery app is imported here to make it available to all of django
│   │   ├── settings.py     # config for celery is defined here
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   └── webapp              # This the app
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── management
│       │   └── commands
│       │       ├── create_superuser.py  # Custom management command we probably don't need
│       │       └── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── tasks.py        # This is where the auto-discovered tasks are
│       ├── tests.py
│       ├── viewsets
│       │   └── __init__.py # A simple viewset for calling xsum asynchronously and for getting task results is here
│       └── views.py
├── docker-compose.yaml
├── Dockerfile
├── NOTES.txt
├── README.md
└── requirements.txt
```


