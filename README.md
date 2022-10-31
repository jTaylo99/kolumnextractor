# KolumnExtrActor

The goal of KolumnExtrActor (KEA) is to provide an easy to use interface to read different types of files by providing a filepath with optional columns and conditions for
said columns.

KEA will allow functionality to specify which of the columns in the file should be read in. It also allow the specification of the type and format of the data in each of these columns. For example, it could be a specified that a column is a Number, between 1 and 100.

## Requirements

Python 3.10 or above.  
Packages in requirements.txt  
git
## Run Tests
```bash
    pip install -r requirements.txt
    pytest
```

## Contributing

This is a new project to help developers learn how to contribute to open-source! If you want to help, raise an issue you think will add to this project in a positive way and we will review it.

When contributing aim to keep to the Google Python Styleguide as our standard: https://google.github.io/styleguide/pyguide.html

## Examples

Below are several examples of how to make use of this package.

### Reading in specific columns
To do this we create a new class based on the `Data` class. We specify the columns of this with a Dictionary of normalised column names and None in the validator.
```python
    from data_holder import Data
    from validation import Number
    from kolumnextractor import reading_data

    class Name(Data):
        _columns = {"column2": None,
                    "column1": None,
                    "column3": None,}
    test = reading_data(filepath="test.csv", columns=Name)
```


### Read in columns where values must be numbers between upper and lower bounds
To do this we create a new class based on the `Data` class. We specify the columns of this with a Dictionary of normalised column names and Number valiators. The number validator has a min and max value specified.
```python
    from data_holder import Data
    from validation import Number

    class Name(Data):
        _columns = {"column2": Number(minvalue=1, maxvalue=100),
                    "column1": Number(minvalue=1, maxvalue=100),
                    "column3": Number(minvalue=1, maxvalue=100),}
    test = reading_data(filepath="test.csv", columns=Name)
```
