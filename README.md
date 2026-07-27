# 🎓 Student Placement Predictor

A Machine Learning web application that predicts whether a student is likely to be placed based on academic performance, communication skills, projects, internship experience, and other factors.

## 🚀 Features

- Predicts student placement using a trained Random Forest model.
- Interactive web interface built with Streamlit.
- User-friendly input form.
- Real-time prediction results.

## 🛠️ Tech Stack

- Python
- Scikit-learn
- Streamlit
- Pandas
- Joblib

## 📊 Dataset Features

- IQ
- CGPA
- Academic Performance
- Internship Experience
- Extra Curricular Score
- Communication Skills
- Projects Completed

## 🤖 Machine Learning Models Compared

- Logistic Regression
- Decision Tree
- Random Forest ✅ (Best Model)
- K-Nearest Neighbors (KNN)

## 📈 Best Model Performance

Random Forest achieved the best performance on the dataset and was selected for deployment.

## 📂 Project Structure

```
student-placement-predictor/
│
├── app.py
├── random_forest_model.pkl
├── requirements.txt
├── README.md
├── student_placement.ipynb
└── college_student_placement_dataset.csv
```

## ▶️ Run Locally

```bash
git clone https://github.com/TharunThurpinti/student-placement-predictor.git
cd student-placement-predictor

pip install -r requirements.txt

streamlit run app.py
```

## 👨‍💻 Author

**Tharun Kumar**