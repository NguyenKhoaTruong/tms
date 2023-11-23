from flask import Flask, request,jsonify

app = Flask(__name__)

student = []

@app.post('/cluster')
def echo():
    print('check data reuqest',request)
    data = request.get_json()
    print('check data',data)
    return jsonify(data)

@app.post("/api/v1.0/students")
def create_student():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    details = {
      'name': name,
      'country': country,
      'city': city,
    }
    student.append(details)
    return details
app.run(debug=True)