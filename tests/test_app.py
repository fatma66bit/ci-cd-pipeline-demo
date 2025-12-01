# tests/test_app.py - Tests pour notre application
import sys
import os
# Ajoute le dossier parent au chemin Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# tests/test_app.py - Tests pour notre application
import pytest
from app import add, subtract, multiply, divide

def test_add():
    """Test de l'addition"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test de la soustraction"""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0

def test_multiply():
    """Test de la multiplication"""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    """Test de la division"""
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    
    # Test d'erreur de division par zéro
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_edge_cases():
    """Tests des cas limites"""
    # Grands nombres
    assert add(1000000, 1000000) == 2000000
    
    # Nombres décimaux
    assert add(0.1, 0.2) == pytest.approx(0.3)
    
    # Nombres négatifs
    assert multiply(-5, -5) == 25