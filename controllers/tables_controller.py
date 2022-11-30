from models.tables import Tables
from repositories.tables_repository import TablesRepository


class TablesController:

    # Constructor
    def __init__(self):
        print("Tables controller ready...")
        self.tables_repository = TablesRepository()

    # Get All
    def index(self) -> list:
        print("Get all tables")
        return self.tables_repository.find_all()

    # Get One by ID
    def show(self, id_: str) -> dict:
        print("Get tables")
        return self.tables_repository.find_by_id()

    # INSERT
    def create(self, tables_: dict) -> dict:
        print("Insert tables")
        tables = Tables(tables_)
        return self.tables_repository.save(tables)

    # UPDATE
    def update(self, id_: str, tables_: dict) -> dict:
        print("Update tables")
        tables = Tables(tables_)
        return self.tables_repository.update(id_, tables)

    # DELETE
    def delete(self, id_: str) -> str:
        print("Delete tables")
        return self.tables_repository.delete(id_)
