from fastapi import APIRouter
from app.models.hello_response import HelloResponse

router = APIRouter()


@router.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to the test-python-3 FastAPI service!"}


@router.get("/hello", response_model=HelloResponse)
async def say_hello():
    return HelloResponse(message="Hello from test-python-3!")


@router.get("/healthz", include_in_schema=False)
async def healthz():
    # App is alive (use this for liveness probe)
    return {"status": "ok"}


@router.get("/readyz", include_in_schema=False)
async def readyz():
    # App is ready to serve traffic (add checks later if needed)
    return {"status": "ready"}
