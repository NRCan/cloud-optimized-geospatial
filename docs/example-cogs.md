# Accessing COG Data
Examples on how to use python libraries to access and use COGs. Demonstrating one of the cloud
optimized advantages, being able to access a **[portion of the data]** without having to download the entire file.  

See <https://guide.cloudnativegeo.org/>

## Using [rasterio]

``` sh
--8<-- "how-to-guides/rasterio-requirements.txt:2:2"
```

The developers of the rasterio library provide additional examples of usage. 
For more details on the rasterio library, see the [rasterio] documentation.

!!! Note
    The following examples starts with a request to the CCMEO STAC API via the pystac-client library.  

    For more details on how to discover data through the STAC API, see the **[Interacting with CCMEO STAC API]** section

<!-- START: Read the header of a cog using rasterio -->
::: how-to-guides.rasterio-header-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="23-35"
--8<-- "how-to-guides/rasterio-header-example.py:code"
```
<!-- END: Read the header of a cog using rasterio -->

<!-- START: Read a portion of a cog using rasterio -->
::: how-to-guides.rasterio-window-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="27-37"
--8<-- "how-to-guides/rasterio-window-example.py:code"
```
<!-- END: Read a portion of a cog using rasterio -->

[rasterio installation]: https://rasterio.readthedocs.io/en/stable/installation.html
[rasterio]: https://rasterio.readthedocs.io/en/latest/quickstart.html
[Interacting with CCMEO STAC API]: pystac-client.md
[portion of the data]: #how-to-guides.rasterio-window-example--read-a-portion-of-a-remote-cog

*[COG]: Cloud Optimized GeoTIFF
*[STAC]: Spatio-Temporal Asset Catalog
*[CCMEO]: Canada Center for Mapping and Earth Observation, Natural Resources Canada
