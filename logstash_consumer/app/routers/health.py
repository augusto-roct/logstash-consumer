from fastapi import APIRouter


router = APIRouter()


@router.get("/live", status_code=200)
async def liveness():
    return {"message": "Ok"}


@router.get("/ready", status_code=200)
async def readiness():
    return {"message": "Ok"}
