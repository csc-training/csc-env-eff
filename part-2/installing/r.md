---
layout: default
title: Installing R application and libraries
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/installing/installing_hands-on_r.html
---

# R on Puhti and package installations

> This tutorial is done on **Puhti**, which requires that:
  - You have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
  - Your account belongs to a project [that has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

💬 A pre-installed R environment is available on Puhti.

1. To check available module versions, run:

    ``` bash
    module spider r-env
    ```

2. There are several ways to use R in `r-env` on Puhti:
   - Interactive jobs on a compute node, using either the R console or RStudio  
     💡 The easiest way to launch RStudio is to use the Puhti web interface at
     [www.puhti.csc.fi](https://www.puhti.csc.fi/)
   - Non-interactive batch jobs
   - Interactively on the login node, using the R console (**only** for moving
     data, checking package availability, installing packages)

   For example, to launch the R console in an interactive job, open a shell
   with `sinteractive` and then

   ``` bash
   module load r-env
   start-r
   ```

💡 See the [r-env documentation](https://docs.csc.fi/apps/r-env/) for further
instructions on different ways to launch R on Puhti.

💬 It is also possible to
[install R packages yourself](https://docs.csc.fi/apps/r-env/#r-package-installations).

☝🏻 However, check first if what you need is already available in `r-env`. The
module contains more than 1300 R packages! The easiest way to check if a
package is available is trying to load it with the command
`library(packagename)`.

## How to install an R package on Puhti

- Note that your own package installations are:
  - project specific
  - R version specific
  - located in the `/projappl` directory of your project

1. Create a folder for your R packages in `/projappl` (open a login node shell
   in the [Puhti web interface](https://www.puhti.csc.fi/) or log in to Puhti
   with SSH):

   ``` bash
   cd /projappl/<project>  # replace <project> with your CSC project, e.g. project_2001234
   mkdir project_rpackages_<rversion>
   ```

2. Start an R session:
   1. Launch RStudio in the [Puhti web interface](https://www.puhti.csc.fi/)
   2. ... or launch the R console in an interactive shell session:
      ```bash
      sinteractive 
      module load r-env
      start-r
      ```
3. In R, add the folder you created above to the list of directories where R
   will look for packages:

   ``` r
   .libPaths(c("/projappl/<project>/project_rpackages_<rversion>", .libPaths())) 
   ```

4. Assign `libpath` to point to this directory (not strictly necessary, but can
   make life easier):

   ``` r
   libpath <- .libPaths()[1]
   ```

5. Install the package (again, defining `lib = libpath` to specify the
   installation location is not strictly necessary, but recommended):

   ``` r
   install.packages("packagename", lib = libpath)
   ```

6. For example, you can try installing a package called `beepr` with:

   ``` r
   install.packages("beepr", lib = libpath)
   ```

7. Finished! The R package is now ready to be loaded and used. Try loading
   `beepr` with `library(beepr)`.

💡 The package location is defined only for the current R session! R has to be
reminded of the location at the start of every R session or script where you
want to use the project-specific package by running this command again:

``` r
.libPaths(c("/projappl/<project>/project_rpackages_<rversion>", .libPaths())) 
```

💡 Instead of installing a missing package for your own project, you can ask
for a module-wide installation for all users by contacting
[CSC Service Desk](mailto:servicedesk@csc.fi).

## More information

💡 Docs CSC: Read more about using R on Puhti in our
[r-env documentation](https://docs.csc.fi/apps/r-env/).
