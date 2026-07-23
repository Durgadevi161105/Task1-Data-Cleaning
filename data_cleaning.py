import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print("Original Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

df = df.drop_duplicates()

df["country"] = df["country"].fillna("Unknown")

df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

df["duration"] = df["duration"].fillna(df["duration"].mode()[0])

df["director"] = df["director"].fillna("Not Available")
df["cast"] = df["cast"].fillna("Not Available")

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

df["country"] = df["country"].str.strip().str.title()
df["director"] = df["director"].str.strip()
df["cast"] = df["cast"].str.strip()

df["date_added"] = df["date_added"].fillna("Unknown")

mask = df["date_added"] != "Unknown"

df.loc[mask, "date_added"] = (
    pd.to_datetime(
        df.loc[mask, "date_added"].str.strip(),
        format="mixed",
        errors="coerce"
    ).dt.strftime("%d-%m-%Y")
)

print("\nData Types:")
print(df.dtypes)

# Convert release_year to integer
df["release_year"] = df["release_year"].astype(int)

print("\nRemaining Missing Values:")
print(df.isnull().sum())

df.to_csv("cleaned_netflix_titles.csv", index=False)

print("\n✅ Cleaning Completed Successfully!")
print("Cleaned dataset saved as 'cleaned_netflix_titles.csv'")