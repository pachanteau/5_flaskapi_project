
from flask import Flask, url_for, request, jsonify, render_template
import joblib

MODEL_PATH = "model/model.joblib"

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    
    if request.json:
        
        json_input = request.get_json()
        
        model = joblib.load(MODEL_PATH)
       
        prediction = model.predict(list(json_input["input"]))
        
        # prediction = float(prediction[0])
        
        response = {
            "prediction": str(prediction)
        }
        return jsonify(response), 200
    return jsonify({"msg": "Error, no JSON detected"})


@app.route("/")
def index():
    return render_template("templates/flaskapi-project2.html")
    

if __name__ == "__main__":
    app.run(debug=True)