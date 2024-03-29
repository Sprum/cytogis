from src.cytogis import GISManager


if __name__ == "__main__":
    # confs: configure your in- and output paths ("../" goes to parent dir, "./" is the dir of the script)
    CONFIG = {"cyto_path": "../input/clustered.cyjs",
              "coord_path": "../input/location_f.csv",
              "out_path_nodes": "../output/cities_nodes.geojson",
              "out_path_edges": "../output/cities_edges.geojson",
              "cols_to_drop": ["geprüft", "Typ", "GND"],  # optional
              "lat_long_cols": ("Lat", "Len")
              }

    # instantiate GIS obj
    gis = GISManager(CONFIG)
    print("processing edges..")
    # create edges geojson obj and save it to disk
    edges_collection = gis.create_features_edges(processed=True)
    edges_collection.save_geojson(CONFIG["out_path_edges"])
    print("done!")

    print("processing nodes...")
    # create nodes geojson obj and save it to disk
    nodes_collection = gis.create_features_nodes()
    nodes_collection.save_geojson(CONFIG["out_path_nodes"])
    print("done!")

    print("Process finished.")
