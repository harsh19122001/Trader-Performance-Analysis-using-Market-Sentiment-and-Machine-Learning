# 📈 Trader Performance Analysis using Market Sentiment & Machine Learning

## 📌 Project Overview

This project analyzes the relationship between Bitcoin Market Sentiment (Fear & Greed Index) and trader performance using historical Hyperliquid trading data.

The objective is to understand how market sentiment influences trader behavior, profitability, and trading patterns while building a machine learning model to predict whether a trade is likely to result in Profit or Loss.

This project demonstrates a complete end-to-end Data Science workflow including Data Cleaning, Exploratory Data Analysis (EDA), Statistical Testing, Machine Learning, Trader Segmentation, and Streamlit Deployment.

---

# 🎯 Problem Statement

Financial markets are highly influenced by investor sentiment.

This project investigates:

- Does market sentiment affect trader profitability?
- Do traders behave differently during Fear and Greed periods?
- Can machine learning predict whether a trade will be profitable?

---

# 📂 Dataset

The project combines two datasets.

### 1. Bitcoin Fear & Greed Index

Contains daily market sentiment.

Columns:

- Date
- Classification
    - Extreme Fear
    - Fear
    - Neutral
    - Greed
    - Extreme Greed

---

### 2. Historical Hyperliquid Trader Data

Contains historical trading activity.

Main Columns

- Account
- Coin
- Execution Price
- Size Tokens
- Size USD
- Side
- Direction
- Fee
- Closed PnL
- Timestamp

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle

---

# 📊 Project Workflow

### Data Collection

- Imported both datasets
- Checked dataset dimensions
- Identified missing values
- Removed duplicate records

---

### Data Cleaning

- Converted timestamps into datetime format
- Created daily trading records
- Merged trader dataset with market sentiment dataset
- Created new engineered features

---

### Feature Engineering

Created features such as

- Win
- Trade Result
- Profit Bucket
- Hour
- Month
- Trade Size
- Fee Percentage

---

### Exploratory Data Analysis

Performed

- Market Sentiment Distribution
- Profit Analysis
- Trade Frequency Analysis
- Trade Size Distribution
- Buy vs Sell Analysis
- Coin Analysis
- Top Trader Analysis
- Fee Distribution
- Correlation Heatmap
- Daily Trading Trend

---

### Statistical Testing

Performed One-Way ANOVA to determine whether trader profitability differs significantly across different market sentiment categories.

---

### Trader Segmentation

Used

- StandardScaler
- K-Means Clustering
- PCA Visualization

to identify different trader groups based on

- Trade Frequency
- Profitability
- Trade Size
- Fees
- Win Rate

---

### Machine Learning

Models Implemented

- Logistic Regression
- Random Forest Classifier

Target Variable

- Win
    - 1 = Profit
    - 0 = Loss

Features Used

- Market Sentiment
- Coin
- Execution Price
- Size Tokens
- Size USD
- Side
- Direction
- Fee
- Hour
- Month

---

# 📈 Model Performance

Model Used

Random Forest Classifier

Test Accuracy

**98.75%**

---

# 📊 Business Insights

Some important findings include

### ✔ Market sentiment influences trader profitability.

### ✔ Different trader segments exhibit distinct trading behaviors.

### ✔ Trade Size and Execution Price significantly influence trade outcomes.

### ✔ Certain trading hours produce better average profitability.

### ✔ A small number of traders generate a large share of total profits.

---

# 💡 Strategy Recommendations

- Reduce position size during Extreme Fear conditions.

- Monitor high-risk traders with consistently low win rates.

- Use market sentiment together with trade size for improved trading decisions.

- Use machine learning predictions to support risk management.

---

# 🌐 Streamlit Application

The project includes an interactive Streamlit application that allows users to

- Select Market Sentiment
- Select Coin
- Enter Trade Details
- Predict Profit/Loss
- View Prediction Confidence

---

# 📁 Project Structure

```
Trader-Performance-Analysis-using-Market-Sentiment-and-Machine-Learning

│
├── app.py
├── Trader_Performance_Analysis.ipynb
├── random_forest_model.pkl
├── encoders.pkl
├── requirements.txt
├── README.md
├── data
│   ├── fear_greed_index.csv
│   └── historical_trader_data.csv
│
├── images
│
└── LICENSE
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Trader-Performance-Analysis-using-Market-Sentiment-and-Machine-Learning.git
```

Go to the project folder

```bash
cd Trader-Performance-Analysis-using-Market-Sentiment-and-Machine-Learning
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 📦 Requirements

- streamlit
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

---

# 🚀 Future Improvements

- XGBoost Model
- SHAP Explainability
- Batch Prediction
- Cloud Deployment
- Real-Time Market Data Integration
- Interactive Dashboard

---

# 👨‍💻 Author

**Harsh Jaiswal**

Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning

GitHub:
https://github.com/harsh19122001

LinkedIn:
https://www.linkedin.com/in/harsh-jaiswal-5a7039353

---

⭐ If you found this project useful, consider giving this repository a star.
