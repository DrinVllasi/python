from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()
#creating developer API with POST Method
@app.post("/developers/")
def create_developer(developer: Developer):
    return {"message": "Developer created successfully","developer":developer}

#Creating Projects API with POST Method
@app.post("/projects/")
def create_project(projct: Project):
    return{"message": "Project created successfully","project":project}