import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, df):
        self.df = df

    def calculate_column1(self):
        self.df['column1'] = self.df['columnA'] * self.df['columnB']  # sample calculation

    def calculate_column2(self):
        self.df['column2'] = np.sqrt(self.df['columnA'])  # sample calculation

    def process(self):
        self.calculate_column1()
        self.calculate_column2()
        return self.df
