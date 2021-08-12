# Test Driven Development: TDD Bowling-Python

* Run `tdd.sh` to continuously run the test
* It will report errors in `RED`
* or it will report `Clear!` in `Green` when all is well!

## Useful commands:
* coverage run --source ./ -m unittest discover tests
* coverage html
* open htmlcov/index.html

## Starter Kit

* the `starter_kit` folder contains a bare-minimum to get started
* a `tests` folder with a single test case in it: `tests/test_bowling.py`
* `tdd.sh` - a script to continuously run your test case

# RED/GREEN/BLUE MODE
* proceed to cycle through the three modes of Test Driven Development:
* RED mode - create a failing unit test
* GREEN mode - create the code to turn your `RED` failing test to `GREEN`
* BLUE mode - refactor - that's your reward for a clean test

## RED mode - create a failing unit test
* `cd` into the `starter_kit` folder
* start by running `tdd.sh`
* You will see an error `ModuleNotFoundError: No module named 'Bowling'`

## GREEN mode - create the code to turn your `RED` failing test to `GREEN`
* Now, create your `Bowling.py` file with your `Bowling` class in it
``` Python
class Bowling:
    def __init__(self):
        pass
```
* once you have created that, the `tdd.sh` should start showing `Clear!`

## BLUE mode - refactor - that's your reward for a clean test
* refactor your `Bowling` class to be clean and beautiful
* refactor your `unit tests` too!
* Remember: Unit Tests are as important as production code - keep them clean

## REPEAT
* now that you've done one full cycle:
* Create a new failing test (`RED` mode)
* Create the code to satisfy the test (`GREEN` mode)
* Refactor like a banshee (`BLUE` mode)