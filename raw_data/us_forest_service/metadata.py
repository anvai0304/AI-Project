import os
import yaml

metadata = {
    "source_url": "https://www.fia.fs.fed.us/tools-data/",
    "description": "Data from the USDA Forest Service Forest Inventory and Analysis (FIA) program, including tree species composition, forest density, and forest health indicators.",
    "spatial_coverage": "Pacific Northwest region of the United States",
    "temporal_coverage": {
        "start": "2010-01-01",
        "end": "2022-12-31"
    },
    "data_format": "CSV"
}

with open("metadata.yaml", "w") as f:
    yaml.dump(metadata, f, sort_keys=False)