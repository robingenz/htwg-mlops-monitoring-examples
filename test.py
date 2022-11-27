from flask import Flask
from flask_restx import Api, Resource, reqparse

flask_app = Flask(__name__)

flask_api = Api(flask_app)

flask_request_parser = reqparse.RequestParser()
flask_request_parser.add_argument('ticket_class', type=int, help='Ticket class: 1 = 1st (Upper), 2 = 2nd (Middle), 3 = 3rd (Lower)', required=True)
flask_request_parser.add_argument('sex', type=int, help='Sex: 0 = Man, 1 = Woman', required=True)
flask_request_parser.add_argument('age', type=int, help='Age', required=True)
flask_request_parser.add_argument('num_of_siblings_and_spouses', type=int, help='Number of siblings and spouses', required=True)
flask_request_parser.add_argument('num_of_parents_and_children', type=int, help='Number of parents and children', required=True)
flask_request_parser.add_argument('fare', type=float, help='Fare', required=True)
flask_request_parser.add_argument('port_of_embarkation', type=int, help='Port of embarkation: 0 = Southampton, 1 = Cherbourg, 2 = Queenstown', required=True)

@flask_api.route('/predict')
class PredictionResource(Resource):
    @flask_api.doc(parser=flask_request_parser)
    def post(self):
        args = flask_request_parser.parse_args()
        print(dict(args))
        return { 'prediction': 1, 'prediction_probability': 0.5 }

if __name__ == '__main__':
    flask_app.run(port=5100)
