from fastapi import FastAPI
#add import
import models
from config import engine
from routes import router

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


#define endpoint
@app.get("/")
def home():
    return "HALLO"

app.include_router(router, prefix="/book", tags=["book"])