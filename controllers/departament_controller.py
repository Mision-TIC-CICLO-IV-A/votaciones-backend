from models.departament import Departament
from repositories.departament_repository import DepartamentRepository


class DepartamentController:

    # Constructor
    def __init__(self):
        print("Departament controller ready...")
        self.departament_repository = DepartamentRepository()

    # Get All
    def index(self) -> list:
        print("Get all departament")
        return self.departament_repository.find_all()

    # Get One by ID
    def show(self, id_: str) -> dict:
        print("Get departament")
        return self.departament_repository.find_by_id()

    # INSERT
    def create(self, departament_: dict) -> dict:
        print("Insert departament")
        departament = Departament(departament_)
        return self.departament_repository.save(departament)

    # UPDATE
    def update(self, id_: str, departament_: dict) -> dict:
        print("Update departament")
        departament = Departament(departament_)
        return self.departament_repository.update(id_, departament)

    # DELETE
    def delete(self, id_: str) -> str:
        print("Delete departament " + id_)
        return self.departament_repository.delete(id_)


