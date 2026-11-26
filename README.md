# 🛒 E-Commerce Sales Data Engineering Pipeline

## 📌 Project Overview

This project implements an end-to-end E-Commerce Sales Data Engineering Pipeline using **Databricks and PySpark**, following the **Medallion Architecture (Bronze, Silver, and Gold)**.

The pipeline processes raw e-commerce sales data, performs data cleaning and transformation, applies data quality checks, and generates business-ready analytical datasets for reporting and visualization.

## 🛠️ Technologies Used

- **Databricks** – Cloud Data Engineering Platform
- **Python** – Programming Language
- **PySpark** – Data Processing and Transformation
- **Delta Lake** – Reliable Data Storage
- **Unity Catalog** – Data Governance and Management
- **Medallion Architecture** – Bronze, Silver, and Gold Layers
- **Databricks AI/BI Dashboards** – Data Visualization

## 🏗️ Project Architecture

The project follows the Medallion Architecture.

### 🥉 Bronze Layer – Raw Data Ingestion

- Ingested raw e-commerce sales data into Databricks.
- Used PySpark for data ingestion.
- Stored raw data in Delta format.
- Maintained source data for downstream processing.

### 🥈 Silver Layer – Data Cleaning and Transformation

- Handled missing and null values.
- Removed duplicate records.
- Performed data type corrections.
- Applied data validation and quality checks.
- Transformed raw data into clean, structured datasets.

### 🥇 Gold Layer – Business-Level Aggregation

- Created business-ready analytical datasets using PySpark.
- Performed aggregations and calculations.
- Generated category-wise sales analysis.
- Prepared datasets for business reporting and dashboards.

## 📊 Dashboard & Visualization

Created interactive dashboards using Databricks AI/BI Dashboards to analyze:

- Overall Sales Performance
- Category-wise Sales Analysis
- Product Performance
- Business KPIs

## 📁 Project Structure

```text
Ecommerce-Sales-Data-Engineering-Pipeline/
│
├── README.md
│
├── notebooks/
│   ├── Bronze/
│   ├── Silver/
│   └── Gold/
│
├── screenshots/
│
├── documentation/
│
└── pipeline/
```

## 🎯 Key Learning Outcomes

- Hands-on experience with Databricks.
- Implemented PySpark DataFrame transformations.
- Understood Medallion Architecture.
- Worked with Delta Lake.
- Implemented data cleaning and quality checks.
- Built business-ready datasets.
- Developed interactive AI/BI dashboards.

## 👨‍💻 Author

**Bala Siva Manikanta**

Aspiring Data Engineer | PySpark | Python | Databricks | Data Analytics
