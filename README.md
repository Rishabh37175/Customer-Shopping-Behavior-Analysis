# Customer Shopping Behavior Analysis

An end-to-end data analytics project focused on understanding customer shopping patterns and exploring what the purchase data tells us about customer preferences, product demand, and sales trends.

## Project Overview

In this project, I worked with a dataset containing 3,900 customer purchase records. My goal was to explore the data, identify useful patterns, and present the findings in a way that could help a business better understand its sales and customers.

I used Python for data cleaning and exploratory analysis, MySQL and SQL to work with the data and answer business questions, and Power BI to build an interactive dashboard.

## Tools & Technologies

- **Python & Pandas:** Used for data cleaning, manipulation, and exploratory analysis.
- **MySQL:** Used to store and manage the cleaned dataset.
- **SQL:** Used to answer business questions and analyze purchasing patterns.
- **Power BI:** Used to create a dashboard and present the key findings.
- **VS Code:** Used as the development environment.

## Project Structure


Customer_Shopping_Behavior/
│
├── data/
│   ├── customer_shopping_behavior.csv
│   └── customer_shopping_behavior_cleaned.csv
│
├── python/
│   ├── data_exploration.py
│   ├── eda.py
│   └── load_to_mysql.py
│
├── sql/
│   └── sql_analysis.sql
│
├── screenshots/
│   └── dashboard_overview.png
│
├── Customer_Shopping_Behavior_Analysis.pbix
├── project_insights.md
└── README.md

## Data Cleaning & Preparation

I started by exploring the original dataset, which contained 3,900 records and 18 columns.

During the initial inspection, I found 37 missing values in the `review_rating` column. I handled these by filling them with the median rating of their respective product categories.

I also:
- Checked the dataset for duplicate records.
- Standardized column names to make them easier to work with.
- Compared `discount_applied` and `promo_code_used`.
- Removed `promo_code_used` because both columns contained exactly the same information in this dataset.

After cleaning, the dataset contained **3,900 records and 17 columns**, with no missing values or duplicate records.

## Key Findings

After exploring the dataset and running SQL queries, I found a few interesting patterns.

| Analysis | Result |
|---|---:|
| Total Revenue | $233,081 |
| Total Purchase Records | 3,900 |
| Average Purchase Amount | $59.76 |
| Average Review Rating | 3.75 |
| Highest Revenue Category | Clothing |
| Highest Revenue Season | Fall |
| Most Purchased Products | Blouse, Pants, Jewelry |

### Revenue by Product Category

| Category | Revenue |
|---|---:|
| Clothing | $104,264 |
| Accessories | $74,200 |
| Footwear | $36,093 |
| Outerwear | $18,524 |

Clothing generated the highest revenue, followed by Accessories. These two categories together contributed the largest share of total sales.

### A Few More Observations

- The 51–70 age group contributed the highest total revenue among the age groups.
- Non-subscribers generated more total revenue, mainly because they had more purchase records. However, the average purchase amount was almost the same for subscribers and non-subscribers.
- PayPal had the highest number of purchase records among the payment methods.
- Footwear had the highest average review rating, although the difference between categories was small.

## Power BI Dashboard

Once the data analysis was complete, I used Power BI to bring the findings together in one dashboard.

The dashboard contains four KPI cards and nine charts covering:

- Revenue by product category
- Revenue by season
- Revenue by age group
- Purchases by gender
- Revenue by subscription status
- Purchases by discount status
- Purchases by payment method
- Purchases by shipping type
- Average review rating by category

### Dashboard Preview

![Customer Shopping Behavior Dashboard](screenshot/dashboard_overview.png)

## SQL Analysis

I wrote 15 SQL queries to explore different aspects of the dataset and answer business-related questions.

Some of the areas I explored include:

- Which product categories generate the most revenue?
- Which products are purchased most frequently?
- How does revenue vary across different age groups?
- How do subscribers and non-subscribers compare?
- Which payment methods and shipping options are used most often?
- Which season records the highest revenue?
- How are purchases distributed by discount status?
- Which products rank among the top three in each category?

## Limitations

While working on this project, I also identified a few limitations in the dataset:

- Every customer ID appears only once, so customer lifetime value and repeat purchases per customer cannot be calculated.
- There are no exact transaction dates, which limits monthly and yearly trend analysis.
- Missing review ratings were filled using category-wise median values, so those values are estimates rather than original customer ratings.
- The analysis shows patterns and relationships in the available data but does not prove cause-and-effect relationships.

## What I Learned

Through this project, I got practical experience with different stages of the data analytics process, including:

- Cleaning and preparing raw data using Python.
- Exploring data and identifying patterns with Pandas.
- Writing SQL queries to answer business questions.
- Connecting MySQL data to Power BI.
- Building a dashboard to communicate analytical findings.

This project helped me understand how Python, SQL, and Power BI can work together in a single data analytics workflow.

## 🙏 Credits and Acknowledgements

This project was inspired by the end-to-end data analytics tutorial by **Amlan Mohanty**.

- **Project Tutorial:** [Complete Data Analytics Portfolio Project in 6 Easy Steps](https://youtu.be/5PrZvPeUw60)
- **Original GitHub Repository:** [Customer Trends Data Analysis – SQL, Python and Power BI](https://github.com/amlanmohanty1/customer-trends-data-analysis-SQL-Python-PowerBI)
- **Dataset:** [Customer Shopping Behavior CSV](https://github.com/amlanmohanty1/customer-trends-data-analysis-SQL-Python-PowerBI/blob/main/customer_shopping_behavior.csv)

The tutorial provided the initial project structure and learning direction. I implemented the project using my own workflow, including data cleaning with Python, analysis with MySQL, and an interactive Power BI dashboard.

Credit goes to Amlan Mohanty for the original tutorial and dataset repository.