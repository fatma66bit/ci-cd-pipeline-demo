# tests/test_fixtures.py
import pytest
import tempfile
import os

@pytest.fixture
def calculator():
    """Fixture qui fournit une calculatrice configurée"""
    from app import add, subtract, multiply, divide
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

@pytest.fixture
def temporary_data():
    """Fixture avec setup et teardown"""
    # Setup
    data = {"x": 10, "y": 2}
    print("\nSetup: Données créées")
    yield data  # Passe les données au test
    # Teardown (automatique après le test)
    print("Teardown: Nettoyage")

@pytest.fixture
def temp_file(tmp_path):
    """Utilise la fixture intégrée tmp_path de pytest"""
    file = tmp_path / "test_data.txt"
    file.write_text("42\n3.14\nHello")
    return file

def test_with_calculator_fixture(calculator):
    """Utilise la fixture calculator"""
    assert calculator["add"](2, 3) == 5
    assert calculator["multiply"](4, 5) == 20

def test_with_temporary_data(temporary_data):
    """Utilise la fixture avec données temporaires"""
    assert temporary_data["x"] + temporary_data["y"] == 12

def test_temp_file_operations(temp_file):
    """Test avec fichier temporaire"""
    content = temp_file.read_text()
    assert "42" in content
    assert "Hello" in content