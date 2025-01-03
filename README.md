# Projet Python for Data Science: Predicting Atlantic Puffin Population

### Authors: Audrey BOVET and Eve SAMANI

## Table of Contents

1.  [Subject](#subject)
2.  [Motivations](#motivations)
3.  [Data Used](#data-used)
4.  [Repository Structure](#repository-structure)
5.  [Requirements and Installation](#requirements-and-installation)
6.  [Usage](#usage)
7.  [Results](#results)
8.  [License](#license)

------------------------------------------------------------------------

## Subject <a name="subject"></a> 

This project aims to **predict the evolution of the Atlantic puffin population in time and space** under various global warming scenarios, using CMIP6 climate projections and historical puffin production data.

![Atlantic Puffin](https://islande24.fr/wp-content/uploads/2018/11/shutterstock_403375483.jpg)

------------------------------------------------------------------------

## Motivations <a name="motivations"></a>

The Atlantic puffin (*Fratercula arctica*) is a small seabird from the North Atlantic Ocean that has faced significant challenges due to climate change. Rising **sea surface temperatures (SST)** affect food availability during breeding seasons, leading to population declines.

Given that puffins are classified as **vulnerable** (IUCN RedList), this project seeks to model their population trends based on historical data and predict their evolution under these CMIP6 scenarios:
- SSP 5.8-5 (most pessimistic)
- SSP 2.4-5 (intermediate)
- SSP 1.2-6 (most optimistic)

------------------------------------------------------------------------

## Data Used <a name="data-used"></a>

-   [**CMIP6 Climate Projections**](https://cds.climate.copernicus.eu/datasets/projections-cmip6?tab=overview)
    Includes historical and predictive sea surface temperature (SST) data.
-   [**Atlantic Puffin Chick Production Data**](https://onlinelibrary.wiley.com/doi/10.1111/gcb.15665)
    Sourced from [Global Change Biology, Hansen et al. (2021)](https://onlinelibrary.wiley.com/doi/10.1111/gcb.15665).
-   [**BirdLife DataZone**](https://datazone.birdlife.org/species/requestdis)
    Species distribution data request. 

### 1. [**CMIP6 Climate Projections**](https://cds.climate.copernicus.eu/datasets/projections-cmip6?tab=overview)
- **Type of Data**: Climate model projections and historical data.
- **File Format**: NetCDF.
- **Content**:
  - The CMIP6 dataset provides global climate projections, including historical and predictive data.
  - **Key Variable Used**: Sea Surface Temperature (TOS).
  - The dataset includes projections for various climate scenarios (RCPs), models, and variables, focusing on SST trends.
  - **Years Covered**: 
    - Historical data: 1850 to present.
    - Future projections: Up to 2049.
  - This data helps to understand how sea surface temperature trends might affect marine ecosystems and coastal bird populations over time.

### 2. [**Atlantic Puffin Chick Production Data**](https://onlinelibrary.wiley.com/doi/10.1111/gcb.15665)
- **Type of Data**: Long-term biological data.
- **File Format**: CSV (available via request or publication supplement).
- **Content**:
  - The dataset contains records of Atlantic Puffin chick production, sourced from the study "Centennial relationships between ocean temperature and Atlantic puffin production" (Hansen et al., 2021).
  - It includes relationships between **ocean temperature** and **Atlantic Puffin chick production** over time.
  - **Years Covered**: 
    - Data spans from the **early 1900s** to the **present**.

### 3. [**BirdLife DataZone**](https://datazone.birdlife.org/species/requestdis)
- **Type of Data**: Species distribution data.
- **File Format**: CSV, Excel (available via request).
- **Content**:
  - BirdLife International’s DataZone provides species distribution maps and detailed data on a wide range of bird species worldwide.
  - **Key Variables**: Species name, geographic distribution, population size, and habitat.
  - This dataset is useful for understanding the current global distribution of birds and the effects of climate change on species ranges.
  - **Years Covered**:
    - Data reflects **current species distribution** and **conservation status**.
    - Timeframe: The dataset provides up-to-date information on species' habitats and populations.


------------------------------------------------------------------------

## Repository Structure <a name="repository-structure"></a>

Here is the repository layout:

```         
📂 data  
 # this folder is not supposed to be there before running the main notebook but we let it there in case there are any issues with connecting to the minio Client
📂 results  
  # this folder is not supposed to be there before running the main notebook but we let it there in case there are any issues with connecting to the minio Client

.gitignore                         # Files excluded from Git tracking  
get_data.ipynb                     # Notebook for downloading data SHOULD NOT BE RUN 
main.ipynb                         # Main analysis script
README.md                          # Project documentation  
requirements.txt                   # Dependencies and required libraries  
```

------------------------------------------------------------------------

## Requirements and Installation <a name="requirements-and-installation"></a>

### Prerequisites:

Ensure you have Python 3.8+ installed.

### Install Required Libraries:

``` bash
pip install -r requirements.txt
```

### Required Python Packages:

-   `xarray`
-   `numpy`
-   `pandas`
-   `matplotlib`
-   `scipy`
-   `netCDF4`
-   `folium`

------------------------------------------------------------------------

## Usage <a name="usage"></a>

### Step 1: Clone the Repository

``` bash
git clone https://github.com/audreybvt/projet_python_2024_ENSAE.git
cd projet_python_2024_ENSAE
```

### Step 2: Main Analysis

Run `main.ipynb` to perform the analysis, train models, and visualize results.

#### N.B.: Data preparation notebook

You don't need to open and execute `get_data.ipynb` to download and process the data as everything has been put on the sspcloud and is called in `main.ipynb`. However you can have a look at `get_data.ipynb` if you want to know how we got the data.

### Step 3: View Results

Interactive maps and visualizations are stored in the `results/` folder and can be opened in a web browser.

------------------------------------------------------------------------

## Results <a name="results"></a>

Key outputs of the project include:
1. **Interactive Map of Puffin Distribution:**
Viewable in `results/puffin_distribution_map.html`.
2. **Comparison of Climate Scenarios:**
`results/tos_comparison_scenarios.html` compares different climate trajectories.
3. **Historical Trends:**
`results/tos_graphic_historical.html` shows past trends in SST.
4. **Population Predictions:**
Graphical predictions of puffin populations under various climate scenarios.

------------------------------------------------------------------------

## **7. License** <a name="license"></a>

This repository is licensed under the MIT License. You are free to use, modify, and distribute the code and data in this repository, provided proper credit is given to the authors.

------------------------------------------------------------------------

## **References**

-   Hansen, E.S., et al. (2021). *Centennial relationships between ocean temperature and Atlantic puffin production reveal shifting decennial trends*. Global Change Biology. DOI: [10.1111/gcb.15665](https://doi.org/10.1111/gcb.15665).
-   CMIP6 Climate Projections: [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/datasets/projections-cmip6?tab=overview).
-   eBird Data Portal: [eBird.org](https://ebird.org/data/download).
-   Birdlife DataZone : [birdlife.org](https://datazone.birdlife.org/species/requestdis)