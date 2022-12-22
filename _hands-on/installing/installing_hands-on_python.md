---
topic: installing
title: Tutorial - Installing Python applications and libraries (essential)
---

# Python

💬 To run Python applications, first load a suitable Python module. CSC has several Python environments available with focus on different application areas, e.g. data science and bio-/geoinformatics.

💡 For details, please see the [Python page](https://docs.csc.fi/apps/python/) in Docs CSC.

💭 By selecting a suitable Python environment to start with, you'll minimize the need to install additional packages.

☝🏻 Note that Conda environments should be containerized according to our [usage policy](https://docs.csc.fi/computing/usage-policy/#conda-installations). See the [Tykky container wrapper](https://docs.csc.fi/computing/containers/tykky/) to accomplish this easily!

## Installing Python packages

💬 To install simple packages it is usually enough to use `pip`, for example:
```bash
pip install --user <package name>   # Or pip3 to ensure use of Python 3
```

☝🏻 Remember to include `--user`. By default, `pip` tries to install to the system Python installation path, which will not work.

🗯 For more complex installations you should create a [containerized environment](https://docs.csc.fi/computing/containers/tykky/).

💡 See the the [Python documentation](https://docs.csc.fi/apps/python/) pages for each Python environment as there might be some environment-specific instructions.

## Example

💬 Let's install a library called `coverage`.

1. Start by loading a Python module and checking if the library is already installed.

```bash
module load python-data
python -c "import coverage"
```

☝🏻 The error message is indicating that the library is not available:

```bash
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'coverage'
```

{:start="2"}
2. Install the missing library:

```bash
pip3 install --user coverage    # This may take a while - don't worry!
```

{:start="3"}
3. Re-test if the library is available:

```bash
python -c "import coverage"
```

💡 This time there's no error message, indicating that the import was succesful.

{:start="4"}
4. User libraries are installed by default under `$HOME/.local`. To change the installation folder:

```bash
export PYTHONUSERBASE=/path/to/your/preferred/installdir
```

{:start="5"}
5. To uninstall:

```bash
pip3 uninstall coverage
```

{:start="6"}
6. Type `y` to confirm.
