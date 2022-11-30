from models.enrollment import Enrollment
from repositories.interfaceRepository import InterfaceRepository


class ReportsRepository(InterfaceRepository[Enrollment]):

    #   Aquí se puede agregar más filtros de búsqueda como en mongo_db...

    def get_highest_votes(self):
        query_aggregation = {
            "_id": "$matter",
            "Votos max": {"$max": "$Votos"},
            "matter": {"$first": "$$ROOT"}
        }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)
