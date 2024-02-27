from fastapi import FastAPI

from src.api.routers import auth, advertisement, review, worktime, category


def create_app_routers(app: FastAPI):
    app.include_router(auth.router)
    app.include_router(advertisement.router)
    app.include_router(review.router)
    app.include_router(worktime.router)
    app.include_router(category.router)

    return app
