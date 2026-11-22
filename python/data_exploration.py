

import pandas as pd

# 1. LOAD THE DATASET
# Load the shopping behavior data into a DataFrame
df = pd.read_csv("data/customer_shopping_behavior.csv")

# 2. TAKE A FIRST LOOK AT THE DATA
# Check the first few rows to get an idea of the dataset
print("\nFirst 5 Rows:")
print(df.head())

# Check how many rows and columns the dataset contains
print("\nDataset Shape:")
print(df.shape)

# Take a look at all the available columns
print("\nColumn Names:")
print(df.columns.tolist())


# 3. UNDERSTAND THE DATASET STRUCTURE
# Get an overview of column names, data types and non-null values
print("\nDataset Information:")
df.info()


# 4. CHECK FOR MISSING VALUES
# Find out if any columns have missing data
print("\nMissing Values:")
print(df.isnull().sum())


# 5. CHECK FOR DUPLICATE RECORDS
# See if the dataset contains any repeated rows
print("\nDuplicate Records:")
print(df.duplicated().sum())


# 6. GET A STATISTICAL OVERVIEW
# Look at basic statistics like mean, standard deviation,
# minimum, maximum and quartiles for numerical columns
print("\nStatistical Summary:")
print(df.describe())


# 7. EXPLORE CATEGORICAL DATA
# See how customers are distributed across genders
print("\nGender Distribution:")
print(df["Gender"].value_counts())

# Check how many purchases were made in each product category
print("\nCategory Distribution:")
print(df["Category"].value_counts())

# Find out how purchases are distributed across seasons
print("\nSeasonal Distribution:")
print(df["Season"].value_counts())


# 8. EXPLORE CUSTOMER SHOPPING PREFERENCES

# Check how many customers have an active subscription
print("\nSubscription Status:")
print(df["Subscription Status"].value_counts())

# Find out which shipping methods customers use most often
print("\nShipping Type Distribution:")
print(df["Shipping Type"].value_counts())

# Check which payment methods are most commonly used
print("\nPayment Method Distribution:")
print(df["Payment Method"].value_counts())


# 9. TAKE ANOTHER LOOK AT SUBSCRIPTION STATUS

# Compare the number of subscribed and non-subscribed customers
print("\nSubscription Status:")
print(df["Subscription Status"].value_counts())


# 10. CREATE A SEPARATE COPY FOR CLEANING

# Keep the original dataset unchanged and work on a copy
df_clean = df.copy()

# Check whether the copied dataset has the same dimensions
print("\nClean Dataset Shape:")
print(df_clean.shape)


# 11. INVESTIGATE MISSING REVIEW RATINGS

# Check which product categories have missing review ratings
print("\nMissing Ratings by Category:")
print(
    df_clean[df_clean["Review Rating"].isnull()]
    .groupby("Category")
    .size()
)

# Find the median review rating for each category
print("\nMedian Rating by Category:")
print(
    df_clean.groupby("Category")["Review Rating"].median()
)


# 12. FILL IN MISSING REVIEW RATINGS

# Use the median rating of each product category
# to fill in its missing review ratings
df_clean["Review Rating"] = df_clean.groupby("Category")[
    "Review Rating"
].transform(
    lambda values: values.fillna(values.median())
)

# Check whether any missing values are still left
print("\nMissing Values After Cleaning:")
print(df_clean.isnull().sum())

# Get the total number of missing values in the dataset
print("\nTotal Missing Values:")
print(df_clean.isnull().sum().sum())


# 13. CLEAN UP THE COLUMN NAMES

# Make column names lowercase and replace spaces with underscores
# Also remove special characters to keep the names consistent
df_clean.columns = (
    df_clean.columns
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-z0-9_]", "", regex=True)
)

# Check how the column names look after cleaning
print("\nUpdated Column Names:")
print(df_clean.columns.tolist())


# 14. CHECK THE RELATIONSHIP BETWEEN DISCOUNTS AND PROMO CODES

# Check how many purchases had a discount applied
print("\nDiscount Applied Distribution:")
print(df_clean["discount_applied"].value_counts())

# Check how many purchases used a promo code
print("\nPromo Code Used Distribution:")
print(df_clean["promo_code_used"].value_counts())

# Compare both columns to see if they contain the same information
print("\nDiscount vs Promo Code:")
print(
    pd.crosstab(
        df_clean["discount_applied"],
        df_clean["promo_code_used"]
    )
)


# 15. REMOVE THE REDUNDANT COLUMN

# Remove promo_code_used since it contains the same information
# as discount_applied and does not add anything new
df_clean = df_clean.drop(columns=["promo_code_used"])

# Check the dataset dimensions after removing the column
print("\nDataset Shape After Removing Redundant Column:")
print(df_clean.shape)

# See which columns are left in the dataset
print("\nRemaining Columns:")
print(df_clean.columns.tolist())


# 16. RUN FINAL DATA QUALITY CHECKS

# Check the final number of rows and columns
print("\nFinal Dataset Shape:")
print(df_clean.shape)

# Make sure no missing values remain
print("\nTotal Missing Values:")
print(df_clean.isnull().sum().sum())

# Check if there are any duplicate rows
print("\nTotal Duplicate Records:")
print(df_clean.duplicated().sum())

# Review the data types of all columns
print("\nFinal Data Types:")
print(df_clean.dtypes)

# Take a final look at the cleaned dataset
print("\nCleaned Dataset Preview:")
print(df_clean.head())


# 17. SAVE THE CLEANED DATASET

# Export the cleaned data as a new CSV file
df_clean.to_csv(
    "data/customer_shopping_behavior_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")

# 18. ANALYSE REVENUE BY PRODUCT CATEGORY

# Calculate total revenue generated by each product category
category_revenue = (
    df_clean.groupby("category")["purchase_amount_usd"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Product Category:")
print(category_revenue)