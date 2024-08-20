# Looker Sales Dashboard

This repository contains the necessary files and scripts to build a sales dashboard in Looker Studio, structured using a star schema.

## Repository Structure
```
.
├── data/
│   ├── raw_sales_data.csv               # Original raw sales data
│   ├── processed_sales_data_cleaned.csv # Cleaned and processed sales data
│   ├── dim_date.csv                     # Date Dimension Table
│   ├── dim_product.csv                  # Product Dimension Table
│   ├── dim_region.csv                   # Region Dimension Table
│   └── fact_sales.csv                   # Fact Table containing sales metrics
│
├── scripts/
│   ├── data_cleaning.py                 # Python script for data cleaning and enhancement
│   ├── create_star_schema.py            # Python script to create star schema tables
│   └── requirements.txt                 # List of required Python packages
│
└── README.md                            # Instructions and details about the project
```

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone <repository_url>
cd looker-sales-dashboard
```

### 2. Install Dependencies

Install the required Python packages using pip:
```bash
pip install -r scripts/requirements.txt
```

###  3. Run Data Cleaning Script
Run the data cleaning script to process the raw sales data:
```bash
python scripts/data_cleaning.py
```

### 4. Create Star Schema Tables
Run the script to create the star schema tables:
```bash
python scripts/create_star_schema.py
```

This will generate the following files in the data/ directory:

	•	dim_date.csv
	•	dim_product.csv
	•	dim_region.csv
	•	fact_sales.csv

5. Upload to Looker Studio