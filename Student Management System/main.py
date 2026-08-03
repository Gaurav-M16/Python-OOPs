from models.student_model import Student
from services.student_services import StudentService

#Creating objects
stu1 = Student("Gaurav", 21, 201)
stu2 = Student("Pooja",22, 202)

#Creating services
service = StudentService()

service.add_student(stu1)
service.add_student(stu2)

service.display_students()