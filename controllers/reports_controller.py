from repositories.reports_repository import ReportsRepository


class ReportsController:

    #    Reportes

    def __init__(self):
        self.reports_repository = ReportsRepository()

    def get_highest_votes(self):
        return self.reports_repository.get_highest_votes()
