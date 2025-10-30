# Custmer Churn Prediction

This is a **Full-Stack Web Application**  It focuses on **Customer Churn Prediction** and **Sales Forecasting**, using **Machine Learning models** integrated with a modern frontend and backend architecture.

---

## 🚀 Features

- **User Authentication** with JWT (Login & Register)
- **Churn Prediction Dashboard**  
  - Displays 10 products  
  - Pie charts for High, Medium, and Low Churn risk customers  
  - ML Model: **K-Means Clustering**
- **Sales Forecasting Dashboard**  
  - Shows Top 10 products  
  - Sales trends and visualizations  
  - ML Model: **Facebook Prophet**
- **Interactive Charts** using modern visualization libraries
- **Backend API** with Flask
- **Frontend** with React and TailwindCSS
- **Database Integration** for user data and results

---

## 🖼️ Screenshots

### 🔐 Login & Register  
![Login Page](/screenshots/login.png)

### 📊 Churn Prediction Dashboard  
![Churn Dashboard](/screenshots/churn.png)

### 📈 Sales Forecasting Dashboard  
![Forecast Dashboard](/screenshots/sales.png)

*(Place your screenshots inside a folder named `screenshots` in your project root and rename accordingly.)*  

---

## 🛠️ Tech Stack

### Frontend
- React.js  
- TailwindCSS  
- Chart.js / Recharts  

### Backend
- Flask (Python)  
- REST APIs  
- JWT Authentication  

### Machine Learning
- **K-Means** for Customer Churn Prediction  
- **Prophet** for Sales Forecasting  

### Database
- MongoDB / MySQL (depending on setup)

---

## ⚙️ Installation & Setup

### Clone Repository
```bash
git clone https://github.com/Himanizambare/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```


## Backend Setup

```
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
python app.py

```
Backend will start on: http://127.0.0.1:5000/


## Frontend Setup


```
cd frontend
npm install
npm start
```
Frontend will start on: http://localhost:3000/


## System Flow
 -  User Login/Register → JWT Authentication

 -  Dashboard

 -  Churn Section → Displays product churn risk analysis (High/Medium/Low)

 -  Sales Forecast Section → Shows top 10 products with forecasted sales

 -  Visualization & Insights shown via charts
