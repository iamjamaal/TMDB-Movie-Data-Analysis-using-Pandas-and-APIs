
          TMDB Movie Data Analysis using Pandas and APIs

A comprehensive data analysis project examining the financial performance, audience reception, and industry trends of major blockbuster films using the TMDB API and Python's Pandas library.

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.1.4-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)



               Project Overview

This project implements a complete ETL (Extract, Transform, Load) pipeline to analyze movie industry data, delivering insights into what makes blockbuster films successful. The analysis covers 18 major films spanning 1997-2019, examining financial performance, audience metrics, and franchise dynamics.


               Key Highlights:
-18 blockbuster films analyzed with combined revenue of $30.45 billion
- 717% average ROI across all movies
- 100% profitability rate in dataset
- 6 professional visualizations with publication-quality graphics
- Advanced KPI analysis with custom ranking algorithms



              Project Objectives

1. API Data Extraction: Fetch comprehensive movie data from TMDB API
2. Data Cleaning & Transformation: Process and structure raw API responses
3. Exploratory Data Analysis: Understand industry trends and patterns
4. Advanced Filtering & Ranking: Identify best/worst performers by multiple metrics
5. Franchise & Director Analysis: Compare franchise vs. standalone performance
6. Visualization & Insights: Present findings through professional charts




                Project Structure

TMDB-Movie-Data-Analysis-using-Pandas-and-APIs/
│
├── config.py # API configuration and movie IDs
├── .env # Environment variables (API key)
├── .env.example # Template for environment setup
├── requirements.txt # Python dependencies
├── README.md # Project documentation (this file)
│
├── data/
│ ├── raw/
│ │ └── movies_raw.json # Raw API responses (18 movies)
│ └── final/
│ └── movies_with_kpis.csv # Cleaned dataset with engineered features
│
├── notebooks/
│ ├── 01_data_extraction.ipynb # API data fetching and storage
│ ├── 02_data_cleaning.ipynb # Data preprocessing and feature engineering
│ ├── 03_kpi_analysis.ipynb # KPI calculations and rankings
│ └── 04_visualization.ipynb # Data visualizations and insights
│
└── reports/
├── kpi_summary.txt # High-level KPI summary
├── kpi_detailed_results.txt # Detailed analysis results
├── final_report.md # Comprehensive final report
└── figures/
├── revenue_vs_budget.png
├── roi_by_genre.png
├── popularity_vs_rating.png
├── yearly_trends.png
├── franchise_vs_standalone.png
└── genre_distribution.png






              Quick Start

Prerequisites
- Python 3.8+ (developed on 3.13)
- TMDB API key ([Get one here](https://www.themoviedb.org/settings/api))
- Git (for cloning repository)


Installation

1. Clone the repository
   git clone https://github.com/iamjamaal/TMDB-Movie-Data-Analysis-using-Pandas-and-APIs.git
   cd TMDB-Movie-Data-Analysis-using-Pandas-and-APIs


2. Create virtual environment 
python -m venv venv

Windows
venv\Scripts\activate

 macOS/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure API creditials
 - Copy the example environment file
    cp .env.example .env

-  Edit .env and add your TMDB API key
-  TMDB_API_KEY=your_api_key_here


5. Run the analysis
Execute notebooks in order
   - jupyter notebook notebooks/01_data_extraction.ipynb
   -  Then proceed through 02, 03, 04 sequentially
   


              Documentation

Detailed Reports
- [Final Report](reports/final_report.md) - Comprehensive analysis with methodology, findings, and recommendations
- [KPI Summary](reports/kpi_summary.txt) - High-level metrics overview
- [Detailed Results](reports/kpi_detailed_results.txt) - Full ranking tables


Code Documentation
Each notebook contains:
- Markdown explanations for each section
- Inline comments for complex operations
- Function docstrings with parameter descriptions
- Output interpretations





