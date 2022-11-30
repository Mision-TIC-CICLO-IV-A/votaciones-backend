from models.matter import Matter
from repositories.matter_repository import MatterRepository
from models.departament import Departament
from repositories.departament_repository import DepartamentRepository


class MatterController:

    # Constructor
    def __init__(self):
        print("Matter controller ready...")
        self.matter_repository = MatterRepository()
        self.departament_repository = DepartamentRepository()

    # Get All
    def index(self) -> list:
        print("Get all matter")
        return self.matter_repository.find_all()

    # Get One by ID
    def show(self, id_: str) -> dict:
        print("Get matter")
        return self.matter_repository.find_by_id()

    # INSERT
    def create(self, matter_: dict) -> dict:
        print("Insert matter")
        matter = Matter(matter_)
        return self.matter_repository.save(matter)

    # UPDATE
    def update(self, id_: str, matter_: dict) -> dict:
        print("Update matter")
        matter = Matter(matter_)
        return self.matter_repository.update(id_, matter)

    # DELETE
    def delete(self, id_: str) -> str:
        print("Delete matter")
        return self.matter_repository.delete(id_)

    def departament_assign(self, matter_id: str, departament_id: str) -> dict:
        matter_dict = self.matter_repository.find_by_id(matter_id)
        matter_obj = Matter(matter_dict)
        departament_dict = self.departament_repository.find_by_id(departament_id)
        departament_obj = Departament(departament_dict)
        matter_obj.departament = departament_obj
        return self.matter_repository.save(matter_obj)



















