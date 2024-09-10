import os
import yaml

metadata = {
    "source_url": "https://www.ncdc.noaa.gov/cdo-web/",
    "description": "Climate data from NOAA's Climate Data Online service, including temperature, precipitation and extreme weather events for the Pacific Northwest region.",
    "spatial_coverage": "Pacific Northwest region of the United States",
    "temporal_coverage": {
        "start": "2010-01-01",
        "end": "2022-12-31"
    },
    "data_format": "CSV, NetCDF"
}

with open("metadata.yaml", "w") as f:
    yaml.dump(metadata, f, sort_keys=False)