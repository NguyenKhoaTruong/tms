from flask import Flask,Blueprint,jsonify,request
from flask_restx import Api,Namespace,Resource,fields
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!"
apiBlPrnt = Blueprint('api', __name__, url_prefix='/api')
api= Api(apiBlPrnt,
         title="API TMS",
         description="TMS PLAN",
         version="1.0",
         doc="/swagger/",
         validate=True,
         )
app.register_blueprint(apiBlPrnt)
tmsCtrlr = Namespace(
    'tms', path="/tms/", description='TMS API Controller')
tmsDB=[]
createTmsCommand=tmsCtrlr.model("createPlanCommand",{
    'plan':fields.String(required=True,description='Plan Details')
})
#body method post response api
tmsDto=tmsCtrlr.model("tmsDTO",{
    'plan':fields.String(required=True,description='Plan Details')
})
#model api cluster
tmsCluster=tmsCtrlr.model("tmsCluster",{
    'order':fields.List(required=True,description='Order'),
    'name':fields.String(description='Name Cluster'),
    'num':fields.Integer(description='Num Cluster')
})
@tmsCtrlr.route("/")
class TMS(Resource):
    @tmsCtrlr.marshal_list_with(tmsDto)
    def get(self):
        return tmsDB
    @tmsCtrlr.expect(createTmsCommand)
    def post(self):
        newTms=tmsCtrlr.payload
        newId=1 if len(tmsDB) == 0 else 1 + max([x["id"] for x in tmsDB])
        tmsDB.append({"id":newId,"plan":newTms["plan"]})
@tmsCtrlr.route("/<int:id>")
class TMS(Resource):
    @tmsCtrlr.marshal_list_with(tmsDto)
    def get(self, id):
        desiredTms = [x for x in tmsDB if x["id"] == id]
        if len(desiredTms) > 0:
            return desiredTms[0]
        tmsCtrlr.abort(404, f"tms plan with id {id} does not exist")
    @tmsCtrlr.expect(tmsDto)
    def put(self, id):
        TmsDbIds = [x["id"] for x in tmsDB]
        if not id in TmsDbIds:
            tmsCtrlr.abort(404, f"plan with id {id} does not exist")
        tmsInd = [x["id"] for x in tmsDB].index(id)
        tmsDB[tmsInd]["task"] = tmsCtrlr.payload["task"]
        return tmsDB[tmsInd]
@tmsCtrlr.route("/cluster")
class TMS(Resource):
    @tmsCtrlr.expect(tmsCluster)
    def post(self,order,name,num):
        return tmsDB
api.add_namespace(tmsCtrlr)
app.run(host="0.0.0.0",port=8080,debug=True)