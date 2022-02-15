from pydantic import BaseModel
from typing import Optional

class Project(BaseModel):
    ProjectId: Optional[str]
    ProjectName: str
    ProjectDescription: str
    ProjectURL: str
    ProjectCode: str
    ProjectImage: str
