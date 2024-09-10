import os
import yaml

metadata = {
    "source_url": "https://modis.gsfc.nasa.gov/data/",
    "description": "MODIS satellite data for monitoring land cover changes, vegetation indices, and surface temperature in the Pacific Northwest region.",
    "spatial_coverage": "Pacific Northwest region of the United States",
    "temporal_coverage": {
        "start": "2010-01-01",
        "end": "2022-12-31"
    },
    "data_format": "HDF, GeoTIFF"
}

with open("metadata.yaml", "w") as f:
    yaml.dump(metadata, f, sort_keys=False)