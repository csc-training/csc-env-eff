---
topic: installing
title: Tutorial - Installing R applications and libraries
---

# R on Puhti and package installations

💬 A pre-installed R environment is available on Puhti.

1.  To check available module versions, run:

```bash
module spider r-env
```

{:start="2"}
2.  There are several ways to use R in `r-env` on Puhti:

    * Interactive jobs on a compute node, using either the R console or RStudio  
        💡 The easiest way to launch RStudio is through the Puhti web interface at [www.puhti.csc.fi](https://www.puhti.csc.fi/)
    * Non-interactive batch jobs
    * Interactively on the login node, using the R console (**only** for moving data, checking package availability, installing packages, no heavy jobs)

{:start="3"}
3. For example, to launch the R console in an interactive job, open a shell with `sinteractive` and then:

```bash
module load r-env
start-r
```

💡 See the [r-env documentation](https://docs.csc.fi/apps/r-env/) for further instructions on different ways to launch R on Puhti.

💬 It is also possible to [install R packages yourself](https://docs.csc.fi/apps/r-env/#r-package-installations).

* However, check first if what you need is already available in `r-env`. The module contains more than 1300 R packages! The easiest way to check if a package is available is trying to load it with the command `library(packagename)`.

## How to install an R package on Puhti

* Note that your own package installations are:
  * project-specific
  * R version-specific
  * located in the `/projappl` directory of your project

1.  On the command-line, create a folder for your R packages under `/projappl`:

```bash
# First navigate to /projappl/<project>, then
mkdir project_rpackages_<rversion>
```

{:start="2"}
2.  In R, add this folder to the list of directories where R will look for packages:

```r
.libPaths(c("/projappl/<project>/project_rpackages_<rversion>", .libPaths())) 
```

{:start="3"}
3. Assign `libpath` to point to this directory (not strictly necessary but can make life easier):

```r
libpath <- .libPaths()[1]
```

{:start="4"}
4.  Install the package (again, defining `lib = libpath` to specify the installation location is not strictly necessary but recommended)

```r
install.packages("packagename", lib = libpath)
```

{:start="5"}
5. Finished! The R package is now ready to be loaded and used.

💡 The package location is defined only for the current R session! R has to be reminded of the location at the start of every R session or script where you want to use the project-specific package by running the following command again:

```r
.libPaths(c("/projappl/<project>/project_rpackages_<rversion>", .libPaths())) 
```

💡 Instead of installing a missing package for your own project, you can ask for a module-wide installation for all users by contacting <servicedesk@csc.fi>.

## More information

💡 Read more about using R on Puhti in the [r-env documentation in Docs CSC](https://docs.csc.fi/apps/r-env/).
