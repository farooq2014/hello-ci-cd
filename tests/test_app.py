import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import greet

def test_greet():
    assert greet("CI/CD") == "Hello, CI/CD!"
