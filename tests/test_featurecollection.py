import os
import unittest
from src.cytogis import FeatureCollection


class TestFeatureCollectionInitialization(unittest.TestCase):
    def test_initialize_feature_collection(self):
        feature_collection = FeatureCollection()
        self.assertIsInstance(feature_collection, FeatureCollection)

    def test_structure_attribute_initialization(self):
        feature_collection = FeatureCollection()
        self.assertTrue(hasattr(feature_collection, '_FeatureCollection__structure'))


class TestFeatureCollectionAddingFeatures(unittest.TestCase):
    def setUp(self):
        self.feature_collection = FeatureCollection()
        self.feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [1.0, 2.0]},
                        "properties": {"name": "TestPoint"}}

    def test_add_feature_method(self):
        self.feature_collection.add_feature(self.feature)
        self.assertEqual(len(self.feature_collection.get_features()["features"]), 1)


class TestFeatureCollectionSavingGeoJSON(unittest.TestCase):
    def setUp(self):
        self.feature_collection = FeatureCollection()
        self.feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [1.0, 2.0]},
                        "properties": {"name": "TestPoint"}}
        self.feature_collection.add_feature(self.feature)
        self.test_file_path = "./output/test.geojson"
        os.makedirs("./output", exist_ok=True)

    def test_save_geojson_method(self):
        self.feature_collection.save_geojson(self.test_file_path)
        with open(self.test_file_path, "r") as tf:
            content = tf.read()
        self.assertIn("Feature", content)

    def tearDown(self):
        # Clean up remove the test geojson file
        import os
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)


class TestFeatureCollectionEdgeCases(unittest.TestCase):

    def test_initialize_feature_collection_with_empty_structure(self):
        feature_collection = FeatureCollection()
        self.assertEqual(feature_collection.get_features()["features"], [])

    def test_save_geojson_with_invalid_path(self):
        feature_collection = FeatureCollection()
        feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [1.0, 2.0]},
                   "properties": {"name": "TestPoint"}}
        feature_collection.add_feature(feature)

        test_file_path = "/invalid/pathss/to/files.geojson"
        print(os.path.exists(os.path.dirname(test_file_path)))
        self.assertFalse(os.path.exists(os.path.dirname(test_file_path)))

        # Call the method
        feature_collection.save_geojson(test_file_path)

        # Check if the directory exists after calling the method
        self.assertTrue(os.path.exists(os.path.dirname(test_file_path)))


if __name__ == '__main__':
    unittest.main()
