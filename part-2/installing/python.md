---
layout: default
title: Installing Python packages and environments
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 2
has_children: false
has_toc: false
permalink: /hands-on/installing/installing_hands-on_python.html
---

# Python

> This tutorial is done on **Puhti**, which requires that:
  - You have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
  - Your account belongs to a project [that has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

💬 To run Python applications, first load a suitable Python module. CSC has
several Python environments available with focus on different application
areas, e.g. [data science and machine learning](https://docs.csc.fi/apps/python-data/),
as well as [geoinformatics](https://docs.csc.fi/apps/geoconda/).

💡 For more details, please see the [Python page](https://docs.csc.fi/apps/python/)
in Docs CSC.

💭 By selecting a suitable Python environment to start with, you'll minimize
the need to install additional packages.

☝🏻 Note that Conda environments should be containerized according to our
[usage policy](https://docs.csc.fi/computing/usage-policy/#conda-installations).
Use the [Tykky container wrapper](https://docs.csc.fi/computing/containers/tykky/)
to accomplish this easily!

## Installing Python packages

💬 To install simple packages it is usually enough to use `pip`, for example:

```bash
pip install --user <package name>   # Or pip3 to ensure use of Python 3
```

☝🏻 Remember to include `--user`. By default, `pip` tries to install to the
system Python installation path, which will not work.

🗯 For more complex installations you should create a
[containerized environment](https://docs.csc.fi/computing/containers/tykky/).

💡 See the Docs CSC pages for each Python module for more details, as there may
be some environment-specific instructions.

### Example: Installing a simple package with `pip`

💬 Let's install a library called `coverage`.

1. Start by loading a Python module and checking if the library is already
   installed:

   ```bash
   module load python-data
   python -c "import coverage"
   ```

2. The error message is indicating that the library is not available:

   ```bash
   Traceback (most recent call last):
     File "<string>", line 1, in <module>
   ModuleNotFoundError: No module named 'coverage'
   ```

3. Install the missing library:

   ```bash
   pip3 install --user coverage  # This may take a while - don't worry!
   ```

4. Re-test to see if the library is now available:

   ```bash
   python -c "import coverage"
   ```

5. This time there's no error message, indicating that the import was
   successful!
6. User libraries are installed by default under `$HOME/.local`. It is a good
   idea to change the installation folder, as the space in `$HOME` is limited:

   ```bash
   export PYTHONUSERBASE=/path/to/another/installdir/  # /projappl is recommended
   ```

7. To uninstall the package:

   ```bash
   pip3 uninstall coverage
   ```

8. Type `y` to confirm.

‼️ Note, if the package you installed also contains executable files, i.e. a
command-line interface, these commands may not work as is! This is because the
Python modules provided by CSC are containerized and the user-installed
binaries will refer to an inaccessible Python path inside the container. For
workaround instructions, see our
[Python documentation](https://docs.csc.fi/apps/python/#installing-python-packages-to-existing-modules),
or install your own environment from the beginning inside a container as
outlined in the following example.

## Example: Containerizing a Conda environment with Tykky

💬 Let's create a containerized Conda environment using the Tykky wrapper.

1. Create a folder under your project's `/projappl` directory for the
   installation, e.g.:

   ```bash
   mkdir -p /projappl/<project>/$USER/tykky-env  # replace <project> with your CSC project, e.g. project_2001234
   ```

2. Create an `env.yml` environment file defining the packages to be installed.
   Using for example `nano`, copy/paste the following contents to the file:

   ```yaml
   channels:
     - conda-forge
   dependencies:
     - python=3.10.8
     - scipy
     - pandas
     - nglview
   ```

3. Purge your current module environment and load the Tykky module:

   ```bash
   module purge
   module load tykky
   ```

4. Create and containerize the Conda environment using the `conda-containerize`
   command:

   ```bash
   conda-containerize new --prefix /projappl/<project>/$USER/tykky-env env.yml  # replace <project> with your CSC project, e.g. project_2001234
   ```

   ☝🏻 This process can take several minutes so be patient.

5. As instructed by Tykky, add the path to the installation `bin` directory to
   your `$PATH`:

   ```bash
   export PATH="/projappl/<project>/$USER/tykky-env/bin:$PATH"  # replace <project> with your CSC project, e.g. project_2001234
   ```

💡 Adding this to your `$PATH` allows you to call Python and all other
executables installed by Conda in the same way as you had activated a
non-containerized Conda environment.

💭 The above Conda installation would create more than 40k files if installed
directly on the parallel file system. Containerizing the environment with Tykky
decreases this to less than 200, thus avoiding Lustre performance issues.

💬 To modify an existing Tykky-based Conda environment, you can use the
`update` sub-command of `conda-containerize` together with the `--post-install`
option to specify a bash script with commands to run to update the installation.
[See more details in Docs CSC](https://docs.csc.fi/computing/containers/tykky/).
