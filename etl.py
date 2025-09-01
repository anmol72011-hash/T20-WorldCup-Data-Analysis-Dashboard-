# scripts/etl.py
import pandas as pd

def load_data(file_path):
    """Load raw data."""
    return pd.read_csv(C:/Users/anmol/Documents/t20wc/ICC Mens T20 Worldcup.csv)

def clean_data(df):
    """Clean and preprocess the data."""
    df['Date'] = pd.to_datetime(df['Date'])  # Convert date column
    df['Year'] = df['Date'].dt.year  # Add a 'Year' column
    df.dropna(inplace=True)  # Drop rows with missing values
    return df

def save_data(df, file_path):
    """Save processed data."""
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    raw_data_path = "../data/raw_data.csv"
    processed_data_path = "../data/processed_data.csv"

    raw_data = load_data(raw_data_path)
    processed_data = clean_data(raw_data)
    save_data(processed_data, processed_data_path)