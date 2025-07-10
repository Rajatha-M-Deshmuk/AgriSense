
# 🌱 Crop Recommendation System

This project is a machine learning-based web application that recommends the most suitable crop to cultivate based on soil and environmental parameters such as Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall.

## 🚀 Features

- 🌐 Web interface built using Flask & Bootstrap
- 🤖 Predicts the best crop using a trained Random Forest Classifier
- 📊 Clean and responsive UI for user input
- 🖼️ Displays recommendation with a crop image
- 📦 Easily deployable and customizable

## 📁 Project Structure

```
crop-recommendation-project/
├── app.py                     # Main Flask application
├── crop_model.pkl             # Trained ML model
├── Crop_recommendation.csv    # Dataset used for training
├── requirements.txt           # Python dependencies
├── static/
│   └── green-wheat-field.jpg  # Image used in result display
├── templates/
│   └── index.html             # Frontend HTML page
└── README.md                  # This documentation file
```



## 📦 Requirements

Install Python dependencies using:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
Flask
numpy
pandas
scikit-learn
matplotlib
seaborn
```

## 🧠 Machine Learning Model

The model is trained using a **Random Forest Classifier** on the [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset). It classifies the best crop among 22 options based on environmental input features.

## ▶️ How to Run

```bash
python app.py
```

Then open your browser and go to:

```
http://localhost:5000
```

## 🖼️ Sample Output

After submitting the soil and weather values, you’ll receive a recommendation like:

> 🌾 **Rice is the best crop to be cultivated right there.**


