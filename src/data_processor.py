import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class DataProcessor:
    def __init__(self, df):
        self.df = df

    def calculate_bid(self):
        logger.debug("Starting bid calculation...")
        self.df['Bid'] = self.df['Clicks'] * self.df['Spend']  # Replace with actual calculation logic
        logger.debug("Bid calculation completed.")

    def calculate_aktualitaetsindex(self):
        logger.debug("Starting Aktualitätsindex calculation...")
        self.df['Aktualitätsindex'] = np.sqrt(self.df['Spend'])  # Replace with actual calculation logic
        logger.debug("Aktualitätsindex calculation completed.")

    def process(self):
        self.calculate_bid()
        self.calculate_aktualitaetsindex()
        return self.df
