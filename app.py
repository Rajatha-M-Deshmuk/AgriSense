from flask import Flask, request, render_template
import numpy as np
import pickle

# ------------------------------------------------------------------
# Load what’s in the pickle file (could be estimator or tuple)
# ------------------------------------------------------------------
loaded = pickle.load(open(
    r"E:/Rajatha M Deshmuk/6th sem/Machine Learning Project/"
    r"crop recommendation system/crop recommedation/views/crop_model.pkl",
    "rb"
))

# If it's a tuple, unpack; otherwise scaler/label_map stay None
if isinstance(loaded, tuple):
    model, scaler, num_to_label = loaded
else:
    model = loaded          # estimator only
    scaler = None
    num_to_label = None
# ------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # 1️⃣ Read and convert form inputs
        N         = float(request.form["Nitrogen"])
        P         = float(request.form["Phosphorus"])
        K         = float(request.form["Potassium"])
        temp      = float(request.form["Temperature"])
        humidity  = float(request.form["Humidity"])
        ph        = float(request.form["Ph"])
        rainfall  = float(request.form["Rainfall"])

        features = np.array([[N, P, K, temp, humidity, ph, rainfall]])

        # 2️⃣ Scale if a scaler is available
        if scaler is not None:
            features = scaler.transform(features)

        # 3️⃣ Predict
        pred_num = model.predict(features)[0]

        # 4️⃣ Map the numeric label to crop name
        if num_to_label is not None:
            crop = num_to_label.get(pred_num, "Unknown crop")
        else:
            # fallback if you never saved num_to_label
            default_map = {
                1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut",
                6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon",
                10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                14: "Pomegranate", 15: "Lentil", 16: "Blackgram",
                17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas",
                20: "Kidneybeans", 21: "Chickpea", 22: "Coffee",
            }
            crop = default_map.get(pred_num, "Unknown crop")

        result = f"{crop} is the best crop to be cultivated right there."
        return render_template("index.html", result=result)

    except Exception as e:
        # Show the error in the UI so you can debug
        return render_template("index.html", result=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
