from ninja import Schema

class todoin(Schema):
    title: str
    description: str

class details(Schema):
    detail: str

class todoup(Schema):
    old_title: str
    new_title: str
    description: str

class tododel(Schema):
    title: str