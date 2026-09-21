---
layout: default
title: Installing binary applications
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 1
has_children: false
has_toc: false
permalink: /hands-on/installing/installing_hands-on_binary.html
---

# Installing binary applications

> This tutorial is done on **Roihu**, which requires that:
  - You have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
  - Your account belongs to a project [that has access to the Roihu service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

💬 In some cases software developers offer ready-made binary versions of their
software.

- If the binary version runs, you don't need to compile the software yourself.

☝🏻 It should be noted that ready binary versions are typically not optimized
for CSC supercomputers.

- The performance difference will depend on the code and on how the application
  was compiled.
- Often the difference is just a few percent, but in some cases it can be more
  substantial.

‼️ Especially all MPI codes need to be compiled on the machine they will be run
on to ensure correct operation.

## Make the installation in your own folder in the `/projappl` directory of your project

1. Move to the `/projappl` directory of your project:

   ```bash
   cd /projappl/<project>   # replace <project> with your CSC project, e.g. project_2001234
   ```

2. If not done already, create your own folder under your project's `/projappl`
   directory:

   ```bash
   mkdir -p $USER
   ```

3. Move to your folder:

   ```bash
   cd $USER
   ```

## Example: Installing the TaxonKit software

💬 In this example we install the binary release of TaxonKit, a tool for
working with the NCBI taxonomy.

1. First check whether CSC already provides it:

   ```bash
   module spider taxonkit
   ```
   This returns "Unable to find: taxonkit", so we install it ourselves.

2. Find the software online. TaxonKit has a project website,
   [bioinf.shenwei.me/taxonkit](https://bioinf.shenwei.me/taxonkit/), and a
   [download page](https://bioinf.shenwei.me/taxonkit/download/) — this is how
   a researcher would normally find a tool that CSC does not provide.

3. On the download page, identify the Linux 64-bit build (`linux_amd64`).
   TaxonKit is a statically linked binary, so it has no library dependencies
   and runs on Roihu as-is.

4. Download the release (a `.tar.gz`, not a `.zip`):

   ```bash
   wget https://github.com/shenwei356/taxonkit/releases/download/v0.20.0/taxonkit_linux_amd64.tar.gz
   ```

5. Unpack it:

   ```bash
   tar -xzf taxonkit_linux_amd64.tar.gz
   ```
   This produces a single executable, `taxonkit`, in the current directory.

6. The download page says to install it with `sudo cp taxonkit /usr/local/bin/`.
   On a supercomputer you have no `sudo` rights and cannot write to system
   directories, so this does not work. We use `$PATH` instead.

7. The bare command fails — the shell does not yet know where the file is:

   ```bash
   taxonkit          # command not found
   ```

8. Run it with an explicit path — this always works:

   ```bash
   ./taxonkit version
   ```
   It prints the version, so the binary runs on Roihu.

   💡 To avoid typing the path every time, add this folder to your `$PATH`.

9. Add the current directory to `$PATH`:

   ```bash
   export PATH=$PWD:$PATH
   ```

10. Confirm the shell now finds it, then run it from anywhere:

    ```bash
    which taxonkit
    taxonkit version
    ```

💡 To actually resolve taxonomy (optional, not needed to complete this
tutorial), TaxonKit needs the NCBI taxonomy files in `$HOME/.taxonkit`:

```bash
wget https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz
mkdir -p $HOME/.taxonkit
tar -xzf taxdump.tar.gz -C $HOME/.taxonkit names.dmp nodes.dmp delnodes.dmp merged.dmp
echo 9606 | taxonkit lineage      # 9606 = Homo sapiens
```

## Some notes about `$PATH`

💡 `$PATH` is a list of directories, separated by `:`, that the shell searches
**in order** when you type a command name. It runs the first match it finds.
`export PATH=$PWD:$PATH` puts your directory at the front of that list, so it
is searched first.

💡 Always keep the existing `$PATH` in the value. If you write
`export PATH=$PWD` on its own, you erase the rest and normal commands (`ls`,
`cat`, …) stop working.

☝🏻 Order matters on a shared system. Look at your list:

```bash
echo $PATH
```

Your new folder now sits *ahead* of the directories that loaded modules add
(compilers, MPI, and other tools). Because your directory is searched first, a
file there would be used before a same-named tool from a module. This is
harmless for a uniquely named tool like `taxonkit`. But if you want to be sure
your own files can never override system or module tools, *append* your
directory instead, so it is searched last:

```bash
export PATH=$PATH:$PWD
```

Use the front position (`$PWD:$PATH`) only when you deliberately want your own
version of a tool to take priority over an installed one.

☝🏻 To set the path automatically in future sessions, add the `export` to
`$HOME/.bashrc`, using the full path instead of `$PWD`:

```bash
export PATH=/projappl/<project>/$USER:$PATH   # replace <project> with your CSC project, e.g. project_2001234
```

‼️ Editing `.bashrc` can conflict with applications pre-installed by CSC. It
runs in every shell and every batch job, so keep it minimal.

💭 If problems appear after changing your environment, restore the default
with the [`csc-env` command](https://docs.csc.fi/support/tutorials/using_csc_env/).
