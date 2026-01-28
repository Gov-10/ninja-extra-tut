from ninja import Schema
class StudentOut(Schema):
    id:int
    name:str
    age:int

class StudentIn(Schema):
    name:str
    age:int
