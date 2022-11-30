from flask import Blueprint
from flask import request
from controllers.enrollment_controller import EnrollmentController

enrollment_blueprints = Blueprint('enrollment_blueprints', __name__)
enrollment_controller = EnrollmentController()


@enrollment_blueprints.route("/enrollment/all", methods=['GET'])
def get_all_enrollment():
    response = enrollment_controller.index()
    return response, 200


@enrollment_blueprints.route("/enrollment/<string:id_>", methods=['GET'])
def get_enrollment_by_id(id_):
    response = enrollment_controller.show(id_)
    return response, 200


@enrollment_blueprints.route("/enrollment/matter/<string:matter_id>", methods=['GET'])
def get_enrollments_by_matter(matter_id):
    response = enrollment_controller.get_tables_by_matter(matter_id)
    return response, 200


@enrollment_blueprints.route("/enrollment/insert/matter/<string:matter_id>/tables/<string:tables_id>", methods=['POST'])
def insert_enrollment(matter_id, tables_id):
    enrollment = request.get_json()
    response = enrollment_controller.create(enrollment, matter_id, tables_id)
    return response, 201


@enrollment_blueprints.route("/enrollment/update/<string:id_>", methods=['PATCH'])
def update_enrollment(id_):
    enrollment = request.get_json()
    response = enrollment_controller.update(id_, enrollment)
    return response, 201


@enrollment_blueprints.route("/enrollment/delete/<string:id_>", methods=["DELETE"])
def delete_enrollment(id_):
    response = enrollment_controller.delete(id_)
    return response, 204

