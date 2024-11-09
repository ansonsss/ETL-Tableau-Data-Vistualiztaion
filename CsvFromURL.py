import pandas as pd


class CsvFromURL:
    def __init__(self, url):
        """
        Initialize with a URL for the CSV file and set the display options for pandas.
        """
        self.url = url
        pd.set_option('display.max_columns', None)  # Set option to display all columns

    def load_data(self):
        """
        Load data from the URL into a pandas DataFrame.
        """
        self.df = pd.read_csv(self.url)
        return self.df


# Example usage
url = "https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD"
processor = CsvFromURL(url)

# Load data
df = processor.load_data()

# Select relevant columns (outside the class)
selected_columns = [
    'DR_NO', 'DATE OCC', 'TIME OCC', 'AREA', 'AREA NAME', 'Crm Cd', 'Crm Cd Desc',
    'Vict Age', 'Vict Sex', 'Vict Descent', 'Premis Cd', 'Premis Desc', 'Weapon Used Cd',
    'Weapon Desc', 'Status', 'Status Desc', 'LOCATION', 'LAT', 'LON'
]
df_selected = df[selected_columns]

# Rename columns (outside the class)
df_renamed = df_selected.rename(columns={
    'DR_NO': 'Division Of Records Number',
    'DATE OCC': 'Date Of Crime Occurrence',
    'TIME OCC': 'Time Of Crime Occurrence',
    'AREA': 'Area',
    'AREA NAME': 'Area Name',
    'Crm Cd': 'Crime Code',
    'Crm Cd Desc': 'Crime Code Description',
    'Vict Age': 'Victim Age',
    'Vict Sex': 'Victim Sex',
    'Vict Descent': 'Victim Descent',
    'Premis Cd': 'Premise Cd',
    'Premis Desc': 'Premise Desc',
    'Weapon Used Cd': 'Weapon Used Code',
    'Weapon Desc': 'Weapon Description',
    'Status Desc': 'Status Description',
    'LOCATION': 'Location',
    'LAT': 'Latitude',
    'LON': 'Longitude'
})

# Format columns (outside the class)
# Convert 'Date Of Crime Occurrence' to 'YYYY-MM-DD' format
df_renamed['Date Of Crime Occurrence'] = pd.to_datetime(
    df_renamed['Date Of Crime Occurrence'],
    format='%m/%d/%Y %I:%M:%S %p'
).dt.strftime('%Y-%m-%d')

# Convert 'Time Of Crime Occurrence' to 'HH:MM:SS' format
df_renamed['Time Of Crime Occurrence'] = df_renamed['Time Of Crime Occurrence'].apply(
    lambda x: f"{str(x).zfill(4)[:2]}:{str(x).zfill(4)[2:]}:00"
)

# Filter data between 2020-01-01 and 2023-12-31
df_filtered = df_renamed[
    (df_renamed['Date Of Crime Occurrence'] >= '2020-01-01') &
    (df_renamed['Date Of Crime Occurrence'] <= '2023-12-31')
]

# Save the filtered data to a new CSV file
df_filtered.to_csv("LA Crime 2020-2023.csv", index=False)

print("Filtered data saved to 'LA Crime 2020-2023.csv'")
