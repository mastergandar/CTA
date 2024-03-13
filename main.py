import uvicorn
from fastapi import FastAPI

from settings import base as base_settings
from exchange.bybit.views import router as bybit_router
from users.views import router as users_router

app = FastAPI(
    title=base_settings.PROJECT_NAME,
    description=base_settings.DESCRIPTION,
    version=base_settings.VERSION,
    summary=base_settings.SUMMARY,
    contact=base_settings.CONTACT,
    license_info=base_settings.LICENSE_INFO,
)
app.include_router(bybit_router)
app.include_router(users_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='127.0.0.1', port=8000)
