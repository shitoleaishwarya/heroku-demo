from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('student_rf.pkl', 'rb'))

@app.route("/register", methods=["GET"])
def get_register():
    # flask loads register.html from templates directory
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def post_register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    # db.query(f"insert into user (name, email, password) values ('{name}', '{email}', '{password}')")

    return "user registered successfully"

@app.route("/login", methods=["GET"])
def get_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def post_login():
    email = request.form.get("email")
    password = request.form.get("password")

    # users = db.select(f"select id, name from user where email = '{email}' and password = '{password}'")
    if email == "admin" and password == "admin" :
        # user does not exist
        return render_template("home.html")
    else:
        # user exists
        return "Login failed"
import numpy as np
@app.route("/predict", methods=["GET"])
def get_prediction():
    return render_template("index.html")
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Student Grades Are  {}'.format(output))


@app.route("/", methods=["GET"])
def root():
    return  render_template("login.html")
app.run(debug=True, port=3000)
