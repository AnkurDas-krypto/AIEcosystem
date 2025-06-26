from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, recipes, tasks
from app.database import engine
from app.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue.js default dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(recipes.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Recipe AI API"}
