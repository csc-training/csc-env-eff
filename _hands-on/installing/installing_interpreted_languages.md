---
topic: installing
title: Tutorial - installing_interpreted_language
---

# Installing applications and libraries for Java, Perl, Python and R 

## Java
Java applications do not typically require special installation. You just need
to download the .jar file.

If you get an error message about java version, try loading a suitable java 
module. You can check the available modules with command:
```text
module spider java
```

Despite their name, modules named `biojava` are just normal java installations,
and can be used with any software, not just bio applications.

Some java applications fail to run on the login nodes. Try running them using
`sinteractive` instead. 

Naturally no compute heavy tasks should be run on the login nodes.

## Perl

To run Perl applications it usually best to first load a perl module.

To check available versions, use:
```text
module spider perl
```
To install and use your own perl packages, it usually enough to download them
to a suitable location and make sure they are included in perl `@INC`

There are three main ways to do it:
1. Inlude command line option -I (capital i) with the path on the command line:
```text
perl -I /projappl/project_12345/myperl ./my_app.pl
```
2. Include the path in `$PERL5LIB` environment variable.
```text
export PERL5LIB=/projappl/project_12345/myperl:${PERL5LIB}
```
3. Iclude the path in the perl code with `use lib`
```text
    use lib '/projappl/project_12345/myperl';
    use My::Module;
```
### Bioperl
If your code requires bioperl, we have a bioperl installation available.

See our [biperl documentation](https://docs.csc.fi/apps/bioperl/) for details.

## Python

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
Remember to include `--user`. By default it tries to install to Python install location,
and this will not work.

For more complex installations it is preferable to create a virtual environment. 

See instructions in our [python-data documentation](https://docs.csc.fi/apps/python-data/).
The same instructions work also for the `python-env` module.

### Biopython
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

## R

Puhti has several R version available as modules. You should start by checking
if one of these is suitable for you needs. 

To check available versions, use:
```text
module spider r-env
```
It is also possible to install your own R packages.

See the [r-env-singularity](https://docs.csc.fi/apps/r-env-singularity/) 
documentation for instructions.

