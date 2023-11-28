from flask import Flask
from flask_restx import Api, Resource, reqparse, fields


app = Flask(__name__)
api = Api(app)


# Định nghĩa mô hình đầu vào (input model)
order_model = api.model('OrderModel', {
    'order': fields.List(fields.List(fields.Raw)),
    'num': fields.Integer,
    'name': fields.String
})


class YourResource(Resource):
    # Sử dụng reqparse để xác thực và parse dữ liệu đầu vào
    parser = reqparse.RequestParser()
    parser.add_argument('data', type=dict, required=True, location='json')


    @api.expect(order_model)  # Đặt mong đợi mô hình đầu vào
    def post(self):
        args = self.parser.parse_args()
        data = args['data']


        print(f"Received data - Order: {data['order']}, Num: {data['num']}, Name: {data['name']}")


        return {'message': 'Data received successfully'}, 200


# Thêm resource vào API
api.add_resource(YourResource, '/your-endpoint')


if __name__ == '__main__':
    app.run(debug=True)





# import requests


# url = 'http://127.0.0.1:5000/your-endpoint'
# data = {
#     "data": {
#         "order": [
#             [10.7400531, 106.73387648, 10.0, 11.0, "1"],
#             [10.73252319, 106.70693794, 10.5, 11.5, "2"],
#             [10.73769961, 106.72571768, 11, 12, "3"],
#             [10.7410835, 106.70203763, 11.5, 12.5, "4"],
#             [10.74838756, 106.70536196, 12, 13, "5"],
#             [10.7495301, 106.7084913, 12.5, 13.5, "6"]
#         ],
#         "num": 2,
#         "name": "K-Mean"
#     }
# }


# headers = {'Content-Type': 'application/json'}


# response = requests.post(url, json=data, headers=headers)


# print(response.status_code)
# print(response.json())



