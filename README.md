**Task 1**: Data Cleaning and Preprocessing

**Objective**
The objective of this project is to clean and preprocess a raw dataset using Python and Pandas. The dataset was cleaned by handling missing values, removing duplicate records, standardizing text values, formatting dates, and verifying data types.

**Dataset**
- **Dataset Name:** Netflix Movies and TV Shows
- **Source:** Kaggle

**Tools Used**
- Python
- Pandas
- Visual Studio Code (VS Code)
  
**Data Cleaning Steps**
1. Loaded the dataset using Pandas.
2. Displayed the first few rows of the dataset.
3. Checked dataset information using `info()`.
4. Identified missing values using `isnull().sum()`.
5. Filled missing values in the following columns:
   - `country` → "Unknown"
   - `director` → "Not Available"
   - `cast` → "Not Available"
   - `rating` → Most frequent value (mode)
   - `duration` → Most frequent value (mode)
6. Removed duplicate rows using `drop_duplicates()`.
7. Renamed column headers to lowercase and replaced spaces with underscores.
8. Standardized text values by removing extra spaces and converting country names to title case.
9. Converted the `date_added` column to a consistent `dd-mm-yyyy` format.
10. Checked and verified data types.
11. Saved the cleaned dataset as `cleaned_netflix_titles.csv`.

**Files Included**
- `netflix_titles.csv` – Original dataset
- `cleaned_netflix_titles.csv` – Cleaned dataset
- `data_cleaning.py` – Python script used for cleaning
- `README.md` – Project documentation

**Output**
The cleaned dataset is free from duplicate records, has standardized text formatting, consistent date formatting, and is ready for further data analysis or visualization.

**Learning Outcomes**
- Learned how to identify and handle missing values.
- Removed duplicate records from a dataset.
- Standardized text and column names.
- Converted date formats using Pandas.
- Improved understanding of data preprocessing techniques.
- Prepared a clean dataset for analysis.

## Author
**Name:** Durga
