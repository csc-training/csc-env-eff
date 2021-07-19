---
topic: installing
title: Tutorial - Installing Perl applictions and libraries
---

# Perl

💬 Perl scripts and applications do not need installation. They can 
be simply downladed and run.

💬 To run Perl applications it usually best to first load a perl module. 
There is a system perl installation that it is available without any modules, but it is very barebones and is missing many commonly used libraries.

- To check available versions, use:
```bash
module spider perl
```
- By default the version `5.30.0`is loaded (19-07-21):
```bash
module load perl
```

💬 To make sure the applications uses the intended perl after loading a module you should either call it with perl:
```bash
perl my_app.pl
```
or make sure the shebang line of the script is:
```bash
#!/usr/bin/env perl
```

## Perl modules

💬 Sometimes the applications may require additional modules to run. These `perl modules`, should not be confused with the software modules in CSC computers.

💬 You should check the installation instructions for each module. For
libraries in CPAN, the easiest method is to use `cpanm`.

🗯 By default `cpanm` tries to install to perl installation location, so we need to first tell it where to install. This can be done by setting a few environment variables.
- Substitute the desired path for PERL_BASE and run the following:
```bash
export PERL_BASE="/projappl/project_2004306/YOURUSERNAME/myperl"   # an example path
export PERL_MM_OPT="INSTALL_BASE=$PERL_BASE"
export PERL_MB_OPT="--install_base $PERL_BASE"
export PERL5LIB="$PERL_BASE/lib/perl5"

cpanm library_name
```

FIXME: An error message is displayed after `cpanm library_name`:
```bash
! Finding library_name on cpanmetadb failed.
! Finding library_name () on mirror http://www.cpan.org failed.
! Couldn't find module or a distribution library_name
```

To use your own perl packages, you need to make sure they are 
included in perl `@INC`

There are three main ways to do it:
1. Inlude command line option -I (capital i) with the path on the command line:
```bash
perl -I /projappl/project_12345/myperl ./my_app.pl
```
2. Include the path in `$PERL5LIB` environment variable.
```bash
export PERL5LIB=/projappl/project_12345/myperl:${PERL5LIB}
```
3. Iclude the path in the perl code with `use lib`
```bash
    use lib '/projappl/project_12345/myperl';
    use My::Module;
```
## Bioperl
If your code requires bioperl, we have a bioperl installation available.

See our [biperl documentation](https://docs.csc.fi/apps/bioperl/) for details.

# Example

In this example we add perl module JSON to our own environment.

Let's start by loading perl module
```bash
module load perl/5.30.0
```
Then we can check if JSON is already available:
```bash
perl -e 'use JSON;'
```
We get an error message indicating that it is not found, so we need to install it.

First we need to set the installation location. It needs to be directory where 
you have write access. It could be e.g. your projects /projappl directory:
```bash
export PERL_BASE="/projappl/project_12345/local_perl"
export PERL_MM_OPT="INSTALL_BASE=$PERL_BASE"
export PERL_MB_OPT="--install_base $PERL_BASE"
```
We can now install the module. In this case it is in CPAN, so we can use cpanm:
```bash
cpanm JSON
```
To use it, we need to tell perl where to find it. In this case we set $PERL5LIB
environment variable: 
```bash
export PERL5LIB="/projappl/Project_12345/local_perl/lib/perl5"
```
We can now try it again:
```bash
perl -e 'use JSON;'
```
This time we do not get an error message indicating that JSON module is now usable.

The installation only needs to be done once, but you need to make sure $PERL5LIB
is set correctly each time you try to use this module.