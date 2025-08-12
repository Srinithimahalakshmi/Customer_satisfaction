
#  Customer Satisfaction Prediction

##  Overview
A machine learning project leveraging **AdaBoost** to classify customer satisfaction levels based on feedback, service quality, and purchase history. The pipeline includes data preprocessing, feature selection, model training, and evaluation—helping businesses make informed decisions.

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📬 Contact](#-contact)  

---

##  Installation
```bash
git clone https://github.com/Srinithimahalakshmi/Customer_satisfaction.git
cd Customer_satisfaction

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Usage

### 1. Explore & Train via Notebook

```bash
jupyter notebook model_training.ipynb
```

### 2. Run Web Interface

```bash
python app.py
```

Then open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** to interact with live predictions.

---

## Project Structure

```
Customer_satisfaction/
├── Customer Satisfaction Scores and Behavior Data.csv  # Dataset
├── model_training.ipynb                               # Training & evaluation notebook
├── agglo_model.joblib                                 # Trained clustering model (if applicable)
├── scaler.joblib                                      # Feature scaler
├── app.py                                             # Flask app for live predictions
├── templates/
│   └── index.html                                     # UI template
├── static/
│   └── [CSS/JS assets]                                # Frontend resources
├── requirements.txt                                   # Python dependencies
└── README.md                                          # This documentation
```

---

## Results

* Achieved strong classifier performance (insert metrics: Accuracy, Precision, Recall, F1-Score).
* Visualization outputs—such as confusion matrices and feature importance—available within the notebook or web interface.

*(Feel free to update metrics and add visual references to support the results.)*

---

## Contributing

Contributions are always welcome! A few ways to help:

* Improve data preprocessing or feature extraction
* Tune or compare with other models—like Random Forest, XGBoost
* Enhance model explanations with SHAP or LIME
* Improve app UI or add additional user flows

**How to contribute**:

1. Fork the project
2. Branch off: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m "Add feature XYZ"`
4. Push & submit a Pull Request

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
🔗 **GitHub**: [same handle](https://github.com/Srinithimahalakshmi)

---

⭐ *If this project is helpful, I’d greatly appreciate a star!*

