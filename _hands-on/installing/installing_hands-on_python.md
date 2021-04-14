---
topic: installing
title: Tutorial - Installing Python applications and libraries
---

# Python

To run Python applications, first load suitable Python module. CSC
has several Python environments available, with focus on different
application areas.

For details, please see the [Python page](https://docs.csc.fi/apps/python/)
in Docs.

By selecting a suitable Python environment to start with, you'll minimize
the need to install additional packages.

## Installing Pyton packages.

To install simple packages it is usually enough to use `pip`:
```text
pip install --user package_to_install
```
Remember to include `--user`. By default pip tries to install to the common Python 
installation location, and this will not work.

For more complex installations it is preferable to create a virtual environment. 

See instructions in our [Python documentation](https://docs.csc.fi/apps/python/).

Also see the the pages for each Python environment so see any environment specific
instructions.

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