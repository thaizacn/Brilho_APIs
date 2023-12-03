from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import BrilhoController

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializando rotas
app.include_router(BrilhoController.router, prefix="/cupons")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
