# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:01:04 2024

@author: sungg1095
"""
'''
Create a calculation to retrieve flood extend m2/km2 and mean flood depth (m)
'''
# import modules
import rasterio
from rasterio.plot import show
#from rasterstats import zonal_stats
import rioxarray as rxr
import os, sys
import numpy as np
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#%%
'''
Flood extent
'''
# 1. open flood map raster with rasterio as the variable 'fm'
# 'raster' is a numpy-array and 'fm' is the variable
# with-statement makes code more readable and automatically closes object
with rasterio.open(r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\flood_maps_SH\LF_1_5_m_my_region.tif") as fm:
                   raster = fm.read(1) # reads the raster data from the first band into a numpy array called 'raster'
                   rows, cols = raster.shape # gets the dimensions (width/height)
                   nodata = fm.nodata  # gets the nodata value and assign it to a variable
#%%
# Inspect my raster(fm)(metadata)
# check type of the variable "fm"
type(fm)

# 1.Projection
fm.crs

# 2. Dimensions
fm.width
fm.height
fm.shape

# 3. Number of bands
fm.count

# 4. data format
fm.driver

# 5. no data values
fm.nodatavals

# 6. all metadata for the whole raster
fm.meta

#%%
# 2. Calculate the total number of pixels
total_pixel_number = rows*cols
print(f"The total pixel number in my flood map is {total_pixel_number}.")
#%%
# 3. Calculate the number of nan pixels 
# if statement checks the variable 'raster' for nodata-values other than 'None'
if nodata is not None:
    raster[raster == nodata] = np.nan  # rename NoData values to NaN
    
# Count the number of NaN values
nan_count = np.isnan(raster).sum()
print(f"Number of NaN values: {nan_count}.")

#%%
# 4. Calculate flood extend by substracting nan_count from total_pixel_number
# and mutiplying with pixel size

# Define cell size
cell_size = 50*50

# calculate flooded pixels
flooded_pixel_count = total_pixel_number - nan_count
print(f"{flooded_pixel_count} Pixels are flooded.")

flooded_area_m2 = flooded_pixel_count * cell_size
print(f"The flooded area in m2 is: {flooded_area_m2} m2.")

flooded_area_km2 = flooded_area_m2 / 1000000
print(f"The flooded area in km2 is: {flooded_area_km2} km2.")

#%%
'''
Mean flood depth
''' 
# The objective is tp calculate de average maximum flood depth (hmax) of all flooded pixels.
# The nan pixels have to be left out

valid_pixels = raster[~np.isnan(raster)] # create df without NANs
valid_sum = valid_pixels.sum()  # calculate the sum of all water depths
mean_flood_depth = valid_sum / flooded_pixel_count # average flood depth 
# is created by dividing the sum by the total number of flooded pixels
print(f" {flooded_pixel_count} pixels are flooded with a mean flood depth of {mean_flood_depth:.3f} cm.")
median_flood_depth = np.median(valid_pixels)

stats = {
    'min': round(valid_pixels.min(), 3),
    'mean': round(valid_pixels.mean(), 3),
    'median': round(np.ma.median(valid_pixels), 3),
    'max': round(valid_pixels.max(), 3)
}

# Create a dictionary with the valus i need
df = pd.DataFrame({
        'event': '200yr event and 1.5 m slr - uni',
        'mean_f_depth_m': [mean_flood_depth],
        'f_extent_km2': [flooded_area_km2]
        #'min_f_depth_m': [stats['min']] # uncomment to calculate min and max hmax
       # 'max_f_depth_m': [stats['max']]
        
        }, index=[0])
#df = df.append(data, ignore_index=True)
df.to_csv(r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\calc_tables\LF_200_1_5m_statistics.csv")


