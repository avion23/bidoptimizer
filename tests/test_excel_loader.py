import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
from src.excel_loader import ExcelLoader
import pytest
import pandas as pd


@pytest.fixture(scope="module")
def excel_loader():
    file_path = "data/Bidoptimizer v30 Caro.xlsx"
    return ExcelLoader(file_path)

def test_load(excel_loader):
    data = excel_loader.load()
    assert isinstance(data, pd.DataFrame)
    assert len(data) > 0

def test_save(excel_loader):
    data = pd.DataFrame({"How To (genau lesen!)": [1, 2, 3]})
    output_path = "output.xlsx"
    excel_loader.save(data, output_path)

    loaded_data = pd.read_excel(output_path)
    assert isinstance(loaded_data, pd.DataFrame)
    assert list(loaded_data.columns) == list(data.columns)

    # Clean up the created output file
    import os
    os.remove(output_path)

def test_check_sheets(excel_loader):
    assert excel_loader.check_sheets() is True

