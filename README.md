# Cyto to GIS

Convert Cytoscape .cyjs files to GeoJSON objects

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

Cyto to GIS is a Python package that facilitates the conversion of Cytoscape .cyjs files into GeoJSON objects to use in QGIS.
It provides functionality to extract node and edge data from Cytoscape JSON representations and transform them into GeoJSON features for geographical information systems (GIS) applications.

## Usage
Example for Using cyto_to_qgis:
```python
from cyto_to_gis import GISManager

# Configure your input and output paths
CONFIG = {
    "cyto_path": "YOUR_PATH_TO_cyjs_FILE",
    "coord_path": "YOUR_PATH_TO_COORDINATES_CSV",
    "out_path_nodes": "YOUR_PATH_TO_OUTPUT_NODES",
    "out_path_edges": "YOUR_PATH_TO_OUTPUT_EDGES",
    "lat_long_cols": ("your column name for latitude", "your column name for longitude"),
    "cols_to_drop": ["your", "cols", "to", "drop"]  # optional
    
}

# Instantiate GIS Manager
gis = GISManager(CONFIG)

# Process edges
edges_collection = gis.create_features_edges()
edges_collection.save_geojson(CONFIG["out_path_edges"])

# Process nodes
nodes_collection = gis.create_features_nodes()
nodes_collection.save_geojson(CONFIG["out_path_nodes"])

```
## Contributing
Contributions are welcome!

## Bug Reports and Feature Requests
If you encounter any issues or have ideas for improvements, please open an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

