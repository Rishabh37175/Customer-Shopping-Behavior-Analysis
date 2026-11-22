CREATE DATABASE IF NOT EXISTS customer_behavior;

USE customer_behavior;

CREATE TABLE IF NOT EXISTS customer_shopping_behavior (
    customer_id INT,
    age INT,
    gender VARCHAR(10),
    item_purchased VARCHAR(50),
    category VARCHAR(30),
    purchase_amount_usd INT,
    location VARCHAR(50),
    size VARCHAR(10),
    color VARCHAR(30),
    season VARCHAR(15),
    review_rating DECIMAL(3,1),
    subscription_status VARCHAR(5),
    shipping_type VARCHAR(30),
    discount_applied VARCHAR(5),
    previous_purchases INT,
    payment_method VARCHAR(30),
    frequency_of_purchases VARCHAR(20)
);


SHOW DATABASES;

SHOW TABLES;

DESCRIBE customer_shopping_behavior;

SELECT COUNT(*)
FROM customer_shopping_behavior;

SELECT *
FROM customer_shopping_behavior
LIMIT 10;

SELECT SUM(purchase_amount_usd) AS total_revenue
FROM customer_shopping_behavior;

SELECT COUNT(*) AS total_purchases
FROM customer_shopping_behavior;

SELECT AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping_behavior;

SELECT
    category,
    SUM(purchase_amount_usd) AS total_revenue
FROM customer_shopping_behavior
GROUP BY category
ORDER BY total_revenue DESC;

SELECT
    category,
    COUNT(*) AS total_purchases
FROM customer_shopping_behavior
GROUP BY category
ORDER BY total_purchases DESC;


-- Q1: Revenue Analysis by Product Category

SELECT
    category,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_revenue,
    ROUND(AVG(purchase_amount_usd), 2) AS average_purchase,
    ROUND(
        SUM(purchase_amount_usd) * 100.0 /
        (SELECT SUM(purchase_amount_usd)
         FROM customer_shopping_behavior),
        2
    ) AS revenue_percentage
FROM customer_shopping_behavior
GROUP BY category
ORDER BY total_revenue DESC;


-- Q2: Top 5 Most Purchased Products

SELECT
    item_purchased,
    COUNT(*) AS total_purchases
FROM customer_shopping_behavior
GROUP BY item_purchased
ORDER BY total_purchases DESC
LIMIT 5;


-- Q3: Revenue Analysis by Age Group

SELECT
    CASE
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 50 THEN '36-50'
        WHEN age BETWEEN 51 AND 70 THEN '51-70'
        ELSE 'Other'
    END AS age_group,

    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_revenue,
    ROUND(AVG(purchase_amount_usd), 2) AS average_purchase

FROM customer_shopping_behavior
GROUP BY age_group
ORDER BY total_revenue DESC;


-- Q4: Subscription Status Analysis

SELECT
    subscription_status,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_revenue,
    ROUND(AVG(purchase_amount_usd), 2) AS average_purchase
FROM customer_shopping_behavior
GROUP BY subscription_status
ORDER BY total_revenue DESC;


-- Q5: Payment Method Analysis

SELECT
    payment_method,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_revenue
FROM customer_shopping_behavior
GROUP BY payment_method
ORDER BY total_purchases DESC;


-- Q6: Seasonal Sales Analysis

SELECT
    season,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_revenue,
    ROUND(AVG(purchase_amount_usd), 2) AS average_purchase
FROM customer_shopping_behavior
GROUP BY season
ORDER BY total_revenue DESC;


-- Q7: Sales Analysis by Gender

SELECT
    gender,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_revenue,
    ROUND(AVG(purchase_amount_usd), 2) AS average_purchase
FROM customer_shopping_behavior
GROUP BY gender
ORDER BY total_revenue DESC;


-- Q8: Shipping Method Analysis

SELECT
    shipping_type,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_revenue
FROM customer_shopping_behavior
GROUP BY shipping_type
ORDER BY total_purchases DESC;


-- Q9: Discount Analysis

SELECT
    discount_applied,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_revenue,
    ROUND(AVG(purchase_amount_usd), 2) AS average_purchase
FROM customer_shopping_behavior
GROUP BY discount_applied
ORDER BY total_purchases DESC;


-- Q10: Purchase Frequency Analysis

SELECT
    frequency_of_purchases,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_revenue
FROM customer_shopping_behavior
GROUP BY frequency_of_purchases
ORDER BY total_purchases DESC;


-- Q11: Revenue Analysis by Location

SELECT
    location,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_revenue,
    ROUND(AVG(purchase_amount_usd), 2) AS average_purchase
FROM customer_shopping_behavior
GROUP BY location
ORDER BY total_revenue DESC
LIMIT 10;


-- Q12: Previous Purchase History Analysis

SELECT
    CASE
        WHEN previous_purchases BETWEEN 1 AND 5 THEN '1-5'
        WHEN previous_purchases BETWEEN 6 AND 10 THEN '6-10'
        WHEN previous_purchases BETWEEN 11 AND 20 THEN '11-20'
        WHEN previous_purchases > 20 THEN '21+'
        ELSE 'Other'
    END AS purchase_history_group,

    COUNT(*) AS total_purchases,
    ROUND(AVG(purchase_amount_usd), 2) AS average_purchase,
    SUM(purchase_amount_usd) AS total_revenue

FROM customer_shopping_behavior
GROUP BY purchase_history_group
ORDER BY total_revenue DESC;


-- Q13: Average Review Rating by Product Category

SELECT
    category,
    COUNT(*) AS total_reviews,
    ROUND(AVG(review_rating), 2) AS average_rating
FROM customer_shopping_behavior
GROUP BY category
ORDER BY average_rating DESC;


-- Q14: Top 10 Highest-Value Purchase Records

SELECT
    customer_id,
    age,
    category,
    item_purchased,
    purchase_amount_usd
FROM customer_shopping_behavior
ORDER BY purchase_amount_usd DESC
LIMIT 10;

-- Q15: Top 3 Most Purchased Products in Each Category

WITH product_counts AS (

    SELECT
        category,
        item_purchased,
        COUNT(*) AS total_purchases
    FROM customer_shopping_behavior
    GROUP BY category, item_purchased

),

ranked_products AS (

    SELECT
        category,
        item_purchased,
        total_purchases,

        ROW_NUMBER() OVER (
            PARTITION BY category
            ORDER BY total_purchases DESC, item_purchased ASC
        ) AS product_rank

    FROM product_counts

)

SELECT
    category,
    item_purchased,
    total_purchases,
    product_rank
FROM ranked_products
WHERE product_rank <= 3
ORDER BY category, product_rank;