import argparse
import logging
from excel_loader import ExcelLoader

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Load, check, and save an Excel file.')
    parser.add_argument('--input', required=True, help='Path to the input Excel file.')
    parser.add_argument('--output', required=True, help='Path to the output Excel file.')
    args = parser.parse_args()

    loader = ExcelLoader(args.input)
    data = loader.load()
    loader.save(data, args.output)

if __name__ == '__main__':
    main()
