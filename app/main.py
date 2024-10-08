from fastapi import FastAPI, APIRouter, Request
from fastapi.staticfiles import StaticFiles
import httpx
from contextlib import asynccontextmanager
from app.routes.home_routes import router as home_router

main_router = APIRouter()
main_router.include_router(home_router)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.requests_client = httpx.AsyncClient()
    yield
    await app.requests_client.aclose()

# Create app instance
app = FastAPI(lifespan=lifespan)

# Add route for static files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

# Include routes in app
app.include_router(main_router)

