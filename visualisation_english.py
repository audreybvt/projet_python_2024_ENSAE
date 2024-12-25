import xarray as xr

###################### VISUALIZE COPERNICUS DATA ####################

# Path to the NetCDF file
file_path = "data/data_SST.nc"

# Load the NetCDF file
data = xr.open_dataset(file_path)

# Explore the data
print(data)  # Summary of dimensions, variables, and attributes
print(data.variables)  # List of available variables

# Access a specific variable
print(data['tos'])  # Replace with an actual variable

# Extract the data from a variable as a NumPy array
variable_data = data['tos'].values

# Close the file to release resources
data.close()

import matplotlib
import matplotlib.pyplot as plt
import xarray as xr

# Assuming 'ds' is your xarray Dataset and 'tos' is the variable
# Extract the 'tos' data variable
tos = data['tos']

# Select data for a specific grid point, e.g., i=0 and j=0
tos_at_point = tos.sel(i=0, j=0, method='nearest')

# Plotting sea surface temperature through time
plt.figure(figsize=(10, 6))
tos_at_point.plot()
plt.title('Sea Surface Temperature Over Time (Grid Point: i=0, j=0)')
plt.xlabel('Time')
plt.ylabel('Sea Surface Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
# Save the plot to a file (e.g., PNG)
plt.savefig('output/sst_time_series.png', dpi=300)

plt.show()

######################### VISUALIZE DIFFERENT SCENARIOS #############################

import xarray as xr
import matplotlib.pyplot as plt

# Paths to the NetCDF files
file_paths = [
    "data/tos_Omon_HadGEM3-GC31-LL_ssp126_r1i1p1f3_gn_20150116-20491216.nc",  # Scenario 1
    "data/tos_Omon_HadGEM3-GC31-LL_ssp245_r1i1p1f3_gn_20150116-20491216.nc",  # Scenario 2
    "data/tos_Omon_HadGEM3-GC31-LL_ssp585_r1i1p1f3_gn_20150116-20491216.nc"   # Scenario 3
]

# Names of the scenarios for the legend
scenario_names = ["SSP1-2.6", "SSP2-4.5", "SSP5-8.5"]

# Initialize the plot
plt.figure(figsize=(12, 8))

# Loop through the files and add them to the plot
for i, file_path in enumerate(file_paths):
    # Load the NetCDF file
    data = xr.open_dataset(file_path)
    
    # Extract the sea surface temperature (tos) data
    tos = data['tos']
    
    # Select a specific grid point (e.g., i=0, j=0)
    tos_at_point = tos.sel(i=0, j=0, method='nearest')
    
    # Add the data to the plot
    plt.plot(
        tos_at_point['time'],  # X-axis: time
        tos_at_point,          # Y-axis: sea surface temperature
        label=scenario_names[i]  # Legend based on the scenario
    )
    
    # Close the NetCDF file to release resources
    data.close()

# Customize the plot
plt.title('Evolution of Sea Surface Temperature for Different Scenarios')
plt.xlabel('Time')
plt.ylabel('Sea Surface Temperature (°C)')
plt.legend(title="Scenarios", loc='upper left')  # Display the legend
plt.grid(True)
plt.xticks(rotation=45)  # Rotate the x-axis labels
plt.tight_layout()

# Save the plot
plt.savefig('output/sst_scenarios_comparison.png', dpi=300)

# Display the plot
plt.show()


####################@ VISUALIZE PUFFIN DATA #################

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data (puffin production rate)
puffins = pd.read_csv("data/puffin-data1_Data.csv")

# Rename the 'Year' column to 'time' to match the temperature column
puffins.rename(columns={"Year": "time", "Prod": "production_rate"}, inplace=True)

# Check the data types
print("Data types in puffins:\n", puffins.dtypes)

# Visualize the puffin production rate over the years
plt.figure(figsize=(10, 6))
plt.plot(puffins['time'], puffins['production_rate'], marker='o', linestyle='-', color='blue', label='Production Rate')
plt.title("Puffin Production Rate Over Years")
plt.xlabel("Year")
plt.ylabel("Production Rate")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the plot (if needed)
plt.savefig('output/puffin_rate_over_years.png', dpi=300)

# Display the plot
plt.show()

##########################@@ VISUALIZE PUFFIN AND TEMPERATURE ###################
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

# Load NetCDF data (temperatures)
nc_file = "output/annual_mean_SST.nc"
data = xr.open_dataset(nc_file)

# Calculate the annual mean of temperatures
temperature = data['tos'].resample(time="1Y").mean().to_dataframe()
temperature.reset_index(inplace=True)

# Convert 'time' to full years
temperature['time'] = temperature['time'].astype(str)  # Convert cftime to string
temperature['time'] = pd.to_datetime(temperature['time'])  # Convert to datetime
temperature['time'] = temperature['time'].dt.year.astype('int64')  # Extract year as integer

# Load CSV data (puffin production rates)
puffins = pd.read_csv("data/puffin-data1_Data.csv")

# Rename the 'Year' column to 'time' to match the temperature column
puffins.rename(columns={"Year": "time", "Prod": "production_rate"}, inplace=True)

# Merge data on the 'time' column (inner join)
merged_data = pd.merge(temperature, puffins[['time', 'production_rate']], on="time", how="inner")

# Visualize temperature and production rate over the years
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot temperature on Y-axis 1
ax1.set_xlabel("Year")
ax1.set_ylabel("Sea Surface Temperature (°C)", color="tab:blue")
ax1.plot(merged_data['time'], merged_data['tos'], color="tab:blue", label="Temperature")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# Add a second Y-axis for the puffin production rate
ax2 = ax1.twinx()  # Share the X-axis
ax2.set_ylabel("Puffin Production Rate", color="tab:green")
ax2.plot(merged_data['time'], merged_data['production_rate'], color="tab:green", label="Puffin Production", linestyle="--")
ax2.tick_params(axis="y", labelcolor="tab:green")

# Add a title and customize the plot
fig.suptitle("Temperature and Puffin Production Rate Over the Years", fontsize=14)
ax1.grid(True, linestyle="--", alpha=0.5)
fig.tight_layout()

# Save the plot (if necessary)
plt.savefig("output/temperature_puffin_rate_over_years.png", dpi=300)

# Display the plot
plt.show()
