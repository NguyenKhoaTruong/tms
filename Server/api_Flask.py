import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Server.Process.process_Data_Kmean import Process_Data
from flask import Flask, request,Response,render_template_string
from flask_restx import Resource, Api,fields,reqparse

app = Flask(__name__)
api = Api(app)
@api.route('/home',)
class ClusterResource(Resource):
    def get(self):
        return "Home"
@api.route('/get/cluster',)
class ClusterResource(Resource):
    def get(self):
        with open('Server/cluster.html', 'r') as file:
            html_content = file.read()
        return render_template_string(html_content)
@api.route('/cluster',)
class ClusterResource(Resource):
    def post(self):
        _data = request.get_json()
        if _data:
            _cluster=Process_Data()._process(_data)
            self.saveFile(_cluster)
            _response={
                'data': _cluster
            }
        else:
            _response={
                'errCode':"Missing Parameter",
                'data':[]
            }
        return _response
    def saveFile(self,data):
        Func = open("Server/cluster.html","w") 
        Func.write(data) 
        Func.close()
#Data Swagger có order models:
order_model = api.model('OrderModel', {
    'order': fields.List(fields.List(fields.Raw)),
    'num': fields.Integer,
    'name': fields.String
})


class YourResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('data', type=dict, required=True, location='json')
    @api.expect(order_model) 
    def post(self):
        args = self.parser.parse_args()
        data = args['data']


        print(f"Received data - Order: {data['order']}, Num: {data['num']}, Name: {data['name']}")


        return {'message': 'Data received successfully'}, 200

api.add_resource(YourResource, '/cluster/models')
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
