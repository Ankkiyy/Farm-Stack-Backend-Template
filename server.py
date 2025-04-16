import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from bind import sio_app

app = FastAPI()

# Mount the static files
app.mount("/static", StaticFiles(directory='static'), name="static")
app.mount('/', app=sio_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def start_server():
    uvicorn.run("server:app", port=10007, reload=True , host="0.0.0.0")

if __name__ == '__main__':
    start_server()