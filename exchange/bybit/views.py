from fastapi import APIRouter

router = APIRouter(prefix="/exchange/bybit", tags=["exchange", "bybit"])
api_key = "QWERTY12"


@router.get("/")
def get_exchange_info():
    return {"info": "Основная платформа для следования за сделками"}


@router.get("/api_key")
def get_api_key():
    return {"api_key": f"{api_key}"}
