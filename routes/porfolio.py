from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from config.db import conn
from schemas.project import projectEntity,projectsEntity
database=conn.portfolio.ProjectsApp_project
from fastapi.templating import Jinja2Templates

portfolio = APIRouter()
templates = Jinja2Templates(directory="templates")


@portfolio.get('/', response_class=HTMLResponse)
def home(request: Request):
    projects= projectsEntity(database.find())
    iconos = [
        {
            'name': 'css',
            'icon': 'portfolio/css.png',
        }, {
            'name': 'django',
            'icon': 'portfolio/django.png',
        }, {
            'name': 'firebase',
            'icon': 'portfolio/firebase.png',
        }, {
            'name': 'git',
            'icon': 'portfolio/git.png',
        }, {
            'name': 'github',
            'icon': 'portfolio/github.png',
        }, {
            'name': 'html',
            'icon': 'portfolio/html.png',
        }, {
            'name': 'javascript',
            'icon': 'portfolio/js.png',
        }, {
            'name': 'mongodb',
            'icon': 'portfolio/mongodb.png',
        }, {
            'name': 'python',
            'icon': 'portfolio/python.png',
        }, {
            'name': 'sass',
            'icon': 'portfolio/sass.png',
        }, {
            'name': 'svelte',
            'icon': 'portfolio/svelte.png',
        }, {
            'name': 'vscode',
            'icon': 'portfolio/vscode.png',
        },
    ]
    return templates.TemplateResponse("home.html", {"request": request,"iconos":iconos,"projects":projects})
