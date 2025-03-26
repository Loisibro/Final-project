
# Project Title

Final Project: **Survey Tool for Collecting and Analyzing Income/Expense Data**  

This repository contains a Flask application that collects user information (age, gender, income, and various expenses), stores that data in MongoDB (Atlas or local), exports it to a CSV file, and performs data analysis in a Jupyter notebook with visualizations.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Prerequisites and Installation](#prerequisites-and-installation)  
4. [Configuration](#configuration)  
5. [Running the Flask App](#running-the-flask-app)  
6. [Data Export to CSV](#data-export-to-csv)  
7. [Data Analysis Notebook](#data-analysis-notebook)  
8. [Deployment on AWS](#deployment-on-aws)  
9. [Project Structure](#project-structure)  
10. [Contributing](#contributing)  
11. [License](#license)

---

## Project Overview

The main objective is to:

1. Collect user data (age, gender, total income, expenses) via a Flask web form.  
2. Store data in MongoDB.  
3. Export data from MongoDB to a CSV file.  
4. Analyze the CSV data using Python (Jupyter notebook).  
5. Create visualizations (matplotlib) for reporting.

This project simulates a survey tool used in the healthcare industry to prepare for a product launch. You can adapt it for various data-collection scenarios.

---

## Features

- **Flask Web Form**: Simple HTML form with checkboxes and text fields for different expense categories.  
- **MongoDB Storage**: Uses `pymongo` to insert form submissions into a MongoDB database.  
- **Data Export**: A Python script/class to retrieve data from MongoDB and store it into `expenses.csv`.  
- **Data Analysis**: A Jupyter notebook that loads `expenses.csv`, computes summaries, and creates plots.  
- **Charts & Visualizations**: Visual charts (bar charts, etc.) showing:
  1. Which ages have the highest incomes.  
  2. Gender distribution across spending categories.
- **AWS Deployment** (optional): Host the Flask application on an EC2 instance or Elastic Beanstalk.

---

## Prerequisites and Installation

1. **Python 3.8+** recommended.  
2. **MongoDB** (Local or Atlas).  
3. **Pip** or **Conda** for package management.

### 1. Clone or Download the Repository

```bash
git clone https://github.com/YourUsername/my_flask_mongo_project.git
cd my_flask_mongo_project
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# Activate the environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Typical dependencies** might include:
- flask  
- pymongo  
- pandas  
- matplotlib  

*(If you have additional libraries, ensure they are listed in `requirements.txt`.)*

---

## Configuration

### MongoDB

1. **Local MongoDB**: Make sure your local MongoDB service is running on the default port (`mongodb://localhost:27017`).  
2. **MongoDB Atlas**:  
   - Create a cluster on [MongoDB Atlas](https://www.mongodb.com/atlas).  
   - Whitelist your IP address.  
   - Get the connection URI (e.g., `mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority`).  
   - Update the connection string in `app.py` (or wherever your database connection is specified).

Inside `app.py`, look for something like:
```python
# Example using MongoDB Atlas
from pymongo import MongoClient

ATLAS_CONNECTION_STRING = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = MongoClient(ATLAS_CONNECTION_STRING)
db = client["surveyDB"]
collection = db["users"]
```

---

## Running the Flask App

1. **Activate your virtual environment** (if not already activated).
2. **Run the Flask development server**:
   ```bash
   python app.py
   ```
3. **Open your browser** and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).  
4. **Submit test data** on the form.  
5. Confirm in your terminal or in MongoDB that the data was inserted.

---

## Data Export to CSV

If you have a separate script (for example, `export_to_csv.py`) that retrieves documents from MongoDB and writes them to a CSV file, run:

```bash
python export_to_csv.py
```

This script:
1. Connects to MongoDB.  
2. Retrieves all user documents.  
3. Writes them to `data/expenses.csv`.  

Check the `data/` folder for the newly created (or updated) CSV file.

---

## Data Analysis Notebook

1. **Navigate** to the `notebooks/` directory (if you have a dedicated directory for notebooks).
2. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```
3. **Open `analysis.ipynb`** (or your notebook’s file name) in the Jupyter interface.
4. **Run each cell** to:
   - Load `expenses.csv` into a pandas DataFrame.
   - Generate bar charts showing:
     1. Ages with the highest average income.  
     2. Gender distribution across spending categories.  
5. The notebook also **saves** the charts (`.png` files) for easy inclusion in a PowerPoint presentation.

---

## Deployment on AWS

### Option A: EC2

1. **Create** an AWS EC2 instance (Ubuntu or Amazon Linux).  
2. **SSH** into the instance.  
3. **Install** Python, pip, and any dependencies.  
4. **Clone** your GitHub repository onto the instance.  
5. **Update** the Flask app’s host/port settings or run with `gunicorn`:  
   ```bash
   pip install gunicorn
   gunicorn -w 4 app:app -b 0.0.0.0:80
   ```
6. **Open** port 80 (or 5000) in the security group inbound rules.  
7. **Navigate** to the public IP in your browser to see the running app.

### Option B: Elastic Beanstalk

1. **Install** the AWS EB CLI locally (`pip install awsebcli`).  
2. **Initialize** in your project directory: `eb init`.  
3. **Create** an environment: `eb create`.  
4. **Deploy**: `eb deploy`.  
5. **Update** your environment variables (like the MongoDB URI) in the EB console or your local `.ebextensions`.

---

## Project Structure

Below is an example directory layout:

```
my_flask_mongo_project/
│
├── app.py                  # Main Flask application
├── export_to_csv.py        # Optional script to export MongoDB data to CSV
├── UserClass.py            # “User” class definition (handles CSV export, etc.)
├── requirements.txt        # List of Python dependencies
├── templates/
│   └── index.html          # HTML form template
├── static/
│   └── (your static files: CSS, JS, images, if any)
├── data/
│   └── expenses.csv        # Generated CSV file from MongoDB data
├── notebooks/
│   └── analysis.ipynb      # Jupyter notebook for data analysis & visualizations
└── README.md               # Instructions for usage and setup
```

---

## Contributing

1. **Fork** the repository.  
2. Create a new **branch** for your feature or bug fix.  
3. **Commit** your changes.  
4. **Push** to your fork.  
5. Create a **Pull Request** in the original repo.

---
