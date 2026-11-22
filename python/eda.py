import pandas as pd


# 1. LOAD THE CLEANED DATASET

df = pd.read_csv("data/customer_shopping_behavior_cleaned.csv")


# 2. CHECK THE DATASET

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# 3. REVENUE BY PRODUCT CATEGORY

category_revenue = (
    df.groupby("category")["purchase_amount_usd"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Product Category:")
print(category_revenue)

# 4. PURCHASE COUNT BY PRODUCT CATEGORY

category_purchases = df["category"].value_counts()

print("\nNumber of Purchases by Category:")
print(category_purchases)

# 5. AVERAGE PURCHASE AMOUNT BY CATEGORY

category_average = (
    df.groupby("category")["purchase_amount_usd"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Purchase Amount by Category:")
print(category_average)

# 6. MOST PURCHASED PRODUCTS

item_purchases = df["item_purchased"].value_counts()

print("\nMost Purchased Products:")
print(item_purchases)

# 7. REVENUE BY SEASON

season_revenue = (
    df.groupby("season")["purchase_amount_usd"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Season:")
print(season_revenue)

# 7.1 PURCHASE COUNT BY SEASON

season_purchases = df["season"].value_counts()

print("\nNumber of Purchases by Season:")
print(season_purchases)

# 8. REVENUE BY GENDER

gender_revenue = (
    df.groupby("gender")["purchase_amount_usd"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Gender:")
print(gender_revenue)

# 9. REVENUE BY AGE GROUP

# Create age groups
df["age_group"] = pd.cut(
    df["age"],
    bins=[17, 25, 35, 50, 70],
    labels=["18-25", "26-35", "36-50", "51-70"]
)

# Calculate revenue by age group
age_group_revenue = (
    df.groupby("age_group", observed=True)["purchase_amount_usd"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Age Group:")
print(age_group_revenue)

# 10. REVENUE BY SUBSCRIPTION STATUS

subscription_revenue = (
    df.groupby("subscription_status")["purchase_amount_usd"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Subscription Status:")
print(subscription_revenue)

# 11. PURCHASE COUNT BY PAYMENT METHOD

payment_counts = df["payment_method"].value_counts()

print("\nPurchase Count by Payment Method:")
print(payment_counts)

# 12. PURCHASE COUNT BY SHIPPING TYPE

shipping_counts = df["shipping_type"].value_counts()

print("\nPurchase Count by Shipping Type:")
print(shipping_counts)

# 13. AVERAGE REVIEW RATING BY CATEGORY

category_ratings = (
    df.groupby("category")["review_rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Review Rating by Category:")
print(category_ratings)

# 14. AVERAGE PURCHASE AMOUNT BY SUBSCRIPTION STATUS

subscription_average = (
    df.groupby("subscription_status")["purchase_amount_usd"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Purchase Amount by Subscription Status:")
print(subscription_average) 