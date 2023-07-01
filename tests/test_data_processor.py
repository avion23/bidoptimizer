import pandas as pd
import numpy as np
from src.data_processor import DataProcessor

def test_calculations():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'columnA': [4, 9, 16],
        'columnB': [2, 3, 4]
    })

    # Initialize the DataProcessor
    processor = DataProcessor(df)

    # Perform the calculations
    result_df = processor.process()

    # Validate the results
    assert (result_df['column1'] == df['columnA'] * df['columnB']).all()
    assert (result_df['column2'] == np.sqrt(df['columnA'])).all()
