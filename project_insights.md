# Customer Shopping Behavior Analysis

## 1. Project Overview

This project analyzes customer shopping behavior to identify purchasing patterns, customer preferences, and sales trends.

The analysis uses SQL for data exploration and Power BI for data visualization and business insights.

### Objectives
- Understand customer purchasing patterns.
- Identify popular product categories.
- Analyze customer spending behavior.
- Examine the impact of discounts on purchases.
- Generate actionable business insights.

## 2. Key Business Questions
Which product categories generate the highest sales?
Which age group spends the most?
Do subscribed customers spend more than non-subscribed customers?
Which products are most popular among customers?
Does discount usage influence purchasing behaviour?
Which season has the highest purchasing activity?
Does product review rating influence customer preferences?
Which customer segments have the highest average spending?

## 3. Key Findings

### 3.1 Revenue by Product Category
- Clothing generated the highest revenue of $104,264.
- Accessories generated $74,200.
- Footwear generated $36,093.
- Outerwear generated the lowest revenue of $18,524.

### 3.2 Revenue by Age Group
- Customers aged 51–70 generated the highest total revenue of $88,480.
- The 36–50 age group generated $65,629.
- The 26–35 age group generated $44,342.
- The 18–25 age group generated $34,630.

Note: Higher total revenue does not necessarily mean higher average spending per customer.

### 3.3 Subscription Analysis
- Non-subscribed customers generated $170,436 in revenue.
- Subscribed customers generated $62,645.
- Average purchase values were approximately $59.87 for non-subscribers and $59.49 for subscribers.

The average purchase values are very similar.

### 3.4 Popular Products
- Blouse, Pants, and Jewelry were among the most purchased products, with 171 purchases each.
- No single product showed a strong lead over the others.

### 3.5 Seasonal Sales
- Fall generated the highest revenue at $60,018.
- Spring generated $58,679.
- Winter generated $58,607.
- Summer generated $55,777.

### 3.6 Discount Analysis
- 2,223 purchase records had no discount.
- 1,677 purchase records had a discount.
- Approximately 57% of purchases were made without discounts.

### 3.7 Customer Ratings
- Footwear received the highest average rating of approximately 3.79.
- Accessories followed at 3.77.
- Outerwear received 3.75.
- Clothing received 3.72.

The rating differences across categories were relatively small.

## 4. Business Recommendations

### 4.1 Focus on High-Revenue Categories
Clothing and Accessories generate the largest share of revenue. The business should maintain product availability and explore opportunities to expand these categories.

### 4.2 Develop Age-Based Marketing Strategies
Customers aged 51–70 generate the highest total revenue. Businesses can study their product preferences and develop relevant marketing campaigns for different age groups.

### 4.3 Improve Subscription Programs
Subscribed customers contribute less total revenue than non-subscribers. The business should review its subscription benefits and consider introducing more attractive offers to encourage subscriptions.

### 4.4 Promote Popular Products
Blouse, Pants, and Jewelry are among the most purchased products. Businesses can maintain sufficient inventory and use these products in promotional campaigns.

### 4.5 Plan Seasonal Marketing
Fall records the highest revenue. Businesses can prepare seasonal campaigns and inventory plans based on purchasing trends.

### 4.6 Evaluate Discount Strategies
Most purchases occurred without discounts. Businesses should evaluate whether discounts are necessary for every product or whether targeted offers would be more effective.

### 4.7 Improve Customer Satisfaction
Although average ratings are relatively close across categories, businesses should monitor customer feedback and identify opportunities to improve product quality and service.

## 5. Dataset Limitations

1. **Limited Dataset:** The analysis is based on 3,900 purchase records, which may not represent the entire customer population.

2. **Missing Values:** The original dataset contained 37 missing values in the review_rating column. These were handled using category-wise median imputation.

3. **Limited Time Information:** The dataset contains seasonal information but does not provide exact purchase dates. Therefore, detailed monthly or yearly trends cannot be analyzed.

4. **Customer Spending:** Total revenue by age group does not necessarily represent average spending per individual customer.

5. **No Causal Evidence:** The analysis identifies relationships and patterns but cannot prove that discounts, subscriptions, or ratings directly cause changes in purchasing behavior.

6. **Dataset-Specific Results:** The findings represent this particular dataset and should not automatically be generalized to all retail businesses.
