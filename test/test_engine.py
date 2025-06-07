"""
KasauSec - Basic tests for engine.py
"""

import pytest
from core import engine

def test_engine_init():
    eng = engine.Engine()
    assert eng is not None

def test_engine_flow(monkeypatch):
    eng = engine.Engine()
    
    # Mock methods to test flow without real network calls
    monkeypatch.setattr(eng, 'run_recon', lambda target: ['sub1.example.com', 'sub2.example.com'])
    monkeypatch.setattr(eng, 'run_scans', lambda subs: {'sub1.example.com': ['XSS'], 'sub2.example.com': []})
    monkeypatch.setattr(eng, 'run_exploits', lambda scan_res: {'sub1.example.com': True, 'sub2.example.com': False})
    
    result = eng.run('example.com')
    assert isinstance(result, dict)
    assert 'sub1.example.com' in result
    assert result['sub1.example.com'] is True
