from fastapi import FastAPI
from settings import settings


app = FastAPI()

@app.get('/')
def fun():
    return "HI this is andrea"

@app.get("/value/{variable}")
def read_variable(variable: str):
    value = settings.get_attribute(variable)
    return {variable: value}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app,host="localhost",port=8000)
    