import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Server.Process.process_Data_Kmean import Process_Data
from flask import Flask, request,Response
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)
@api.route('/home',)
class ClusterResource(Resource):
    def get(self):
        return "Home"

@api.route('/cluster',)
class ClusterResource(Resource):
    def post(self):
        _data = request.get_json()
        
        if _data:
            print('check value data request status',Response.status_code)
            _cluster=Process_Data()._process(_data)
            # lưu dữ liệu vào file:
            self.saveFile(_cluster)
            _response={
                'data': _cluster
                # 'status':200,
            }
        else:
            _response={
                'errCode':"Missing Parameter",
                'data':[]
                # 'status':404,
            }
        return _response
    def saveFile(self,data):
        Func = open("Server/cluster.html","w") 
        Func.write(data) 
        Func.close()
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
