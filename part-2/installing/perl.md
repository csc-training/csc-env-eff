---
layout: default
title: Installing Perl applications and libraries
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 5
has_children: false
has_toc: false
permalink: /hands-on/installing/installing_hands-on_perl.html
---

# Perl

💬 Perl scripts and applications do not need installation. They can be simply
downloaded and run.

💬 To run Perl applications, it's usually best to first load a Perl module.

☝🏻 A system Perl installation is available (without a module), but it is very
bare-bones and is missing many commonly used libraries.

1. To check available module versions, use:

   ```bash
   module spider perl
   ```

2. The current default version is `5.34.1` and can be loaded with:

   ```bash
   module load perl
   ```

3. To ensure scripts use the intended Perl version after loading a module you
should either call the script with `perl`:

   ```bash
   perl my_app.pl
   ```

4. or make sure the shebang line of the script is:

   ```bash
   #!/usr/bin/env perl
   ```

## Installing Perl modules

💬 Sometimes applications may require additional modules to run.

- These "Perl modules", should not be confused with the software modules on CSC
  supercomputers.

💬 You should check the installation instructions for each module. For
libraries in CPAN, the easiest method is to use `cpanm`.

- You can check out the
  [CPAN documentation here](https://metacpan.org/dist/App-cpanminus/view/bin/cpanm).

### In this example, we'll add the Perl module JSON to our own environment

1. Check if JSON is already available:

   ```bash
   perl -e 'use JSON;'
   ```

   - The error message indicates that it is not found, so you need to install
     it.

   🗯 By default, `cpanm` tries to install new modules to the Perl installation
   path, which will not work.

   - You need to set the location to a directory where you have write access.
     It could be e.g. your project's `/projappl` directory.
   - This is accomplished by setting a few environment variables.

2. Replace the desired path for `PERL_BASE` and run the following:

   ```bash
   export PERL_BASE="/projappl/<project>/$USER/myperl"  # replace <project> with your CSC project, e.g. project_2001234
   export PERL_MM_OPT="INSTALL_BASE=$PERL_BASE"
   export PERL_MB_OPT="--install_base $PERL_BASE"
   export PERL5LIB="$PERL_BASE/lib/perl5"
   mkdir -p $PERL_BASE
   ```

3. You can now install the module. In this case, it is in CPAN, so you can use
   `cpanm`:

   ```bash
   cpanm JSON
   ```

4. To use the module, you need to tell Perl where to find it. In this case, you
   can set the `$PERL5LIB` environment variable (already done above):

   ```bash
   export PERL5LIB="/projappl/<project>/$USER/myperl/lib/perl5"  # replace <project> with your CSC project, e.g. project_2001234
   ```

5. You can now try again:

   ```bash
   perl -e 'use JSON;'
   ```

   - This time there's no error message, indicating that the JSON module is now
     available.

## Additional info

💬 The installation only needs to be done once, but you need to always ensure
Perl knows where to find the installed modules.

💭 There are three main ways to do this (we used the second already).

### Option 1

- Pass the path using the command-line option `-I`:

  ```bash
  perl -I /projappl/<project>/$USER/myperl/lib/perl5 ./my_app.pl  # replace <project> with your CSC project, e.g. project_2001234
  ```

### Option 2

- Include the path in the `$PERL5LIB` environment variable:

  ```bash
  export PERL5LIB=/projappl/<project>/$USER/myperl/lib/perl5:$PERL5LIB  # replace <project> with your CSC project, e.g. project_2001234
  ```

### Option 3

- Include the path in your Perl script with `use lib`:

  ```bash
  use lib '/projappl/<project>/$USER/myperl/lib/perl5';
  use My::Module;
  ```

## Bioperl

💬 If you need the BioPerl collection of Perl modules, you can find this
pre-installed on Puhti (try `module spider bioperl`).

💡 See our [BioPerl documentation](https://docs.csc.fi/apps/bioperl/) for more
details.
