-- Write SQL queries to:

-- 1- Identify and remove duplicate orders.
-- 2- Find orders where quantity is missing or zero.
-- 3- Calculate total revenue per product and category.
-- 4- List top 5 regions by revenue in the last 6 months.

-- The methodology about every detail, like what I did and why I did it, is explained in super detail in the report.

--------------------------------------------------------------------------------------------------------------------

-- 1- Identify and remove duplicate orders.

SELECT *
FROM orders;

-- It is not a good practice to make our work on the raw table so i will make a copy.

CREATE TABLE orders_staging AS
SELECT * FROM orders;


-- Checking the new copy table.

SELECT *
FROM orders_staging;

-- Because we have order_id, which is a unique identifier, it makes Identifying duplicates so easy.
-- If there were not a unique identifier, we would use window functions. (Explained in detail in the report) 

-- Here I used a sub-query in which I used MIN(order_id) to return the lowest id after grouping.
-- The main query then identifies duplicates by excluding the lower id's from the sub-query.

-- Before deleting the records, I like to take a look at them.

SELECT *
FROM orders_staging
WHERE order_id NOT IN (
    SELECT MIN(order_id)
    FROM orders_staging
    GROUP BY customer_id, product_id,order_date,quantity,price
);

-- Deleting the duplicates.

DELETE FROM orders_staging
WHERE order_id NOT IN (
    SELECT MIN(order_id)
    FROM orders_staging
    GROUP BY customer_id, product_id,order_date,quantity,price
);

-- Deleted 251 records.

--------------------------------------------------------------------------------------------------------------------

-- 2- Find orders where quantity is missing or zero.

SELECT *
FROM orders_staging
WHERE quantity = 0 OR quantity IS NULL ;

-- Removing or keeping missing values is a very cruical step

-- In real-world e-commerce datasets, quantity = 0 orders often represent:

-- Failed transactions or cancellations
-- Test entries
-- Placeholders or bugs in the system

-- I decided to keep them and exclude quantity = 0 from any calculations (explained in full detail in the report).

--------------------------------------------------------------------------------------------------------------------

-- 3- Calculate the total revenue per category.
-- I joined the order table with product table.
-- Notice that I put quantity > 0 in the where statment to EXCLUDE the 0 quantity orders.
-- Finally used group by to summrize reveune per product and order by reveune in descending order.

SELECT p.category , SUM(o.price*o.quantity) AS revenue
FROM orders_staging o
JOIN products p
USING(product_id)
WHERE quantity > 0
GROUP BY p.category
ORDER BY 2 DESC;

-- Calculate the total revenue per product. 

SELECT p.product_name , SUM(o.price*o.quantity) AS revenue
FROM orders_staging o
JOIN products p
USING(product_id)
WHERE quantity > 0
GROUP BY p.product_name
ORDER BY 2 DESC;


--------------------------------------------------------------------------------------------------------------------


-- 4- List top 5 regions by revenue in the last 6 months.

-- Identifing the first and last date. 
SELECT  MIN(order_date), MAX(order_date) 
FROM orders_staging;

-- I used sub query here to get date 30-6-2024 in order to use > and get the remaining month after that.

SELECT c.region, SUM(o.price * o.quantity) AS revenue
FROM orders_staging o
JOIN customers c
USING(customer_id)
WHERE quantity > 0 AND order_date > (
        SELECT MAX(order_date) - INTERVAL '6 months' FROM orders_staging
    )
GROUP BY c.region
ORDER BY revenue DESC
LIMIT 5;






