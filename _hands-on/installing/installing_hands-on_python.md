---
topic: installing
title: Tutorial - Installing Python applications and libraries
---

# Python

To run Python applications, first load suitable Python module. You can check 
available modules with e.g.:
```text
module spider python
```
- `python-env` is a general purpose Python installation
- `python-data` includes commonly used packages for data analysis and machine learning

To install simple packages it is usually enough to use:
```text
pip install --user package_to_install
```
Remember to include `--user`. By default pip tries to install to the common Python 
installation location, and this will not work.

For more complex installations it is preferable to create a virtual environment. 

See instructions in our [python-data documentation](https://docs.csc.fi/apps/python-data/).
The same instructions work also for the `python-env` module.

## Biopython
For applications requiring Biopython we have two options:

First option using `biopythontools` module:
```text
module load biokit
module load biopythontools
```
With this option use `pip install --user` as above.

Second option activates a virtual environment with biopython (substitute your project name):
```text
export PROJAPPL=/projappl/project_12345
module load bioconda
biopython-env
```
See our [Biopython documentation](https://docs.csc.fi/apps/biopython/) for more details.

## Example
We need library `coverage`.

Let's start by loading a Python module and checking if the library is already installed.
```text
module load python-env
python -c "import coverage"
```
We receive an error message indicating that the library is not available:
```text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'coverage'
```
Let's install the missing library:
```text
pip install --user coverage
```
We can now re-test if the library is available:
```text
python -c "import coverage"
```
This time we don't get and error message, indicating the import command was succesful-

The library is installed in directory `$HOME/.local`

To uninstall:
```text
pip uninstall coverage
```