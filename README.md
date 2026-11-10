Nassau Candy Distributor – Product Line Profitability & Margin Performance Analysis

## Project Overview

This project analyzes the profitability and margin performance of Nassau Candy Distributor using Python and Power BI. The objective is to identify products and divisions that contribute the most to profit, detect products with low margins, and provide insights for improving pricing and product portfolio decisions.

The analysis focuses on profitability instead of only sales revenue, helping business stakeholders understand which products create the highest financial value.

---

## Business Problem

High sales do not always result in high profit. Some products generate significant revenue but contribute very little to overall profit due to high manufacturing costs or low margins.

This project answers the following questions:

- Which products generate the highest profit?
- Which products have the highest gross margin?
- Which divisions perform best financially?
- Which products have high sales but low margins?
- Which products require pricing or cost review?
- Is the company dependent on a small number of products for most of its profit?

---

## Dataset Information

The dataset contains 6,064 order records with information related to:

- Orders
- Customers
- Product Division
- Product Name
- Sales
- Cost
- Gross Profit
- Units Sold
- Shipping Details
- Region

---

## Tools & Technologies

- Python
- Pandas
- Jupyter Notebook
- Power BI
- DAX
- GitHub

---

## KPIs

- Gross Margin (%)
- Profit per Unit
- Revenue Contribution
- Profit Contribution
- Margin Volatility

---

## Project Workflow

### Data Cleaning

- Converted Order Date and Ship Date into datetime format
- Validated sales, cost, and profit values
- Removed invalid records
- Checked missing values

### Feature Engineering

Calculated:

- Gross Margin (%)
- Profit per Unit
- Revenue Contribution
- Profit Contribution
- Margin Volatility

### Product-Level Analysis

- Top products by Gross Profit
- Top products by Gross Margin
- High Sales – Low Margin products
- Low Sales – Low Profit products

### Division-Level Analysis

- Revenue by Division
- Gross Profit by Division
- Average Gross Margin by Division
- Division efficiency comparison

### Cost Structure Diagnostics

- Cost vs Sales relationship
- Cost to Sales Ratio
- Margin Risk Analysis
- Products requiring pricing review

### Profit Concentration Analysis

- Revenue contribution by product
- Profit contribution by product
- Product dependency analysis

---

## Power BI Dashboard

The dashboard consists of four pages:

### Page 1 – Executive Profitability Overview

- KPI Cards
- Revenue vs Profit by Division
- Product Profitability Matrix
- Average Gross Margin by Division

### Page 2 – Product Profitability Analysis

- Top 10 Products by Gross Profit
- Top 10 Products by Gross Margin
- Product Performance Table

### Page 3 – Cost Structure Diagnostics

- Cost vs Sales Analysis
- Cost to Sales Ratio
- Margin Risk Table

### Page 4 – Profit Concentration Analysis

- Revenue Contribution by Product
- Profit Contribution by Product
- Dependency Analysis

---

## Key Insights

- Chocolate products generate the highest overall profit.
- Some products achieve high sales but lower margins.
- Margin performance varies across product divisions.
- A limited number of products contribute a significant portion of total profit.
- Cost-to-Sales analysis highlights products that require pricing or cost optimization.

---

## Recommendations

- Review pricing strategies for low-margin products.
- Focus promotional efforts on high-margin products.
- Negotiate production costs for cost-heavy products.
- Monitor products with consistently low profitability.
- Reduce dependency on a limited number of products by improving the performance of other product lines.

---

## Project Structure
