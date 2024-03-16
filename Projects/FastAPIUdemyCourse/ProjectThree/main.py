from fastapi import FastAPI

from .database import engine
from .routers import auth, todos
from .models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/health")
async def health():
    return {"status": "healthy"}


app.include_router(auth.router)
app.include_router(todos.router)
