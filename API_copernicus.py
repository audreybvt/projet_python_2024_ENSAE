import copernicusmarine
import s3fs

import pandas as pd
import geopandas as gpd

request_dataframe = copernicusmarine.subset(
  dataset_id="cmems_obs_si_arc_phy_my_L4-DMIOI_P1D-m",
  variables=["analysed_st", "analysis_error", "mask", "observation_max", "observation_min", "observation_num", "observation_std", "sea_ice_fraction"],
  minimum_longitude=-179.97500610351562,
  maximum_longitude=179.97500610351562,
  minimum_latitude=58,
  maximum_latitude=89.94999694824219,
  start_datetime="2023-10-31T00:00:00",
  end_datetime="2023-12-31T00:00:00",
)