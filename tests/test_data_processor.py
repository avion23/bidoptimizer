import pandas as pd
import numpy as np
from src.data_processor import DataProcessor

def test_calculations():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'Clicks': [4, 9, 16],
        'Spend': [2, 3, 4]
    })

    # Initialize the DataProcessor
    processor = DataProcessor(df)

    # Perform the calculations
    result_df = processor.process()

    # Validate the results
    assert (result_df['Bid'] == df['Clicks'] * df['Spend']).all()
    assert (result_df['Aktualitätsindex'] == np.sqrt(df['Spend'])).all()
