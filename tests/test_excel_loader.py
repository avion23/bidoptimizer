import pytest
import pandas as pd
from src.excel_loader import ExcelLoader

@pytest.fixture(scope="module")
def excel_loader():
    file_path = "data/Bidoptimizer v30 Caro.xlsx"
    return ExcelLoader(file_path)

def test_load(excel_loader):
    data = excel_loader.load()
    assert isinstance(data, pd.DataFrame)
    assert len(data) > 0

def test_save(excel_loader):
    data = pd.DataFrame({"Column1": [1, 2, 3], "Column2": [4, 5, 6]})
    output_path = "output.xlsx"
    excel_loader.save(data, output_path)

    loaded_data = pd.read_excel(output_path)
    assert isinstance(loaded_data, pd.DataFrame)
    assert len(loaded_data) == len(data)
    assert list(loaded_data.columns) == list(data.columns)

    # Clean up the created output file
    import os
    os.remove(output_path)

def test_check_sheets(excel_loader):
    # Existing sheets
    sheet_names = ['How To', 'Bulkdatensammlung', 'SPA', 'SB', 'SD', 'KPIs', 'Dashboard', 'Auswertung']
    assert excel_loader.check_sheets(sheet_names) is True

    # Non-existing sheet
    invalid_sheet_names = ['InvalidSheet']
    assert excel_loader.check_sheets(invalid_sheet_names) is False
