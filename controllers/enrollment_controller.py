from models.enrollment import Enrollment
from models.matter import Matter
from models.tables import Tables
from repositories.enrollment_repository import EnrollmentRepository
from repositories.matter_repository import MatterRepository
from repositories.tables_repository import TablesRepository


class EnrollmentController:

    # Constructor
    def __init__(self):
        print("Enrollment controller ready...")
        self.enrollment_repository = EnrollmentRepository()
        self.matter_repository = MatterRepository()
        self.tables_repository = TablesRepository()

    # Get All
    def index(self) -> list:
        print("Get all enrollment")
        return self.enrollment_repository.find_all()

    # Get One by ID
    def show(self, id_: str) -> dict:
        print("Get enrollment")
        return self.enrollment_repository.find_by_id()

    def get_tables_by_matter(self, matter_id: str) -> list:
        return self.enrollment_repository.get_enrollments_by_matter(matter_id)

    # INSERT
    def create(self, enrollment_: dict, matter_id: str, tables_id: str) -> dict:
        print("Insert enrollment")
        enrollment = Enrollment(enrollment_)
        matter_dict = self.matter_repository.find_by_id(matter_id)
        matter_obj = Matter(matter_dict)
        tables_dict = self.tables_repository.find_by_id(tables_id)
        tables_obj = Tables(tables_dict)
        enrollment.matter = matter_obj
        enrollment.tables = tables_obj
        return self.enrollment_repository.save(enrollment)

    # UPDATE
    def update(self, id_: str, enrollment_: dict) -> dict:
        print("Update enrollment")
        enrollment = Enrollment(enrollment_)
        return self.enrollment_repository.update(id_, enrollment)

    # DELETE
    def delete(self, id_: str) -> str:
        print("Delete enrollment")
        return self.enrollment_repository.delete(id_)
