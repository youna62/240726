import pandas as pd

# Load the data
file_path = 'daily_temp.csv'
data = pd.read_csv(file_path)

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Extract year from the date
data['year'] = data['date'].dt.year

# Calculate yearly average, minimum, and maximum temperatures
yearly_data = data.groupby('year').agg({
    'temperature': ['mean', 'min', 'max']
}).reset_index()

# Flatten the column names
yearly_data.columns = ['year', 'average_temp', 'min_temp', 'max_temp']

yearly_data
