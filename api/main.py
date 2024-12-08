from fastapi import FastAPI

# import uvicorn

from .crud.villes import router as villes_router

app = FastAPI()

app.include_router(villes_router, prefix="/villes", tags=["villes"])

# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=8000)