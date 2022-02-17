# Overview
## project structure

Below is the general structure of the repository:
```
.
├── backend
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── lending
│   │   ├── accounts
│   │   ├── db.sqlite3
│   │   ├── lending
│   │   ├── loans
│   │   └── manage.py
│   └── requirements.txt
├── docker-compose.yml
├── frontend
│   ├── auth
│   │   ├── commands.txt
│   │   ├── node_modules
│   │   ├── package.json
│   │   ├── package-lock.json
│   │   ├── public
│   │   ├── README.md
│   │   └── src
│   └── Dockerfile
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── postgres
└── README.md
```

1. **Backend:** Django project that handles user creation and loan processing.
2. **Frontend:** React project that provides users an interface to the system.
3. **postgres:** Configuration for the postgres database docker setup.
4. **nginx** Configuration and Dockerfile for nginx docker setup.

### Getting started
1. Run the following command to setup the project:
```shell script
docker-compose up --build
```

2. Complete the database setup by running the migrations:
```shell script
docker-compose exec backend python lending/manage.py migrate --noinput
```

3. Create the admin user for the system. Please provide details as requested.
```shell script
docker-compose exec backend python lending/manage.py createsuperuser
```

Once complete, access the project via ```http://localhost:8008```