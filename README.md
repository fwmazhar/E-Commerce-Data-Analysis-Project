# 📦 E-Commerce Data Analysis Project

**May 2025**  
**By:** Omar Ahmed Mazhar

---

## 🧠 Project Overview

This project simulates a real-world data analytics scenario in an e-commerce context. It walks through the full data lifecycle—from **data generation** using Python, **data cleaning** with SQL, to **exploratory data analysis (EDA)** and **interactive dashboarding using Microsoft Power BI**.

The goal is to derive actionable insights for decision-makers from a custom-built dataset of customer, product, and order information.

---

## 🔧 Tools & Technologies Used

- 🐍 **Python** — For synthetic data generation
- 🐘 **PostgreSQL** (via **pgAdmin**) — For data storage and SQL-based cleaning
- 📊 **Microsoft Power BI** — For data visualization and KPI tracking

---

## 📁 Dataset Description

The project consists of three main CSV files:

1. **`customers.csv`**
   - 500 customers
   - 10 global regions
   - Signup dates in 2023

2. **`products.csv`**
   - 30 products
   - 6 common e-commerce categories
   - Price data (assumed as cost)

3. **`orders.csv`**
   - 5,000+ orders in 2024
   - 5% duplicates (to mimic real-world errors)
   - 5% orders with `quantity = 0` to simulate cancellations

---

## 🧹 SQL Data Cleaning

The raw data was cleaned using SQL scripts. Key operations included:

- ✅ Removing duplicate orders using window functions
- ❌ Filtering out invalid orders with `quantity = 0`
- 💰 Calculating total revenue per product and category
- 🌍 Identifying top-performing regions over the past 6 months

All queries were executed on a local PostgreSQL database using pgAdmin.

---

## 📊 Exploratory Data Analysis (Power BI)

The cleaned data was analyzed using Power BI, focusing on:

- **Revenue Trends by Month**
- **Performance by Product Category and Region**
- **Customer Signup-to-Order Delay**

> 📌 *Average time from signup to first order: ~189.52 days*  
> 📌 *Books and Beauty were the lowest-performing categories*

---

## 📈 Dashboard Highlights

Key dashboard metrics:

- 💵 **Total Revenue**: $763,000  
- 📦 **Total Orders**: 4,999  
- 🧾 **Average Order Value**: $152.64  
- ❌ **Cancelled Orders**: 250  

Interactive visualizations help stakeholders explore trends by **region**, **category**, and **time**. France emerged as the top-performing region, while Home & Kitchen was the most profitable category.

---

## 💡 Bonus Metric – CLTV (Customer Lifetime Value)

A metric was proposed to estimate long-term customer value:

```text
CLTV = Avg. Order Value × Purchase Frequency × Customer Lifespan
