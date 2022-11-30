from flask import Blueprint
from flask import request
from controllers.departament_controller import DepartamentController

departament_blueprints = Blueprint('departament_blueprints', __name__)
departament_controller = DepartamentController()


@departament_blueprints.route("/departament/all", methods=['GET'])
def get_all_departament():
    response = departament_controller.index()
    return response, 200


@departament_blueprints.route("/departament/<string:id_>", methods=['GET'])
def get_departament_by_id(id_):
    response = departament_controller.show(id_ )
    return response, 200


@departament_blueprints.route("/departament/insert", methods=['POST'])
def insert_departament():
    departament = request.get_json()
    response = departament_controller.create(departament)
    return response, 201


@departament_blueprints.route("/departament/update/<string:id_>", methods=['PATCH'])
def update_departament(id_):
    departament = request.get_json()
    response = departament_controller.update(id_, departament)
    return response, 201


@departament_blueprints.route("/departament/delete/<string:id_>", methods=["DELETE"])
def delete_departament(id_):
    response = departament_controller.delete(id_)
    return response, 204
