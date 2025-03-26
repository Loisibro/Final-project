#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
from pymongo import MongoClient


# In[4]:


import csv
import os

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

    def to_dict(self):
        """ Return a dictionary representation suitable for writing to CSV. """
        user_dict = {
            "Age": self.age,
            "Gender": self.gender,
            "Total_Income": self.total_income
        }
        # Merge expense categories into the user_dict
        for category, amount in self.expenses.items():
            user_dict[category] = amount
        return user_dict

    @staticmethod
    def export_to_csv(user_list, csv_filepath):
        """ 
        Writes a list of User objects to a CSV file. 
        """
        if not user_list:
            return

        # Extract all expense categories from the first user for CSV headers
        first_user_expenses = user_list[0].expenses.keys()

        # Build header
        fieldnames = ["Age", "Gender", "Total_Income"] + list(first_user_expenses)

        file_exists = os.path.exists(csv_filepath)
        
        with open(csv_filepath, mode='a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header only if file doesn't exist
            if not file_exists:
                writer.writeheader()

            for user in user_list:
                writer.writerow(user.to_dict())


# In[ ]:




