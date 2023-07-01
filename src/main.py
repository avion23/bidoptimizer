import argparse
import logging
from excel_loader import ExcelLoader
from data_processor import DataProcessor

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Process an Excel file with predefined calculations.')
    parser.add_argument('--input', required=True, help='Path to the input Excel file.')
    parser.add_argument('--output', help='Path to the output Excel file. If not provided, the input file will be overwritten.')
    args = parser.parse_args()

    if args.output is None:
        args.output = args.input

    loader = ExcelLoader(args.input)
    data = loader.load()
    if data is None:
        logger.error('Data could not be loaded. Exiting...')
        return
    processor = DataProcessor(data)
    processed_data = processor.process()

    loader.save(processed_data, args.output)


if __name__ == '__main__':
    main()
