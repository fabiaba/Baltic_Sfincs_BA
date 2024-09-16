# Baltic_Sfincs_BA
 Welcome to the git repository for my bachelor thesis. Here you can find relevant scripts that I created to run SFINCS on
 the german Baltic Sea coast and process the flood rasters afterwards.

SFINCS was set up using python language in a Jupiter Notebook.
This notebook together with the associated data catalogue is provided above. 
Additionally, the raw python script can be downloaded.

To retrieve flood extents and average maximum flood depths,
I calculated statistics using the two scripts "SFINCS_raster_statistics" and "SFINCS_statistics_postprocessing".
The first deals with calculating the extent and flood depth of individual flood maps and the latter mainly aggregates different csv files into one table.

Lastly, the script to create a waterlevel timeseries is provided as SFINCS requires specific date and table formatting. 
