import sys
sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from flask import Flask, Blueprint, jsonify, request,Response
from flask_restx import Api, Namespace, Resource, fields, reqparse
from Server.Process.process_Data_Kmean import Process_Data


app = Flask(__name__)
apiBlPrnt = Blueprint('api', __name__, url_prefix='/api')
api = Api(apiBlPrnt,
          title="API TMS",
          description="TMS PLAN",
          version="1.0",
          doc="/swagger/",
          validate=True,
          )
app.register_blueprint(apiBlPrnt)
tmsCtrlr = Namespace(
    'tms', path="/tms/", description='TMS API Controller')
tmsDB = []


# models
tmsDto = tmsCtrlr.model("tmsDTO", {
    'plan': fields.String(required=True, description='Plan Details')
})
tmsCluster = tmsCtrlr.model("tmsCluster", {
    'order': fields.List(fields.List(fields.Float), description='Order'),
    'name': fields.String(description='Name Cluster'),
    'num': fields.Integer(description='Num Cluster')
})


@tmsCtrlr.route("/cluster")
class TMSCluster(Resource):
    @tmsCtrlr.expect(tmsCluster)
    def post(self):
        data = request.get_json()
        _cluster=Process_Data()._process(data)
        print('check value data',_cluster)
        return _cluster
        # data=Process_Data()._process(_cluster)
        # print('check valeu data',data)
        # tmsDB.append(new_cluster)
        # return Response(data)

if __name__ == '__main__':
    api.add_namespace(tmsCtrlr)
    app.run(host="0.0.0.0", port=8080, debug=True)



