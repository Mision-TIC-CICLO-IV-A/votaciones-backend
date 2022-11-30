import json
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve
from blueprints.departament_blueprints import departament_blueprints
from blueprints.enrollment_blueprints import enrollment_blueprints
from blueprints.matter_blueprints import matter_blueprints
from blueprints.tables_blueprints import tables_blueprints
from blueprints.reports_blueprints import reports_blueprints

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(departament_blueprints)
app.register_blueprint(enrollment_blueprints)
app.register_blueprint(matter_blueprints)
app.register_blueprint(tables_blueprints)
app.register_blueprint(reports_blueprints)


@app.route("/", methods=['GET'])
def home():
    response = {
        "message": "Bienvenido a los microservicios de las votaciones para la registraduria"
    }
    return jsonify(response)


# ==================== Config and setup app
def load_file_config():
    with open("config.json", 'r') as config_file:
        data = json.load(config_file)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
