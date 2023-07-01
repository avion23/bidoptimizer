
BidOptimizer
============

BidOptimizer is a Python application designed to process Excel files. It loads an input Excel file, performs predefined calculations, and outputs the processed data back into an Excel file.

Table of Contents
-----------------

1.  [Overview](#overview)
2.  [Installation](#installation)
3.  [Usage](#usage)
4.  [Running Tests](#running-tests)
5.  [Contributing](#contributing)
6.  [License](#license)

Overview <a name="overview"></a>
--------------------------------

BidOptimizer works with an Excel file containing several sheets. The application specifically reads data from the 'Bulkdatensammlung' sheet, performs calculations on certain columns and produces an output file. The application is built with object-oriented principles and uses packages such as pandas and openpyxl for handling Excel data.

Development follows a test-driven development approach: all new functionality must include corresponding tests in the `tests` directory.

Installation <a name="installation"></a>
----------------------------------------

1.  Clone the repository:
    
    bashCopy code
    
    `git clone https://github.com/avion23/bidoptimizer`
    
2.  Navigate to the project root directory (where `setup.py` is located).
    
3.  Install the project and its dependencies using pip:
    
    bashCopy code
    
    `pip install .`
    

Usage <a name="usage"></a>
--------------------------

After installation, you can run the application from the command line with:

bashCopy code

`python -m src.main --input <path-to-input-excel-file> --output <path-to-output-excel-file>`

Replace `<path-to-input-excel-file>` with the path to your input Excel file, and `<path-to-output-excel-file>` with the path where you want to save the output Excel file. The program will then load the data, perform the necessary calculations and save the result to the output file.

Running Tests <a name="running-tests"></a>
------------------------------------------

To run the tests, navigate to your project root directory and execute:

bashCopy code

`pytest tests/`

or

bashCopy code

`python3 -m pytest`

This will run all the test cases defined in the `tests` directory.

Contributing <a name="contributing"></a>
----------------------------------------

We follow the "[GitHub Flow](https://guides.github.com/introduction/flow/index.html)" workflow:

1.  Create a new branch for your feature or bugfix:
    
    bashCopy code
    
    `git checkout -b your-feature-or-bugfix-branch`
    
2.  Make your changes in the new branch.
    
3.  Commit your changes:
    
    bashCopy code
    
    `git add . git commit -m "Your meaningful commit message"`
    
4.  Push your changes to the remote repository:
    
    bashCopy code
    
    `git push origin your-feature-or-bugfix-branch`
    
5.  [Create a Pull Request](https://github.com/avion23/bidoptimizer/compare) from your branch to the `main` branch in the repository.
    

You can then assign another team member to review your Pull Request. Once it's reviewed and all changes are approved, it can be merged into the `main` branch.

License <a name="license"></a>
------------------------------