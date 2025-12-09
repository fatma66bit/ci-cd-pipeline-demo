# tests/test_markers.py
import pytest
import time

@pytest.mark.slow
def test_slow_operation():
    """Test marqué comme lent"""
    time.sleep(0.5)  # Simulation d'une opération lente
    assert 1 + 1 == 2

@pytest.mark.fast
def test_fast_operation():
    """Test marqué comme rapide"""
    assert 2 * 2 == 4

@pytest.mark.skip(reason="Fonctionnalité pas encore implémentée")
def test_unimplemented():
    """Test ignoré temporairement"""
    assert False

@pytest.mark.xfail(reason="Bug connu à corriger")
def test_known_bug():
    """Test qui échoue mais c'est attendu"""
    assert 1 == 2  # Bug connu

@pytest.mark.parametrize("input", [1, 2, 3])
@pytest.mark.positive
def test_positive_numbers(input):
    """Test avec multiple marqueurs"""
    assert input > 0

# Pour exécuter uniquement les tests 'fast'
# python -m pytest tests/ -m fast -v