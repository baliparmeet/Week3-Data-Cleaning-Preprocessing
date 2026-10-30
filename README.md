
# Week 3 – Data Cleaning and Preprocessing Pipeline

## Project Overview

This project focuses on developing a data cleaning and preprocessing pipeline using a Sephora customer reviews dataset. It is part of my Data Science internship task in the Beauty and Wellness domain.

The objective is to improve data quality and prepare the dataset for further analysis.

## Objectives

- Inspect the dataset and understand its structure.
- Identify and handle missing values.
- Detect and remove repeated review records.
- Validate ratings and feedback counts.
- Clean and standardize review text.
- Identify potential price outliers.
- Save the cleaned dataset for future analysis.

## Tools and Technologies

- Python
- Pandas
- NumPy (supporting numerical-computing library)
- VS Code
- Excel

## Dataset Information

The original dataset contains customer reviews, product information, ratings, recommendation status, feedback counts and customer attributes.

After preprocessing, the final dataset contains:

- **Rows:** 49,972
- **Columns:** 21
- **Text-analysis records:** 49,912

## Preprocessing Steps

1. Dataset inspection and removal of an unnecessary index column.
2. Identification and removal of repeated review combinations.
3. Missing-value analysis and appropriate handling.
4. Validation of ratings and feedback counts.
5. Review-text whitespace cleaning.
6. Cautious correction of common text-encoding issues.
7. Price outlier detection using the IQR method.
8. Saving the final cleaned datasets.

## Key Results

- Removed 5 excess records from repeated review combinations.
- Found no invalid ratings.
- Found no negative feedback counts.
- Found no inconsistent feedback totals.
- Identified 4,738 potential price outliers (9.48%).
- Preserved missing values where appropriate.
- Prepared a separate dataset for text analysis.

## Project Files

- `week3.py` – Python preprocessing code.
- `Week3_Professional_Project_Report.docx` – Detailed project report.
- `sephora_reviews_cleaned.csv` – Final cleaned dataset.
- `sephora_reviews_cleaned.xlsx` – Excel version of the cleaned dataset.
- `sephora_text_analysis.csv` – Dataset prepared for text analysis.

## Conclusion

This project helped me understand the importance of data quality before performing data analysis. It provided practical experience in identifying data issues, applying preprocessing techniques and preparing structured datasets for further analysis.

## Internship Task

**Week 3: Data Cleaning and Preprocessing Pipeline Development**

Domain: Beauty and Wellness
