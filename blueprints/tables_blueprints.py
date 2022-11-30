from flask import Blueprint
from flask import request
from controllers.tables_controller import TablesController

tables_blueprints = Blueprint('tables_blueprints', __name__)
tables_controller = TablesController()


@tables_blueprints.route("/tables/all", methods=['GET'])
def get_all_tables():
    response = tables_controller.index()
    return response, 200


@tables_blueprints.route("/tables/<string:id_>", methods=['GET'])
def get_tables_by_id(id_):
    response = tables_controller.show(id_)
    return response, 200


@tables_blueprints.route("/tables/insert", methods=['POST'])
def insert_tables():
    tables = request.get_json()
    response = tables_controller.create(tables)
    return response, 201


@tables_blueprints.route("/tables/update/<string:id_>", methods=['PATCH'])
def update_tables(id_):
    tables = request.get_json()
    response = tables_controller.update(id_, tables)
    return response, 201


@tables_blueprints.route("/tables/delete/<string:id_>", methods=["DELETE"])
def delete_tables(id_):
    response = tables_controller.delete(id_)
    return response, 204
