from flask import Blueprint
from flask import request
from controllers.matter_controller import MatterController

matter_blueprints = Blueprint('matter_blueprints', __name__)
matter_controller = MatterController()


@matter_blueprints.route("/matter/all", methods=['GET'])
def get_all_matter():
    response = matter_controller.index()
    return response, 200


@matter_blueprints.route("/matter/<string:id_>", methods=['GET'])
def get_matter_by_id(id_):
    response = matter_controller.show(id_)
    return response, 200


@matter_blueprints.route("/matter/insert", methods=['POST'])
def insert_matter():
    matter = request.get_json()
    response = matter_controller.create(matter)
    return response, 201


@matter_blueprints.route("/matter/update/<string:id_>", methods=['PATCH'])
def update_matter(id_):
    matter = request.get_json()
    response = matter_controller.update(id_, matter)
    return response, 201


@matter_blueprints.route("/matter/<string:matter_id>/departament/<string:departament_id>", methods=['PUT'])
def assign_departament(matter_id, departament_id):
    response = matter_controller.departament_assign(matter_id, departament_id)
    return response, 201


@matter_blueprints.route("/matter/delete/<string:id_>", methods=["DELETE"])
def delete_matter(id_):
    response = matter_controller.delete(id_)
    return response, 204
