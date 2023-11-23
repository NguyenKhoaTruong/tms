# import requests

# # URL của API
# api_url = "http://localhost:8080/api/tms/cluster"

# # Dữ liệu bạn muốn truyền
# data = {
#     'order': [[10.1, 10.2], [10.3, 11.2]],
#     'name': 'TMA',
#     'num': 10
# }

# # Gọi API sử dụng phương thức POST
# response = requests.post(api_url, json=data)

# # Kiểm tra kết quả
# if response.status_code == 200:
#     print("Success!")
#     print(response.json())
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)
import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Server.Process.process_Data_Kmean import Process_Data
from flask import Flask, request,Response
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/cluster',)
class ClusterResource(Resource):
    def post(self):
        _data = request.get_json()
        if _data:
            _cluster=Process_Data()._process(_data)
            # lưu dữ liệu vào file:
            self.saveFile(_cluster)
            _response={
                'success':True,
                'status':200,
                'data': _cluster
            }
        else:
            _response={
                'errCode':"Missing Parameter",
                'status':400,
                'data':[]
            }
        return _response
    def saveFile(self,data):
        Func = open("cluster.html","w") 
        Func.write(data) 
        Func.close()
if __name__ == '__main__':
    app.run(debug=True)
