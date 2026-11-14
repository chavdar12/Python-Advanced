"""Users and products persisted as JSON files in the db folder (no GUI code here, so it can be tested)."""
import json
from pathlib import Path

DB_DIR = Path(__file__).with_name("db")


def _read(name, db_dir):
    path = Path(db_dir) / name
    return json.loads(path.read_text()) if path.exists() else []


def _write(name, data, db_dir):
    (Path(db_dir) / name).write_text(json.dumps(data, indent=2))


def register(username, password, first_name, last_name, db_dir=DB_DIR):
    if not username or not password or not first_name or not last_name:
        raise ValueError("All fields are required")
    users = _read("users.json", db_dir)
    if any(u["username"] == username for u in users):
        raise ValueError("Username is already taken")
    users.append({"username": username, "password": password, "first_name": first_name,
                  "last_name": last_name, "products": []})
    _write("users.json", users, db_dir)


def login(username, password, db_dir=DB_DIR):
    return any(u["username"] == username and u["password"] == password for u in _read("users.json", db_dir))


def list_products(db_dir=DB_DIR):
    return _read("products.json", db_dir)


def buy(username, product_id, db_dir=DB_DIR):
    products = _read("products.json", db_dir)
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None or product["count"] <= 0:
        raise ValueError("Product is not available")
    users = _read("users.json", db_dir)
    user = next(u for u in users if u["username"] == username)
    product["count"] -= 1
    user["products"].append(product_id)
    _write("products.json", products, db_dir)
    _write("users.json", users, db_dir)
