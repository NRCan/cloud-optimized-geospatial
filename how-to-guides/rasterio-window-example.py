"""
## Read a portion of a remote COG

For this example, you will need to also install [shapely](https://shapely.readthedocs.io/en/stable/installation.html):   
```bash
pip install shapely
```

In this code you will : 

- Query a STAC API with pystac-client to get link to a COG;
- Read a portion of a remote COG based on an AOI with the window functionality;
- Optionally write the portion locally inside a .tif file

!!! info
    This specific example uses the collection **mrdem-30** from CCMEO's datacube

!!! Tip
    COG'S file contains internal tiling that can be leverage by iterating on
    the `src.block_windows()` while reading. If the reading window does not align with 
    the internal tiling of the file, the data will be resampled. 

    Example : <https://rasterio.readthedocs.io/en/stable/topics/windowed-rw.html#blocks>

    API definition: <https://rasterio.readthedocs.io/en/stable/topics/windowed-rw.html#blocks>
"""
# --8<-- [start:code]
import pystac_client
import rasterio 
from rasterio.windows import from_bounds
from rasterio.warp import transform_geom
from shapely.geometry import box, shape


# Define a bounding box for an AOI (Ottawa) in EPSG:4326
bbox=[-75.8860,45.3157,-75.5261,45.5142]
bbox_crs = "EPSG:4326"

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['mrdem-30'], 
    bbox=bbox,
	) 

# Get the link to the data asset for mrdem-30 dtm
links = []
for page in search.pages():
	for item in page:
		links.append(item.assets['dtm'].href)

# Read AOI from the first COG
with rasterio.open(links[0]) as src:
    # Transform bbox to src EPSG
    transformed_bbox = shape(transform_geom(src.crs, bbox_crs, 
                                                box(*bbox))).bounds
    # Define the window to read the values
    window=from_bounds(transformed_bbox[0], transformed_bbox[1], 
                       transformed_bbox[2], transformed_bbox[3], 
                       src.transform)
    # Read value from file
    rst = src.read(1, window=window)
    
    # Copy and update the source metadata to write the output tiff
    metadata = src.meta.copy()
    metadata.update({
        'height': window.height,
        'width': window.width,
        'transform': rasterio.windows.transform(window, src.transform)
    }) 

# Perform analysis ...

# Write the output array to a tiff file
output_tiff = r"path/to/output.tif"
with rasterio.open(output_tiff, 'w', **metadata) as dst:
    dst.write(rst, 1)
# --8<-- [end:code]




