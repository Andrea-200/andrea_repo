
from fastapi import FastAPI
from settings import settings  # Import the settings instance

app = FastAPI()

@app.get("/{variable}")
def read_variable(variable: str):
    value = settings.get_attribute(variable)
    return {variable: value}


