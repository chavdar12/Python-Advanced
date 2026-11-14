import json
import tempfile
import unittest
from pathlib import Path

import storage


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name)
        (self.db / "products.json").write_text(json.dumps([{"id": 1, "name": "Mouse", "count": 1}]))

    def tearDown(self):
        self.tmp.cleanup()

    def test_register_and_login(self):
        storage.register("peter", "123", "Peter", "Petrov", db_dir=self.db)
        self.assertTrue(storage.login("peter", "123", db_dir=self.db))
        self.assertFalse(storage.login("peter", "wrong", db_dir=self.db))

    def test_register_validates(self):
        storage.register("peter", "123", "Peter", "Petrov", db_dir=self.db)
        with self.assertRaises(ValueError):
            storage.register("peter", "456", "Other", "Name", db_dir=self.db)
        with self.assertRaises(ValueError):
            storage.register("", "1", "A", "B", db_dir=self.db)

    def test_buy_decreases_count_and_records_product(self):
        storage.register("peter", "123", "Peter", "Petrov", db_dir=self.db)
        storage.buy("peter", 1, db_dir=self.db)
        self.assertEqual(storage.list_products(db_dir=self.db)[0]["count"], 0)
        users = json.loads((self.db / "users.json").read_text())
        self.assertEqual(users[0]["products"], [1])
        with self.assertRaises(ValueError):
            storage.buy("peter", 1, db_dir=self.db)


if __name__ == "__main__":
    unittest.main()
