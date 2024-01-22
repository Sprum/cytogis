import unittest
from src.cytogis import Feature


class TestFeatureInitialization(unittest.TestCase):
    def setUp(self):
        self.valid_obj_type = "Point"
        self.valid_coordinates = [1.0, 2.0]
        self.valid_properties = {"name": "TestPoint"}

    def test_initialize_feature_with_valid_parameters(self):
        feature = Feature(self.valid_obj_type, self.valid_coordinates, self.valid_properties)
        self.assertIsInstance(feature, Feature)

    def test_structure_attribute_initialization(self):
        feature = Feature(self.valid_obj_type, self.valid_coordinates, self.valid_properties)
        self.assertTrue(hasattr(feature, 'structure'))

    def test_populated_obj_attribute_population(self):
        feature = Feature(self.valid_obj_type, self.valid_coordinates, self.valid_properties)
        self.assertTrue(hasattr(feature, 'populated_obj'))


class TestFeatureValidation(unittest.TestCase):
    def test_validate_obj_type_with_valid_type(self):
        feature = Feature("Point", [1.0, 2.0], {"name": "TestPoint"})
        result = feature._validate_obj_type("Point")
        self.assertTrue(result)

    def test_validate_obj_type_with_invalid_type(self):
        feature = Feature("Point", [1.0, 2.0], {"name": "TestPoint"})
        with self.assertRaises(ValueError):
            feature._validate_obj_type("InvalidType")


class TestFeaturePopulating(unittest.TestCase):
    def test_populate_method(self):
        feature = Feature("Point", [1.0, 2.0], {"name": "TestPoint"})
        result = feature._populate([3.0, 4.0], {"name": "NewPoint"})

        self.assertEqual(result["geometry"]["coordinates"], [3.0, 4.0])
        self.assertEqual(result["properties"]["name"], "NewPoint")


class TestFeatureEdgeCases(unittest.TestCase):
    def test_initialize_feature_with_empty_coordinates(self):
        with self.assertRaises(ValueError):
            Feature("Point", [], {"name": "TestPoint"})

    def test_initialize_feature_with_empty_properties(self):
        feature = Feature("Point", [1.0, 2.0], {})
        self.assertEqual(feature.populated_obj["properties"], {})


if __name__ == '__main__':
    unittest.main()
