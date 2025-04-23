# Cloud Optimized Geospatial Data Access

Best practices and tutorials using open-source libraries for Cloud Optimized GeoTIFF (COG) access
from the Canada Center for Mapping and Earth Observation (CCMEO) datacube. 

!!! info "Link to CCMEO COG collections "
    STAC API : <https://datacube.services.geo.ca/stac/api/>  
    STAC API via STAC-Browser : <https://radiantearth.github.io/stac-browser/#/external/datacube.services.geo.ca/stac/api/?.language=en>

<!--- 
What should be on the main page : 
A single sentence that says what the product is, succinctly and memorably.
A paragraph of one to three short sentences, that describe what the product does.
A third paragraph of similar length, this time explaining what need the product meets.
Finally, a paragraph that describes whom the product is useful for.
-->
---

## In this site...
<div class="grid cards" markdown>
-   __How-to guides__

    ---

    **Code examples** covering key operations and common tasks
    :arrow_right: [how-to guides](pystac-client.md)

-   __External references__

    ---

    :arrow_right: [**external references**](reference.md)  


    <!-- :arrow_right: [Quick links](reference.md) -->
</div>
---

## Libraries used in the examples:

### To Discover Data

From [Radiant Earth] :  

- [pystac-client]

### To Access Data  

Based on GDAL :

- [rasterio]
- [rioxarray]

Third party libraries using STAC objects :

- [stackstac]
- [odc-stac]

## Report an Issue

If you encounter any issues, please [create a new issue](https://github.com/NRCan/cloud-optimized-geospatial/issues/new/choose) using our template.

## License
The examples are released under the [Open Government License - Canada](https://open.canada.ca/en/open-government-licence-canada).

!!! Note
    All the libraries and resources presented here are open-source and have their own licensing.
    Please refer to the specific libraries documentation for licensing information.

[pystac-client]: https://pystac-client.readthedocs.io/en/stable/usage.html
[rasterio]: https://rasterio.readthedocs.io/en/latest/quickstart.html
[stackstac]: https://stackstac.readthedocs.io/en/latest/basic.html
[odc-stac]: https://odc-stac.readthedocs.io/en/latest/
[rioxarray]: https://corteva.github.io/rioxarray/stable/
[Radiant Earth]: https://github.com/radiantearth
*[COG]: Cloud Optimized GeoTIFF
*[CCMEO]: Canada Center for Mapping and Earth Observation, Natural Resources Canada
*[STAC]: Spatio-Temporal Asset Catalog
