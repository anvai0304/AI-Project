import os
import yaml

metadata = {
    "source_url": "https://www.gbif.org/",
    "description": "Biodiversity data from the Global Biodiversity Information Facility (GBIF), including species occurrence records for the Pacific Northwest region.",
    "spatial_coverage": "Pacific Northwest region of the United States",
    "temporal_coverage": {
        "start": "2010-01-01",
        "end": "2022-12-31"
    },
    "data_format": "CSV, Darwin Core Archive"
}

with open("metadata.yaml", "w") as f:
    yaml.dump(metadata, f, sort_keys=False)