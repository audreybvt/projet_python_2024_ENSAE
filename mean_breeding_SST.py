import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

# Path to the NetCDF file
file_path = "/home/onyxia/projet_python_2024_ENSAE/data/data_SST.nc"

# Load the NetCDF file
data = xr.open_dataset(file_path)

# Print the structure of the data to verify the variables and dimensions
print(data)

# Assume the variable for temperature is 'tos'
tos = data['tos']

# Convert 'time' from cftime to pandas datetime (handling 360-day calendar)
data['time'] = [pd.to_datetime(t) for t in data['time'].values]

# Shift the 'time' by 8 months to match the period from September t-1 to August t
data['shifted_time'] = data['time'] - pd.DateOffset(months=8)

# Group by the adjusted time (shifted year) and calculate the annual mean SST
tos_annual_mean = tos.groupby(data['shifted_time'].dt.year).mean()

# Plot the time series of the annual mean SST at grid point (i=0, j=0)
plt.figure(figsize=(10, 6))
tos_annual_mean.sel(i=0, j=0, method='nearest').plot()
plt.title('Annual Mean Sea Surface Temperature Over Time (Grid Point: i=0, j=0)')
plt.xlabel('Time')
plt.ylabel('Annual Mean Sea Surface Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('/home/onyxia/projet_python_2024_ENSAE/output/annual_breading_sst_time_series.png', dpi=300)

plt.show()

# Save the annual mean SST data into a new NetCDF file
output_path = "/home/onyxia/projet_python_2024_ENSAE/output/annual_mean_breading_SST.nc"
tos_annual_mean.to_netcdf(output_path)

print(f"NetCDF file with annual mean SST saved: {output_path}")
