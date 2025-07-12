# 🏠 Airbnb Listings Analysis Using Python

---

## 📘 Table of Contents

1. Introduction
2. About Airbnb Data
3. Project Objective
4. Dataset Overview
5. Tools & Libraries Used
6. Environment Setup
7. Step-by-Step Analysis

   * Data Loading
   * Data Exploration
   * Data Cleaning
   * Summary Statistics
   * Key Business Insights
   * Data Filtering
   * Export Processed Data
8. Possible Visualizations
9. Use Cases & Business Impact
10. Conclusion
11. Future Improvements
12. Resume Line Example
13. GitHub Repo Structure
14. Contact Info

---

## 1. 🧽 Introduction

The travel and tourism industry has transformed immensely over the last decade. Platforms like Airbnb have made it easier for travelers to find affordable, diverse, and personalized lodging experiences globally. For hosts, it has opened new income opportunities.

However, as Airbnb listings grow, so does the complexity in understanding trends — from pricing to customer satisfaction. That’s where data analysis plays a key role. With Python, Pandas, and NumPy, we can analyze large volumes of Airbnb data to uncover patterns that can guide decisions for both businesses and users.

This project offers a beginner-friendly yet professional-level analysis of mock Airbnb data using industry-relevant tools.

---

## 2. 🏨 About Airbnb Data

Airbnb provides a wide array of listing features such as pricing, number of reviews, review scores, availability, and more. Each of these metrics offers insights into host performance, demand trends, and customer behavior.

In this analysis, we simulate a real-world dataset to understand how to extract insights that would otherwise be hidden in raw data.

---

## 3. 🎯 Project Objective

The main objectives of this project are:

* Explore the dataset to understand its structure
* Perform statistical analysis using Pandas and NumPy
* Identify trends in pricing and reviews
* Highlight top-performing hosts and locations
* Export processed data for potential use in dashboards

---

## 4. 🗃️ Dataset Overview

The dataset used (`airbnb_listings.csv`) includes the following columns:

| Column Name         | Description                                 |
| ------------------- | ------------------------------------------- |
| Listing\_ID         | Unique ID of each listing                   |
| Host\_Name          | Host's name                                 |
| Price\_per\_Night   | Price per night in USD                      |
| Location            | City of the listing                         |
| Number\_of\_Reviews | Total number of user reviews                |
| Review\_Score       | Average rating score (1 to 5)               |
| Minimum\_Nights     | Minimum number of nights for a booking      |
| Availability\_365   | Number of days available for rent in a year |

---

## 5. 🔧 Tools & Libraries Used

| Tool/Library    | Purpose                          |
| --------------- | -------------------------------- |
| Python          | Programming language             |
| Pandas          | Data manipulation                |
| NumPy           | Numerical operations             |
| Jupyter/VS Code | IDE for writing and running code |

---

## 6. ⚙️ Environment Setup

To run this project on your system:

```bash
pip install pandas numpy
```

Or use Google Colab or Jupyter Notebook for an interactive experience.

---

## 7. 🔍 Step-by-Step Analysis

### a. 📥 Data Loading

```python
import pandas as pd
df = pd.read_csv("airbnb_listings.csv")
```

### b. 👁️ Data Exploration

```python
df.head()
df.info()
df.describe()
```

We review the first few rows and check data types and summary statistics.

### c. 🧹 Data Cleaning

```python
df.dropna(inplace=True)
```

This ensures we remove any rows with missing values, ensuring clean analysis.

### d. 📊 Summary Statistics

```python
import numpy as np
average_price = np.mean(df["Price_per_Night"])
average_review_score = np.mean(df["Review_Score"])
```

These figures give us a macro understanding of affordability and satisfaction.

### e. 🧐 Key Business Insights

```python
df[df["Review_Score"] == df["Review_Score"].max()]
```

Identify high-performing hosts and their listing locations.

### f. 🧼 Data Filtering

```python
premium = df[(df["Price_per_Night"] > 100) & (df["Availability_365"] > 200)]
```

Find premium listings based on price and availability.

### g. 💾 Export Processed Data

```python
df.to_csv("processed_airbnb_listings.csv", index=False)
```

---

## 8. 📈 Possible Visualizations (Suggested)

While this is a code-only project, the data can be visualized using:

* **Bar Chart**: Listings by City
* **Boxplot**: Price distribution
* **Histogram**: Review score distribution
* **Line Chart**: Price trends over time (if date is added)

---

## 9. 💼 Use Cases & Business Impact

### Hosts:

* Set competitive pricing
* Improve reviews based on analytics

### Airbnb:

* Detect top markets
* Recommend better host practices

### Tourists:

* Choose best-rated, most available listings

---

## 10. 📏 Conclusion

This project showcases how beginner data analysts can use Python, Pandas, and NumPy to extract valuable insights from a flat dataset. It simulates real-world Airbnb use cases, covering end-to-end workflow from loading to exporting.

---

## 11. 🔮 Future Improvements

* Add time-based data (e.g., date of reviews)
* Implement advanced NLP for text reviews
* Create dashboards using Plotly or Tableau
* Connect with real Airbnb open data

---

## 12. 💼 Resume Line Example

> Analyzed Airbnb listings using Python (Pandas, NumPy), calculated average prices/reviews, filtered high-performing listings, and exported results for visualization.

---

## 13. 📂 GitHub Repo Structure

```
airbnb-listings-analysis/
├── airbnb_listings.csv
├── airbnb_analysis.py
├── processed_airbnb_listings.csv
└── README.md
```

---

## 14. 📬 Contact Info

**Author**: Kritika Mishra
**GitHub**: [@Kritikamishraa]https://github.com/Kritikamishraa/airbnb-listings-analysis
**Email**: [kritikamishraa12@gmail.com](mailto:kritikamishraa12@gmail.com)

---

Thank you for checking out this project! Feel free to fork, improve, or connect with me on GitHub!
