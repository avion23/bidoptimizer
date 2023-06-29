import pytest
from src.excel_loader import ExcelLoader

def test_load():
    loader = ExcelLoader('data/Bidoptimizer v30 Caro.xlsx')
    try:
        data = loader.load()
        assert data is not None
    except Exception as e:
        pytest.fail(f"Loading the Excel file raised an exception: {e}")
