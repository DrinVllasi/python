from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()
#creating developer API with POST Method
@app.post("/developers/")
def create_developer(developer: Developer):
    return {"message": "Developer created successfully","developer":developer}

#Creating Projects API with POST Method
@app.post("/projects/")
def create_project(project: Project):
    return{"message": "Project created successfully","project":project}

@app.get("/projects/")
def get_projects():
    sample_project = Project(
        title = "Sample Project",
        description = "This is a sample project",
        language = ["Python","Javascript"],
        lead_developer = Developer(name="John Doe", experience=5)

    )
    return {"projects": [sample_project]}