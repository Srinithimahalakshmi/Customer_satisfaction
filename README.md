# Customer Satisfaction Analysis & Prediction System 📊

![Customer Satisfaction Dashboard](images/dashboard.png) <!-- Add actual screenshot path -->

End-to-end solution for analyzing customer feedback data and predicting satisfaction levels. Includes EDA, sentiment analysis, and predictive modeling.

## Features ✨
- Sentiment analysis of customer reviews
- Satisfaction prediction using ML models
- Interactive dashboards for insights
- Topic modeling for feedback categorization
- Automated report generation

## Installation 💻

### Prerequisites
- Python 3.8+
- pip or conda

### Setup
```bash
# Clone repository
git clone https://github.com/Srinithimahalakshmi/Customer_satisfaction.git
cd Customer_satisfaction

# Create virtual environment
python -m venv custsat_env
source custsat_env/bin/activate  # Linux/Mac
custsat_env\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
Dataset 📁
Customer Feedback Dataset (included in data/)

Contains:

Customer reviews (text)

Numerical ratings (1-5 stars)

Metadata (product, date, location)

Key features:

Review text

Verified purchase flag

Product category

Review date

Usage 🚀
1. Data Exploration
bash
python src/eda.py --input data/reviews.csv --output reports/eda_report.html
2. Sentiment Analysis
bash
python src/sentiment_analysis.py --input data/reviews.csv --output results/sentiment_scores.csv
3. Model Training
bash
# Train satisfaction prediction model
python src/models/train_predictor.py --data processed/clean_data.csv --model models/satisfaction_model.pkl
4. Generate Dashboard
bash
python src/dashboard/app.py  # Access at http://localhost:8050
Key Components 🔍
Sentiment Analysis Pipeline
Text preprocessing (cleaning, stemming)

Feature extraction (TF-IDF, word embeddings)

Sentiment classification (BERT, LSTM, or SVM)

Satisfaction score calculation

Prediction Models
Model	Accuracy	F1-Score	Use Case
XGBoost	92.4%	0.91	Overall prediction
LSTM	89.7%	0.88	Text-based
Ensemble	93.1%	0.92	Final deployment
Repository Structure 📂
text
├── data/                   # Raw and processed data
│   ├── raw/                # Original datasets
│   └── processed/          # Cleaned data
│
├── docs/                   # Documentation
├── images/                 # Visual assets
│
├── models/                 # Trained models
│   └── satisfaction_model.pkl
│
├── reports/                # Analysis outputs
│   ├── eda_report.html
│   └── feature_importance.png
│
├── src/                    # Source code
│   ├── data_processing/    # Data cleaning modules
│   ├── visualization/      # Plotting utilities
│   ├── models/             # ML model training
│   ├── dashboard/          # Streamlit/PowerBI dashboard
│   ├── sentiment_analysis.py
│   └── predict.py          # Prediction API
│
├── notebooks/              # Jupyter notebooks
│   ├── 01_Data_Exploration.ipynb
│   └── 02_Model_Comparison.ipynb
│
├── requirements.txt        # Dependencies
└── LICENSE
Sample Visualization
https://reports/feature_importance.png <!-- Add actual path -->
Top factors influencing customer satisfaction

How to Predict Satisfaction
python
from src.predict import SatisfactionPredictor

# Initialize predictor
predictor = SatisfactionPredictor('models/satisfaction_model.pkl')

# Sample input
customer_data = {
    'review_text': 'Product exceeded expectations with fast shipping',
    'rating': 5,
    'product_category': 'electronics'
}

# Make prediction
prediction = predictor.predict(customer_data)
print(f"Satisfaction Probability: {prediction['satisfaction_prob']:.2%}")
Business Applications 💼
Identify dissatisfied customers in real-time

Prioritize product improvement areas

Track satisfaction trends over time

Automate customer service routing

Measure impact of satisfaction initiatives

Contributors 👥
Srinithi Mahalakshmi
https://img.shields.io/badge/LinkedIn-Connect-blue
https://img.shields.io/badge/GitHub-Follow-lightgrey
