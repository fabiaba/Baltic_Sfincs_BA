# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:50:53 2024

@author: sungg1095
"""

"""
Create Waterlevel Timeseries as .csv file

"""
import pandas as pd
import geopandas as gpd
from io import StringIO
from shapely.geometry import Point

# import all csv files from all stations
colnames= ['sealevel', 'time']

Fl = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Flensburg.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
#%%
# Rename column 'sealevel' to ID of Flensburg (0)
Fl = Fl.rename(columns={'sealevel':1})

# create a variable "cols" and change the column order
cols = Fl.columns.tolist()
cols = cols[-1:] + cols[:-1]
cols  # print cols variable
# reorder the df
Fl = Fl[cols]

#%%
# Import Holnis and copy to Fl
Holnis = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Holnis.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
# Rename column 'sealevel' to ID of Holnis (1)
Holnis = Holnis.rename(columns={'sealevel': 2})
# Copy the '1' column from Holnis to Fl
Fl[2] = Holnis[2]


GeltingerBirk = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\GeltingerBirk.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
GeltingerBirk = GeltingerBirk.rename(columns={'sealevel': 3})
# copy the column "2" from Gb to Fl
Fl[3] = GeltingerBirk[3]



Schleimuende = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Schleimuende.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
Schleimuende = Schleimuende.rename(columns={'sealevel': 4})

Fl[4] = Schleimuende[4]



Kappeln = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Kappeln.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
Kappeln = Kappeln.rename(columns={'sealevel': 5})
Fl[5] = Kappeln[5]




Booknis = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Bock.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
Booknis = Booknis.rename(columns={'sealevel': 6})
Fl[6] = Booknis[6]




Eck = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Eckernfoerde.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
Eck = Eck.rename(columns={'sealevel': 7})
Fl[7] = Eck[7]



Kiel = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Eckernfoerde.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
Kiel = Kiel.rename(columns={'sealevel': 8})
Fl[8] = Kiel[8]



Schön = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Schoenberg.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
Schön = Schön.rename(columns={'sealevel':9})
Fl[9] = Schön[9]



Daz= pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Dazendorf.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
Daz = Daz.rename(columns={'sealevel':10})
Fl[10] = Daz[10]



Fehm = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Fehmarn.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
Fehm = Fehm.rename(columns={'sealevel':11})
Fl[11] = Fehm[11]



Kell = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\Kellenhusen.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
Kell = Kell.rename(columns={'sealevel':12})
Fl[12] = Kell[12]




Timm = pd.read_csv(
    r"C:\Users\sungg1095\Documents\BA_sfincs\baltic_data\Boundary\boundary_conditions\200yr_1_5m\TImmendorf.txt.bdy.bdy",
    sep=" ",
    names=colnames,
    header=None)
Timm = Timm.rename(columns={'sealevel':13})
Fl[13] = Timm[13]

#%%

boundary_stations = Fl

'''
Change timestamps in sec to DateTime format starting at 2023-01-01 00:00:00
'''
print(boundary_stations.columns)
# Define startdate variable
start_datetime = pd.Timestamp('2023-01-01T00:00:00')

# Convert time column to DateTime format
boundary_stations['datetime'] = start_datetime + pd.to_timedelta(boundary_stations['time'], unit='s')

# Remove column "time" and set column "datetime" as index column
boundary_stations = boundary_stations.drop(columns= {'time'})


# rename column "datetime" to "time"
boundary_stations = boundary_stations.rename(columns={'datetime':'time'})

#boundary_stations = boundary_stations.set_index('time')
#boundary_stations['time'] = boundary_stations['time'].dt.strftime('yyyy-MM-ddTHH:mm:ss')
boundary_stations =boundary_stations.set_index('time')
#%%
# save boundary stations to csv
boundary_stations.to_csv(
    r"C:\Users\sungg1095\Documents\GitHub\baltic_sfincs\baltic_data\waterlevel\boundary_stations_200y_1_5m.csv",
    sep=','
    )







































