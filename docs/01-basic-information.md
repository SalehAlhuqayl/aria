# Project: AI-Powered Price Prediction and Variance Analysis of Used Cars in Saudi Arabia

## Research Background

### Domain Introduction
The automotive market in Saudi Arabia is witnessing rapid growth, with a significant share coming from used car transactions. Understanding how different factors—such as brand, model, mileage, year, and location—affect car prices can provide valuable insights for consumers, dealers, and policymakers. Applying Artificial Intelligence (AI) and Machine Learning (ML) techniques can enhance market transparency and support data-driven decision-making in this evolving sector.

### Research Motivation
Despite the large used car market, pricing inconsistencies and lack of standardized valuation methods often confuse both buyers and sellers. By leveraging machine learning models, this research aims to bridge the knowledge gap and build a robust predictive framework that captures price variance across brands, regions, and other car attributes. This study contributes to developing an AI-driven pricing reference that can increase fairness and efficiency in the Saudi used car market.

## Research Objectives

### Primary Goal
To explore the used car market in Saudi Arabia and build AI-based models capable of predicting car prices and analyzing price variance across multiple attributes.

### Specific Aims
1. Perform exploratory data analysis (EDA) to uncover key patterns and correlations in the dataset.  
2. Develop and evaluate predictive models (e.g., Linear Regression, Random Forest, XGBoost) for price estimation.  
3. Investigate how different factors—brand, mileage, region, and year—contribute to price variability.  
4. Propose a machine learning framework for fair and explainable price predictions.

## Raw Data Description

### Data Source
- **Origin:** Public dataset fromش Kaggle – “Saudi Arabia Used Cars Dataset” by Turki Bin Talib  
- **Collection Method:** Aggregated from online car listing platforms  
- **Time Period:** Data collected during 2023  
- **Geographic Scope:** Kingdom of Saudi Arabia  

### Data Characteristics
- **File Format:** CSV  
- **Number of Files:** 1  
- **Total Size:** ~1.4 MB  
- **Sample Count:** Approximately 35,000 used car records  
- **Feature Count:** Around 20 columns, including car attributes and prices  

### Data Structure
- **Primary Keys:** None explicitly defined (each row represents a unique car listing)  
- **Feature Types:** Numerical (price, mileage, year), categorical (brand, model, location), and textual (description)  
- **Target Variable:** `Price`  
- **Missing Data:** Minor missing values observed in non-essential features such as “model” or “location”  

---

## Preprocessing Summary
- We cleaned the raw data and saved the results to `data/processed/`.
- Zeros in `Price` were treated as missing and removed.
- Text fields were standardized to title case.
- Out-of-range years and negative mileage were set to missing and dropped if critical.
- We added simple features: `Vehicle_Age` and `Price_per_km`.

## Processed Data Overview
- Cleaned file: `data/processed/usedcars_clean.csv`  
- Profile: `data/processed/usedcars_profile.json`  
- Rows: 5,482; Columns: 15  
- Key categories: `Make` (57), `Type` (349), `Region` (27)

Note: If the final row count is much lower than the expected ~35k, this dataset may be a subset. We can update the pipeline when the full dataset is provided.

