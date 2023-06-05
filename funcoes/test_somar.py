from somar import somar
from dividir import dividir
from multiplicar import multiplicar
from subtrair import subtrair


import pytest

def test_somar():
    assert somar(11,12) == 23
    
def test_somar_incorreto():
    with pytest.raises(Exception):
        somar("abc", "xyz")

def test_somar_incorreto_menor10():
    with pytest.raises(Exception):
        somar(1,3)

def test_subtrair():
   assert subtrair(3,1) == 2

def test_multiplicar():
   assert multiplicar(3,3) == 9

def test_dividir():
    assert dividir(3,3) == 1