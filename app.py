from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.project import project
from routes.porfolio import portfolio
app= FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(project)
app.include_router(portfolio)
