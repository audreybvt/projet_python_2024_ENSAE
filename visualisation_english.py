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
