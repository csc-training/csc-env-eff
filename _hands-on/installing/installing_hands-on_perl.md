---
topic: installing
title: Tutorial - Installing Perl applictions and libraries
---

# Perl

💬 Perl scripts and applications do not need installation. They can 
be simply downladed and run.

💬 To run Perl applications it usually best to first load a perl module.  

☝🏻 *There is a system perl installation that it is available without any modules, but it is very barebones and is missing many commonly used libraries.*

1. To check available versions, use:
    ```bash
    module spider perl
    ```
2. By default the version `5.30.0`is loaded (19-07-21):
    ```bash
    module load perl
    ```

☝🏻 To make sure the applications uses the intended perl after loading a module you should either call it with perl:
```bash
perl my_app.pl
```
or make sure the shebang line of the script is:
```bash
#!/usr/bin/env perl
```

## Installing Perl modules

💬 Sometimes the applications may require additional modules to run. 
- These `perl modules`, should not be confused with the software modules in CSC computers.

💬 You should check the installation instructions for each module. For
libraries in CPAN, the easiest method is to use `cpanm`. 
- You can check out [CPAN docs here.](https://metacpan.org/dist/App-cpanminus/view/bin/cpanm).

### In this example we add perl module JSON to our own environment

1. Check if JSON is already available:
    ```bash
    perl -e 'use JSON;'
    ```
    - The error message indicates that it is not found, so you need to install it.

🗯 By default `cpanm` tries to install to perl installation location.   
- You need to set the location to a directory where you have write access instead. It could be e.g. your project's /projappl directory. 
- This can be done by setting a few environment variables:

{:start="2"}
2. Substitute the desired path for PERL_BASE and run the following:
    ```bash
    export PERL_BASE="/projappl/project_xxxx/yourcscusername/myperl"   # an example path
    export PERL_MM_OPT="INSTALL_BASE=$PERL_BASE"
    export PERL_MB_OPT="--install_base $PERL_BASE"
    export PERL5LIB="$PERL_BASE/lib/perl5"
    ```
3. You can now install the module. In this case it is in CPAN, so you can use `cpanm`:
    ```bash
    cpanm JSON
    ```

4. To use it, you need to tell perl where to find it. In this case you can set `$PERL5LIB` environment variable: 
    ```bash
    export PERL5LIB="/projappl/project_xxxx/yourcscusername/myperl/lib/perl5"
    ```
5. You can now try again:
    ```bash
    perl -e 'use JSON;'
    ```
    - This time there's no error message which indicates that JSON module is now usable.

## Additional info

💬 The installation only needs to be done once, but you need to make sure perl knows where to find the installed modules.

💭 There are three main ways to do this (we used the second already):

**Option 1.**  
1. Inlude command line option -I (capital i) with the path on the command line:
    ```bash
    perl -I /projappl/project_xxxx/yourcscusername/myperl/lib/perl5 ./my_app.pl
    $HOME
    ```

**Option 2.**  
1. Include the path in `$PERL5LIB` environment variable.
    ```bash
    export PERL5LIB=/projappl/project_xxxx/yourcscusername/myperl/lib/perl5:${PERL5LIB}
    ```

**Option 3.**  
1. Include the path in the perl code with `use lib`
    ```bash
    use lib '/projappl/project_xxxx/yourcscusername/myperl/lib/perl5';
    use My::Module;
    ```

## Bioperl
💬 If your code requires bioperl, we have a bioperl installation available.

💡 See our [bioperl documentation](https://docs.csc.fi/apps/bioperl/) for details.

