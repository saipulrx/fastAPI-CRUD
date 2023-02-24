## Repository for fastAPI CRUD Database operation

### Prerequisites :
- Create virtual environment for FastAPI
```
#create virtual environment
python -m venv ./venv

#activate virtual environment (Windows)
.\venv\Scripts\activate

#activate virtual environment (Linux/Mac)
source venv/bin/activate
```

- Install libraries : fastapi, ASGI (Asynchronous Server Gateway Interface) server(in this case we will use Uvicorn), SQLAlchemy and psycopg2 to connect to postgres databases. You can type pip install requirements.txt for install all libraries.

### Structure folder :
Lets define project structure bellow :
```
+-- app
| +-- __init__.py
| +-- crud.py
| +-- config.py
| +-- main.py
| +-- models.py
| +-- routes.py
| +-- schemas.py
+-- venv
```

### How to Run
- type command bellow
```
cd app
uvicorn main:app --reload
```

- It will run apps with default ip 127.0.0.1 and port 8000
