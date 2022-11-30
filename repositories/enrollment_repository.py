from bson import ObjectId
from models.enrollment import Enrollment
from repositories.interfaceRepository import InterfaceRepository


class EnrollmentRepository(InterfaceRepository[Enrollment]):
    def get_enrollments_by_matter(self, matter_id: str) -> list:
        query_dict = {"matter.$id": ObjectId(matter_id)}
        return self.query(query_dict)
