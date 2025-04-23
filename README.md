# Cloud Optimized Geospatial Data Access
Best practices and tutorials using open-source libraries for Cloud Optimized GeoTIFF (COG) access from Natural Resources Canada's Center for Mapping and Earth Observation (CCMEO) datacube.

See the GitHub pages repository site : https://nrcan.github.io/cloud-optimized-geospatial/    

Built with : [![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

## Link to CCMEO COG collections 
STAC API : <https://datacube.services.geo.ca/stac/api/>  
STAC API via STAC-Browser : <https://radiantearth.github.io/stac-browser/#/external/datacube.services.geo.ca/stac/api/?.language=en>

## Libraries used in the examples.

### To discover data  

From [Radiant Earth] : 
- [pystac-client]

### To access data  

Based on GDAL :

- [rasterio]
- [rioxarray]

Third party libraries using STAC objects :

- [stackstac]
- [odc-stac]

[pystac-client]: https://pystac-client.readthedocs.io/en/stable/usage.html
[rasterio]: https://rasterio.readthedocs.io/en/latest/quickstart.html
[stackstac]: https://stackstac.readthedocs.io/en/latest/basic.html
[rioxarray]: https://corteva.github.io/rioxarray/stable/
[odc-stac]: https://odc-stac.readthedocs.io/en/latest/intro.html
[Radiant Earth]: https://github.com/radiantearth

## Report an Issue

If you encounter any issues, please [create a new issue](https://github.com/NRCan/cloud-optimized-geospatial/issues/new/choose) using our templates.

## License
The examples are released under the [Open Government License - Canada](https://open.canada.ca/en/open-government-licence-canada).
