from flask import Blueprint
from controllers.reports_controller import ReportsController

reports_blueprints = Blueprint('reports_blueprints', __name__)
reports_controller = ReportsController()


@reports_blueprints.route("/reports/highest_votes", methods=['GET'])
def report_highest_votes():
    response = reports_controller.get_highest_votes()
    return response, 200
