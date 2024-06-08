from fastapi import FastAPI, Depends, HTTPException, Path
import models
from database import engine, SessionLocal
from routers import auth,todos,admin

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
