"""
### Load pystac items into an Xarray

In this code you will : 

- Query a STAC API with pystac-client to get a `pystac-item` object; 
- Load the `pystac-item` object into an Xarray.DataArray using `stackstac`
- Stream the actual data in memory with dask workflow included in `stackstac`

!!! info
    This specific example uses the collections **hrdem-mosaic-1m**
    from CCMEO's datacube

"""
# --8<-- [start:transform]
def reorder_transform(gdal_transform):
    """
    Reorders the GDAL GeoTransform (6-element tuple) into the 9-element format
    that is compatible with proj:transform.
    """
    return [gdal_transform[1], gdal_transform[2], gdal_transform[0],
            gdal_transform[4], gdal_transform[5], gdal_transform[3],
            0, 0, 1]
# --8<-- [end:transform]

# --8<-- [start:code]
import pystac_client
import stackstac

# Define a bounding box for an AOI in EPSG:4326
bbox=[-71.2155,45.4012,-71.1079, 45.5083]
bbox_crs = "EPSG:4326"

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['hrdem-mosaic-1m'], 
    bbox=bbox,) 

# Re-order the proj:transform
result_items = []
# Use the pagination to improve efficiency
# Iterate over returned page and update the transform for each items
for page in search.pages():
    for item in page:
        # reorder_transform() function is define above
        reordered_transform = reorder_transform(
                                item.properties["proj:transform"]
                                )
        item.properties["proj:transform"] = reordered_transform
        result_items.append(item)

# Importing unnecessary assets may cause memory and speed issues.
# To know the assets available in this collection :
print(result_items[0].assets.keys())
# >> dict_keys(['dsm', 'dtm', 'dsm-vrt', 'dtm-vrt', 'thumbnail', 
#               'hillshade-dsm', 'hillshade-dtm', 'extent',
#               'coverage',])

items_xarray = stackstac.stack(result_items, 
                          assets = ["dsm", "dtm"], 
                          bounds_latlon = bbox, 
                          chunksize = (1000, 1000),
                          epsg = 3979,
                          properties=False)

print(items_xarray)
# >>> items_xarray 
# <xarray.DataArray 'stackstac-a96f69db1a66a462b3fb7c84c412aa7e' (time: 1,
#                                                                 band: 2,
#                                                                 y: 8812, 
#                                                                 x: 7581)> Size: 1GB
# dask.array<fetch_raster_window, shape=(1, 2, 8812, 7581), dtype=float64, chunksize=(1, 1, 1000, 1000), chunktype=numpy.ndarray>
# Coordinates:
#   * time         (time) datetime64[ns] 8B 2023-05-09T12:00:00
#     id           (time) <U13 52B '9_2-mosaic-1m'
#   * band         (band) <U3 24B 'dsm' 'dtm'
#   * x            (x) float64 61kB 1.843e+06 1.843e+06 ... 1.855e+06 1.855e+06
#   * y            (y) float64 70kB -3.925e+04 -3.925e+04 ... -5.362e+04
#     title        (band) <U27 216B 'Digital Surface Model (COG)' 'Digital Terr...
#     description  (band) <U61 488B 'Digital Surface Model derived fromAirborne...
#     epsg         int64 8B 3979
# Attributes:
#     spec:           RasterSpec(epsg=3979, bounds=(1842906.2779342758, -53625....
#     crs:            epsg:3979
#     transform:      | 1.63, 0.00, 1842906.28|\n| 0.00,-1.63,-39249.98|\n| 0.0...
#     resolution_xy:  (1.6327081635433747, 1.6314054662236352)

# At this point, the metadata and array shape are set, but the data itself isn't read.
# Running .compute() allows Dask to optimize the workflow, evaluating and executing it 
# in the most efficient way, optimizing resource usage.
# # --8<-- [end:code]

# --8<-- [start:example]
# Example : Get the mean surface height for the AOI
# 1. Subtract the dtm to the dsm
# Dimension are [time, band, x, y], and band are : [dsm, dtm]
items_xarray['surface_height'] = items_xarray[:, 0, :, :] - items_xarray[:, 1, :, :]
# items_xarray[:, 0, :, :] -> Getting all from dimension time, x and y, and only element 0 from dimension band
# 2. Compute the calculation, before that, only the workflow was defined
surface_height = items_xarray.surface_height.compute()
# 3. Perform the mean
surface_height.mean()
# --8<-- [end:example]
