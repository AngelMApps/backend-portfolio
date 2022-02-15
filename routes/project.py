from fastapi import APIRouter, Response
from config.db import conn
from schemas.project import projectEntity,projectsEntity
from models.project import Project
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


project = APIRouter()
database=conn.portfolio.ProjectsApp_project

@project.get('/')
def home():
    return {"message":"main"}

@project.get('/projects')
def getProjects():
    return projectsEntity(database.find())

@project.post('/projects')
def createProject(project: Project):
    new_project=dict(project)
    id=database.insert_one(new_project).inserted_id
    
    return projectEntity(database.find_one({'_id':id}))


@project.get('/projects/{id}')
def getProject(id: str):
    return projectEntity(database.find_one({'_id':ObjectId(id)}))

@project.put('/projects/{id}')
def updateProject(id: str, project: Project):
    database.find_one_and_update({'_id':ObjectId(id)},{"$set": dict(project)})
    return projectEntity(database.find_one({'_id':ObjectId(id)}))

@project.delete('/projects/{id}')
def deleteProject(id: str):
    projectEntity(database.find_one_and_delete({'_id':ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)