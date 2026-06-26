# 🚗 Car Price Prediction System

A Machine Learning web application that predicts the selling price of a used car based on its details such as company, model, manufacturing year, fuel type, and kilometers driven.

---

## 📌 Project Overview

This project uses a **Random Forest Regression** model to estimate the selling price of used cars. The application is built with **Python**, **Flask**, **Bootstrap 5**, and **Scikit-learn**.

Users can:

* Select a car company
* Choose a car model
* Enter the manufacturing year
* Select the fuel type
* Enter the kilometers driven
* Get an estimated selling price instantly

---

## 🚀 Features

* Machine Learning based price prediction
* Dynamic Car Model dropdown based on selected Company
* Clean and responsive Bootstrap UI
* Flask backend
* Fast prediction using a trained Random Forest model
* Easy to use interface

---

## 🛠️ Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* Random Forest Regressor
* HTML5
* CSS3
* Bootstrap 5
* JavaScript

---

## 📂 Project Structure

```
Car-Price-Prediction/
│
├── app.py
├── model.pkl
├── columns.pkl
├── quikr_car.csv
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── templates/
    └── index.html
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Akshay-achar-2/Car-Price-Prediction.git
```

Move into the project folder:

```bash
cd Car-Price-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📸 Application Preview

* Select Company
* Select Car Model
* Enter Manufacturing Year
* Select Fuel Type
* Enter Kilometers Driven
* Click **Predict Price**
* View the estimated car price

---

## 📊 Machine Learning Model

* Algorithm: Random Forest Regression
* Dataset: Quikr Used Car Dataset
* Data Preprocessing:

  * Missing value handling
  * Data cleaning
  * One-Hot Encoding
* Model Training using Scikit-learn

---

## 🔮 Future Improvements

* Car image preview
* Price trend charts
* User login system
* Save prediction history
* Deploy online using Render

---

## 👨‍💻 Developed By

**Akshay**

AI & Machine Learning Intern

InternPE Internship Project

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
