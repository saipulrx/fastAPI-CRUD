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

- Install postman for run API after run FastAPI apps. You can download [here](https://www.postman.com/downloads/)

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
- Type command bellow. It will run apps with default ip 127.0.0.1 and port 8000
```
cd app
uvicorn main:app --reload
```
<img width="890" alt="image" src="https://user-images.githubusercontent.com/22763010/221135920-a3883587-4707-4f5f-8272-ccf585ffdde0.png">


- Open Postman, type url http://127.0.0.1:8000 and methode GET then save as **Home**. Click Send button then will display output "Hallo"
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/22763010/221137029-0e38e18c-9768-4ec6-ae02-4b31cc55519f.png">

- Next define other request as bellow :
  - Request Name : Create New. URL : http://127.0.0.1:8000/book/create. Method : POST. Body: Choose raw and type 
    ```
    {
      "parameter": {
        "title": "Apache Spark for Data Scientist",
        "description": "Book about Apache Spark for Data Scientist"
       }
    }
    ```
    save as **Create New**. Click Send button then will display Response 200 OK
    <img width="845" alt="image" src="https://user-images.githubusercontent.com/22763010/221142946-0545fcab-d80f-468a-8d51-467059a44404.png">
  
  - Request Name : Get All. URL : http://127.0.0.1:8000/book/. Method : GET. Save as **Get All** then click Send button will display output bellow
    
    <img width="845" alt="image" src="https://user-images.githubusercontent.com/22763010/221143681-ede910cf-6f91-46f3-9478-52d2d98e3343.png">
 
  - Request Name : Get By Id. URL : http://127.0.0.1:8000/book/{id}(id with get from run request Get All).
    Method : GET. Save as **Get By Id** then click Send button will display output bellow 
    
    <img width="856" alt="image" src="https://user-images.githubusercontent.com/22763010/221144680-bad9db66-1ecb-4bc6-b629-53b0f16861e6.png">

  - Request Name : Update. URL : http://127.0.0.1:8000/book/update. Method : PATCH . Body: Choose raw and type  
    ```
    {
    "parameter": {
        "id": "3",
        "title": "Apache Spark for Data Scientist",
        "description": "Book about Apache Spark for Data Scientist for Beginner"
        }
    }
    ```
    save as **Update**. Click Send button then will display output bellow
    
    <img width="831" alt="image" src="https://user-images.githubusercontent.com/22763010/221145535-ea8a7cc6-fffa-40ac-a3b1-1f7d20909dd1.png">
  
  - Request Name : Delete. URL : http://127.0.0.1:8000/book/{id}(id with get from run request Get All).
    Method : DELETE. Save as **Delete** then click Send button will display output bellow
    
    <img width="844" alt="image" src="https://user-images.githubusercontent.com/22763010/221145959-d1993c97-24bf-4669-9381-987baf56fdc2.png">
