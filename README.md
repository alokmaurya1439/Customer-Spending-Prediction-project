## Customer Spending Prediction

# Project Setup

1) create virtual environment:
'''
python -m venv myenv
'''

2) activate virtual environment:
'''
myenv\Scripts\activate
'''

3) Install dependencies:
'''
pip install -r requirements.txt
'''

Dataset Description
Use a suitable customer dataset containing the columns below. If a dataset has not been provided, create or obtain a CSV file with realistic sample records. The target column must be Amount_Spent.
Column	                        Type	                                Description
Age	                            Numerical	                            Customer age
Annual_Income	                Numerical	                            Customer annual income
Website_Visits	                Numerical	                            Number of website visits per month
Previous_Purchases	            Numerical	                            Number of previous purchases
Membership_Type	                Categorical	                            Bronze, Silver, or Gold
Preferred_Category	            Categorical	                            Electronics, Fashion, Home, or Beauty
City_Tier	                    Categorical	                            Tier 1, Tier 2, or Tier 3
Discount_Used	                Categorical	                            Yes or No
Amount_Spent	                Numerical target	                    Customer spending amount to predict

Problem type: Regression, because Amount_Spent is a continuous numerical value.