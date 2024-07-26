from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    # Retrieve environment variables
    env_a = os.getenv('a', 'Not Set')
    env_b = os.getenv('b', 'Not Set')
    env_c = os.getenv('c', 'Not Set')
    env_d = os.getenv('d', 'Not Set')
    
    # Return environment variables
    return {
        "a": env_a,
        "b": env_b,
        "c": env_c,
        "d": env_d
    }

if _name_ == "_main_":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)