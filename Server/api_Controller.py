from flask import Flask, request, jsonify
import json
app = Flask(__name__)

# Route để nhận dữ liệu JSON từ tham số trên URL
@app.route('/api/process_json', methods=['GET'])
def process_json():
    # Lấy giá trị của tham số 'data' từ URL
    json_data_param = request.args.get('data')

    try:
        # Chuyển đổi giá trị từ chuỗi JSON thành đối tượng Python
        json_data = json.loads(json_data_param)

        # Xử lý dữ liệu JSON theo nhu cầu của bạn
        processed_data = {'result': 'success', 'data': json_data}

        # Trả về kết quả dưới dạng JSON
        return jsonify(processed_data)
    except json.JSONDecodeError:
        return jsonify({'result': 'error', 'message': 'Invalid JSON data'})

if __name__ == '__main__':
    app.run(debug=True)
