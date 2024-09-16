# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 08:58:01 2024

@author: sungg1095
"""

'''
Post-processing of flood maps statistics based on the script "SFINCS_raster_statistics"
'''
# import modules
import rasterio
from matplotlib import pyplot as plt
from rasterio.plot import show
import rioxarray as rxr
import os, sys
import numpy as np
import geopandas as gpd
import pandas as pd
#%%

'''
1. Storm surges
-----
aggegrate all statistics dfs created with the script "SFINCS_raster_statistics"
for the three storm surge events to one
'''
# read all three csv files
fm200 = pd.read_csv(
    r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\calc_tables\200y_mod_statistics.csv",
    sep=',',
    usecols=[1,2,3]
    )
fm200_1 = pd.read_csv(
    r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\calc_tables\200y_1m_mod_statistics.csv",
    sep=',',
    usecols=[1,2,3]
    )
fm200_1_5 = pd.read_csv(
    r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\calc_tables\200y_1_5m_mod_statistics.csv",
    sep=',',
    usecols=[1,2,3]
    )

# join all dfs into one --> 'result'
frames = [fm200, fm200_1, fm200_1_5]   # create a list with all dfs

result = pd.concat(frames)    # use concat to join all dfs in the list
print(result)

index = pd.Index([0,1,2])   # set a new index
result = result.set_index(index)

result.to_csv(r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\calc_tables\all_events_statistics.csv")


#%%
'''
2. Roughness Sensitivity Analysis
-----
aggegrate all statistics dfs created with the script "SFINCS_raster_statistics"
for different roughness set ups to one
'''
# Create a daframe with all roughness tables
# the simulation ran with res = 50, zmin = -2

rgh_mod = pd.read_csv(
   r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\calc_tables\200y_1_5m_mod_statistics.csv",
   sep=',',
   usecols=(1,2,3)
    )
rgh_high = pd.read_csv(
    r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\vgl_roughness\200y_1_5m_high_statistics.csv",
    sep=',',
    usecols=(1,2,3)
    )
rgh_uni = pd.read_csv(
    r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\vgl_roughness\200y_1_5m_uni_statistics.csv",
    sep=',',
    usecols=(1,2,3)
    )
rgh_land_water =pd.read_csv(
    r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\vgl_roughness\200y_1_5m_land&water_statistics.csv",
    sep=',',
    usecols=(1,2,3)
    )
#%%

# join all dfs into one --> 'result'
frames2 = [rgh_mod, rgh_high, rgh_uni, rgh_land_water]   # create a list with all dfs
#%%
result2 = pd.concat(frames2)    # use concat to join all dfs in the list
print(result2)

index2 = pd.Index([0,1,2,3])   # set a new index
result2 = result2.set_index(index2)

#%%
result2.to_csv(r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\vgl_roughness\roughness_comparison_wholedomain.csv")

#%%
'''
3. Roughness Sensitivity Analysis only for Fehmarn
'''
rgh_mod_fehm = pd.read_csv(
   r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\vgl_roughness\sensitivity_fehmarn\fehm_200y_1_5m_mod_statistics.csv",
   sep=',',
   #index_col='event',
   usecols=(1,2,3)
    )
rgh_high_fehm = pd.read_csv(
    r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\vgl_roughness\sensitivity_fehmarn\fehm_200y_1_5m_high_statistics.csv",
    sep=',',
    #index_col='event',
    usecols=(1,2,3)
    )
rgh_uni_fehm = pd.read_csv(
    r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\vgl_roughness\sensitivity_fehmarn\fehm_200y_1_5m_uni_statistics.csv",
    sep=',',
    #index_col='event',
    usecols=(1,2,3)
    )
rgh_land_water_fehm =pd.read_csv(
    r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\vgl_roughness\sensitivity_fehmarn\fehm_200y_1_5m_land&water_statistics.csv",
    sep=',',
    #index_col='event',
    usecols=(1,2,3)
    )

frames3 = [rgh_mod_fehm, rgh_high_fehm, rgh_uni_fehm, rgh_land_water_fehm]
result3 = pd.concat(frames3)
print(result3)

index3 = pd.Index([0,1,2,3])
result3 = result3.set_index(index3)

# Fehmarn area= 181,764 km2
#%% 
# variable with total area of Fehmarn
total_area_km2 = 181.764 # the area is based on own calculations in QGIS

# function to calculate area percentage of each flood extent
def flood_extent_percentage(f_extent_km2, total_area_km2):
    return (f_extent_km2 / total_area_km2)*100

# apply the function to create a new column in my dataframe
result3['f_extent_%'] = result3['f_extent_km2'].apply(flood_extent_percentage,total_area_km2 = total_area_km2).round(2)
  
# export df to csv                                              
result3.to_csv(r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\output_processed\vgl_roughness\sensitivity_fehmarn\roughness_comparison_fehm.csv")






















