import json
import os


class Feature:
    """
    Class to create geojson features. supported Features right now are: LineString and Point.
    """
    def __init__(self, obj_type: str, coordinates: list, properties: dict) -> None:
        if not coordinates:
            raise ValueError("Coordinates cannot be empty.")
        if self._validate_obj_type(obj_type):
            self.structure = {
                "type": "Feature",
                "geometry": {
                    "type": obj_type,
                    "coordinates": None
                },
                "properties": None  # dict with all properties
            }
            self.populated_obj = self._populate(coordinates, properties)

    def _populate(self, coordinates: list, properties: dict) -> dict:
        """
        method to populate base Feature structure with properties. Returns Dictionary.
        :param coordinates: list
        :param properties: dict
        :return: dict
        """
        new_obj = self.structure.copy()
        new_obj["geometry"]["coordinates"] = coordinates
        new_obj["properties"] = properties
        return new_obj

    @staticmethod
    def _validate_obj_type(obj_type: str) -> bool:
        """
        validates if ob_type is a valid choices. Returns True if valid and raises Type Error if not.
        :param obj_type:
        :return: bool
        """
        valid_types = ['Point', 'LineString']
        if obj_type in valid_types:
            return True
        raise ValueError(f"Invalid obj_type: {obj_type}. Valid types are {valid_types}")


class FeatureCollection:
    """
    class to create geojson FeatureCollections with.
    """
    def __init__(self) -> None:
        self.__structure = {
            "type": "FeatureCollection",
            "features": [
                # list of features, append here
            ]
        }

    def add_feature(self, feature) -> None:
        """adds feature to collection"""
        self.__structure["features"].append(feature)

    def save_geojson(self, path) -> None:
        """
        func for saving geojson to disk
        :param path: str
        :return: none
        """
        try:
            geo_json = json.dumps(self._get_features(), indent=4)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding='UTF-8') as of:
                of.write(geo_json)
        except (Exception, PermissionError) as e:
            print(f"Error saving geojson: {e}")

    def _get_features(self) -> dict:
        """getter method"""
        return self.__structure
