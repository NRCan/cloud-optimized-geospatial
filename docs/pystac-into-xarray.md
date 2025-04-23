# Additional Libraries

The following examples focus on loading COG data into xarray object backed by Dask for efficient in memory reading and processing. 

!!! info
    [Xarray] is build on NumPy and Pandas, adding capabilities for labeled and multi-dimensional arrays (e.g., climate data, satellite images). It extends NumPy arrays by attaching metadata (coordinates, labels), making it easier to work with data dimensions like time, latitude, longitude, and other variables.

    Xarray can use Dask arrays for lazy evaluation, enabling work with large datasets that don't fit in memory. Dask optimizes workflows by parallelizing tasks, reading data in chunks, and improving performance and memory efficiency.

    Source : [Xarray: Parallel Computing with Dask] 

!!! Note
    The following examples starts with a request to the CCMEO STAC API via the pystac-client library.  

    For more details on how to discover data through the STAC API, see the **[Interacting with CCMEO STAC API]** section

## Using Rioxarray

Load a single COG, using the link to the s3 object, into an xarray.

Rioxarray is based on rasterio, and can be used to read data into Xarray object. The developers of the rioxarray library provide additional usage examples, like this [one](https://corteva.github.io/rioxarray/stable/examples/read-locks.html).

``` sh
--8<-- "how-to-guides/rioxarray-requirements.txt"
```
Source :  [rioxarray installation]

::: how-to-guides.rioxarray-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

!!! Note 
    When using `rioxarray.open_rasterio()` set `chunks` to enable lazy loading with Dask. This allows Dask to read data in smaller chunks, improving speed and memory usage through parallel computing. For example, a `chunk` size of 1000 for both x and y means Dask reads 100x100 boxes instead of the entire array, processing multiple chunks simultaneously.

``` py linenums="1" hl_lines="20-23"
--8<-- "how-to-guides/rioxarray-example.py:code"
```
See [working-with-xarray-object] or [community-notebook-complete-examples] section for an example on using Xarray object.

## From pystac item object to Xarray object. 

See [pystac.Item] or [pystac-client] for more information.

!!! Warning
    The following libraries are not part of the [STAC utils] ecosystem. Be aware of the maintaining status of those libraries.

!!! Warning
    GDAL's GetGeoTransform and rasterio use different formats for transform metadata. When using GDAL based method you need to re-order the transform. 
    See [Re-order the STAC proj:Transform] for more details.
    ``` py
    --8<-- "how-to-guides/odc-stac-example.py:transform"
    ```
        
    For more information, please see [STAC documentation on proj:transform]

### Using [stackstac]

This is a third party library based on Xarray, but not listed under the Xarray documentation. 

``` sh
--8<-- "how-to-guides/stackstac-requirements.txt"
```
If you have problems with the installation, please refer to [stackstac installation].

<!-- START: Read with stackstac-stac -->
::: how-to-guides.stackstac-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="36-41"
--8<-- "how-to-guides/stackstac-example.py:code"
```

See [working-with-xarray-object] or [community-notebook-complete-examples] section for an example on using Xarray object.
### Using [odc-stac]

This is a third party library based on Xarray, but not listed under the Xarray documentation. 

``` sh
--8<-- "how-to-guides/odc-stac-requirements.txt"
```
If you have problems with the installation, please refer to [odc-stac installation].

<!-- START: Read with odc-stac -->
::: how-to-guides.odc-stac-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="38-41"
--8<-- "how-to-guides/odc-stac-example.py:code"
```
See [working-with-xarray-object] or [community-notebook-complete-examples] section for an example on using Xarray object.

## Working with Xarray object
See `Xarray.DataArray` for details on methods : <https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html>
``` py linenums="1"
--8<-- "how-to-guides/stackstac-example.py:example"
```
## Community Notebook complete examples

- [Loading multi-collections in a Xarray.Dataset]
- [Calculating the flow direction using open source library pyflwdir and Xarray.DataArray]

[Access COG data using rioxarray]: example-cogs.md/#using-rioxarray
[Xarray]: https://docs.xarray.dev/en/stable/
[Xarray: Parallel Computing with Dask]: https://docs.xarray.dev/en/stable/user-guide/dask.html
[STAC documentation on proj:transform]:  https://github.com/stac-extensions/projection?tab=readme-ov-file#projtransform
[Re-order the STAC proj:Transform]: reorder-transform-example.md
[odc-stac installation]: https://odc-stac.readthedocs.io/en/latest/intro.html#installation
[stackstac installation]: https://stackstac.readthedocs.io/en/latest/#installation
[STAC utils]: https://github.com/stac-utils
[pystac-client]: https://pystac-client.readthedocs.io/en/stable/
[pystac.Item]: https://pystac.readthedocs.io/en/latest/api/pystac.html#item
[stackstac]: https://stackstac.readthedocs.io/en/latest/
[odc-stac]: https://odc-stac.readthedocs.io/en/latest/
[rioxarray installation]: https://corteva.github.io/rioxarray/stable/installation.html
[rioxarray]: https://corteva.github.io/rioxarray/stable/index.html
[Xarray]: https://docs.xarray.dev/en/stable/
[Xarray: Parallel Computing with Dask]: https://docs.xarray.dev/en/stable/user-guide/dask.html
[Interacting with CCMEO STAC API]: pystac-client.md
[working-with-xarray-object]: #working-with-xarray-object
[community-notebook-complete-examples]: #community-notebook-complete-examples
<!-- TODO : Find a better way to link those jupyternotebooks... -->
[Loading multi-collections in a Xarray.Dataset]: https://github.com/NRCan/cloud-optimized-geospatial/blob/ec2de7af4249ee53b9c1cdf106e8fa9b6118b5cb/how-to-guides/notebook/multi-collection-example.ipynb
[Calculating the flow direction using open source library pyflwdir and Xarray.DataArray]: https://github.com/NRCan/cloud-optimized-geospatial/blob/ec2de7af4249ee53b9c1cdf106e8fa9b6118b5cb/how-to-guides/notebook/pyflwdir-example.ipynb
