from src.cytogis import GISManager

if __name__ == "__main__":
    # confs: configure your in- and output paths ("../" goes to parent dir, "./" is the dir of the script)
    CONFIG = {"cyto_path": "../input/MutiDi_Städte_Ego_Tübingen1564-1572.cyjs--clustered.cyjs",
              "coord_path": "../input/location_f.csv",
              "out_path_nodes": "../output/tübingen_nodes4.geojson",
              "out_path_edges": "../output/tübingen_edges4.geojson",
              "lat_long_cols": ("Lat", "Len"),
              "node_props_drop": ["lng", "lat", "id", "shared_name", "name", "value"],
              "processed": True,
              "cols_to_drop": ["geprüft", "Typ", "GND"],  # optional
              }

    # instantiate GIS obj
    gis = GISManager(CONFIG)
    print("processing edges..")
    # create edges geojson obj and save it to disk
    edges_collection = gis.create_features_edges()
    edges_collection.save_geojson(CONFIG["out_path_edges"])
    print("done!")

    print("processing nodes...")
    # create nodes geojson obj and save it to disk
    nodes_collection = gis.create_features_nodes()
    nodes_collection.save_geojson(CONFIG["out_path_nodes"])
    print("done!")

    weighted_nodes = gis.weight_nodes(nodes_collection)
    weighted_nodes.save_geojson("../output/new_nodes.geojson")
    print("Process finished.")
