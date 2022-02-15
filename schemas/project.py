def projectEntity(item) -> dict:
    return {
        "ProjectId":str(item["_id"]),
        "ProjectName":item["ProjectName"],
        "ProjectDescription":item["ProjectDescription"],
        "ProjectURL":item["ProjectURL"],
        "ProjectCode":item["ProjectCode"],
        "ProjectImage":item["ProjectImage"]
    }

def prueba():
    return "prueba"

def projectsEntity(entity) -> list:
    return [projectEntity(item) for item in entity]