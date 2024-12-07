from fastapi import FastAPI

from .crud.villes import router as villes_router

app = FastAPI()

app.include_router(villes_router, prefix="/villes", tags=["villes"])
