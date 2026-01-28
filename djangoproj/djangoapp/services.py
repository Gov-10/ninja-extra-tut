from .models import Student
from django.shortcuts import get_object_or_404
class StudentService:
    def create(self,payload):
        return Student.objects.create(**payload)
    def list(self):
        return Student.objects.all()
    def get(self, student_id:int):
        return get_object_or_404(Student, id=student_id)
    def update(self, student_id:int, payload):
        stud = get_object_or_404(Student, id=student_id)
        for key,val in payload.items():
            setattr(stud, key, val)
        stud.save()
        return {"message": "Updated"}
    def delete(self, student_id:int):
        stud = get_object_or_404(Student, id=student_id)
        stud.delete()
        return {"message" : "Deleted"}

