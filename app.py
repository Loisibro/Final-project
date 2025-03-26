#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient


# In[ ]:


app = Flask(__name__)


# In[ ]:


# Replace with your MongoDB connection string
client = MongoClient("mongodb+srv://loisibro:<db_password>@testcluster.ic1q6.mongodb.net/?retryWrites=true&w=majority&appName=TestCluster")
db = client["surveyDB"]          # Database name
collection = db["users"]         # Collection name


# In[ ]:


@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            gender = request.form['gender']
            total_income = float(request.form['total_income'])
            
            expenses = {}
            categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
            for category in categories:
                amount = request.form.get(f"{category}_amount", 0.0)
                expenses[category] = float(amount) if amount else 0.0

            user_data = {
                'age': age,
                'gender': gender,
                'total_income': total_income,
                'expenses': expenses
            }
            users_collection.insert_one(user_data)
            return redirect(url_for('thank_you'))
        except Exception as e:
            return f"An error occurred: {str(e)}", 400

    return render_template('form.html')


# In[ ]:


@app.route('/thank_you')
def thank_you():
    return "Thank you for participating!"

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,  # Keep debug for development
        use_reloader=False  # Disable problematic reloader
    )


# In[ ]:




