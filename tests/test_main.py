
# tests/test_main.py
from fastapi.testclient import TestClient
from main import app

# Create a TestClient for your FastAPI application
client = TestClient(app)

def test_read_root():
    """
    Test the root endpoint.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "¡Bienvenido a mi API FastAPI!"}

def test_create_item():
    """
    Test the item creation endpoint.
    """
    response = client.post(
        "/items/",
        json={
            "name": "Test Item",
            "description": "This is a test item",
            "price": 10.99,
            "tax": 1.5
        }
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Ítem creado exitosamente"
    assert "item" in response.json()
    assert response.json()["item"]["name"] == "Test Item"

def test_read_items():
    """
    Test the read all items endpoint.
    """
    # Create a test item first
    client.post(
        "/items/",
        json={
            "name": "Another Item",
            "description": "Yet another test item",
            "price": 5.00,
            "tax": 0.5
        }
    )

    response = client.get("/items/")
    assert response.status_code == 200
    assert "items" in response.json()
    assert len(response.json()["items"]) > 0

def test_read_single_item():
    """
    Test the read single item by ID endpoint.
    """
    # Create a test item first to ensure there's something to read
    client.post(
        "/items/",
        json={
            "name": "Specific Item",
            "description": "This is a specific test item",
            "price": 20.00,
            "tax": 2.0
        }
    )

    response = client.get("/items/0")  # Assuming the first item created
    assert response.status_code == 200
    assert "item" in response.json()
    assert response.json()["item"]["name"] == "Test Item"

def test_read_non_existent_item():
    """
    Test reading a non-existent item.
    """
    response = client.get("/items/999")  # An ID that should not exist
    assert response.status_code == 200  # FastAPI often returns 200 even for not found if handled in logic
    assert response.json() == {"message": "Ítem no encontrado", "item_id": 999}

