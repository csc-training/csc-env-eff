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

### Example: Installing a simple package with pip

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

💡 This time there's no error message, indicating that the import was successful.

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

## Example: Containerizing a Conda environment with Tykky

💬 Let's create a containerized Conda environment using the Tykky wrapper.

1. Create a folder under your project's `/projappl` directory for the installation, e.g.:

```bash
mkdir -p /projappl/<project>/$USER/tykky-env    # replace <project> with your CSC project, e.g. project_2001234
```

{:start="2"}
2. Create an `env.yml` environment file defining the packages to be installed. Using for example `nano`, copy/paste the following contents to the file:

```yaml
channels:
  - conda-forge
dependencies:
  - python=3.10.8
  - scipy
  - pandas
  - nglview
```

{:start="3"}
3. Purge your current module environment and load the Tykky module:

```bash
module purge
module load tykky
```

{:start="4"}
4. Create and containerize the Conda environment using the `conda-containerize` command:

```bash
conda-containerize new --prefix /projappl/<project>/$USER/tykky-env env.yml    # replace <project> with your CSC project, e.g. project_2001234
```

☝🏻 This process can take several minutes so be patient.

{:start="5"}
5. As instructed by Tykky, add the path to the installation `bin` directory to your `$PATH`:

```bash
export PATH="/projappl/<project>/$USER/tykky-env/bin:$PATH"    # replace <project> with your CSC project, e.g. project_2001234
```

💡 Adding this to your `$PATH` allows you to call Python and all other executables installed by Conda in the same way as you had activated a non-containerized Conda environment.

💭 The above Conda installation creates more than 40k files if installed directly on the parallel file system. Containerizing the environment with Tykky decreases this to less than 200, thus avoiding Lustre performance issues.

💬 To modify an existing Tykky-based Conda environment you can use the `update` keyword of `conda-containerize` together with the `--post-install` option to specify a bash script with commands to run to update the installation. [See more details in Docs CSC](https://docs.csc.fi/computing/containers/tykky/).
