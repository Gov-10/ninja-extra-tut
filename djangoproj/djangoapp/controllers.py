from ninja_extra import api_controller, http_get, http_post, http_put, http_delete
from ninja.errors import HttpError
from .services import StudentService
from .schema import StudentOut, StudentIn
from typing import List
from ninja_extra import NinjaExtraAPI

@api_controller("/students", tags=["Student"])
class StudentController:
    def __init__(self, service:StudentService):
        self.service = service

    @http_post("/", response=StudentOut)
    def create_stud(self, payload:StudentIn):
        return self.service.create(payload.dict())

    @http_get("/", response=List[StudentOut])
    def list_stud(self):
        return self.service.list()

    @http_get("/{student_id}", response=StudentOut)
    def get_stud(self, student_id:int):
        return self.service.get(student_id)

    @http_put("/{student_id}")
    def update_stud(self, student_id:int, payload:StudentIn):
        return self.service.update(student_id, payload.dict())
    @http_delete("/{student_id}")
    def delete_stud(self, student_id:int):
        return self.service.delete(student_id)


api=NinjaExtraAPI()
api.register_controllers(StudentController)
        
