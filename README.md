# BidOptimizer

BidOptimizer is a Python application designed to process Excel files. It loads an input Excel file, performs predefined calculations, and outputs the processed data back into an Excel file.

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Running Tests](#running-tests)
5. [Contributing](#contributing)
6. [License](#license)

## Overview <a name="overview"></a>

BidOptimizer works with an Excel file containing several sheets. The application specifically reads data from the 'Bulkdatensammlung' sheet, performs calculations on certain columns and produces an output file. The application is built with object-oriented principles and uses packages such as pandas and openpyxl for handling Excel data.

Development follows a test-driven development approach: all new functionality must include corresponding tests in the `tests` directory.

## Installation <a name="installation"></a>

1. Clone the repository:

   ```bash
   git clone https://github.com/avion23/bidoptimizer
   ```

2. Navigate to the project root directory (where `setup.py` is located).
3. Install the project and its dependencies using pip:

   ```bash
   pip install .
   ```

## Usage <a name="usage"></a>

After installation, you can run the application from the command line with:

```bash
python -m src.main --input <path-to-input-excel-file> --output <path-to-output-excel-file>
```

Replace `<path-to-input-excel-file>` with the path to your input Excel file, and `<path-to-output-excel-file>` with the path where you want to save the output Excel file. The program will then load the data, perform the necessary calculations and save the result to the output file.

## Running Tests <a name="running-tests"></a>

To run the tests, navigate to your project root directory and execute:

```bash
pytest tests/
```

or

```bash
python3 -m pytest
```

This will run all the test cases defined in the `tests` directory.

## Contributing <a name="contributing"></a>

1. Fork the repository.
2. Clone the forked repository to your local machine:

   ```bash
   git clone <forked-repo-url>
   ```

   Replace `<forked-repo-url>` with the URL of your forked repository.

3. Make changes in the cloned repository.
4. Commit the changes:

   ```bash
   git add .
   git commit -m "Your meaningful commit message"
   ```

5. Push the changes to your forked repository:

   ```bash
   git push
   ```

6. Create a pull request with your changes.

## License <a name="license"></a>
