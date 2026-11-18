# Convert Markdown into HTML, preview, and publish

## Open a shell on Roihu

The slides are built with a container on Roihu. You can use either:

- **The web interface (easiest):** log in at <https://www.roihu.csc.fi> with
  your CSC or Haka account and multi-factor authentication. On the dashboard,
  open the shell app under *Pinned Apps* (or *Tools* in the top bar) and
  choose the login node (Login node shell, Roihu-CPU) option. No SSH keys are needed. Keep the browser tab
  open while a command runs, as closing it stops the command.
- **SSH:** see [Connecting to CSC supercomputers](https://docs.csc.fi/computing/connecting/)
  for setting up SSH keys and certificates.

## Get the container image

Copy the container to `$HOME/bin`, which is used in the examples below. This
needs to be done only once.

```bash
mkdir -p $HOME/bin && cd $HOME/bin
wget https://a3s.fi/pandocTool/pandoc-env-eff.sif   # or: curl -L -o pandoc-env-eff.sif https://a3s.fi/pandocTool/pandoc-env-eff.sif
chmod u+x pandoc-env-eff.sif
```

> Alternatively, if you have initialized Allas with project_2001659 (works only
for CSC staff, see below), use `a-get pandocTool/pandoc-env-eff.sif`.

## Build the slides

1. Clone the repository (or the branch you are working on) and go to the
   `_slides` folder. The repository must be under your `$HOME`.

   ```bash
   cd $HOME
   git clone -b <branch-name> https://github.com/csc-training/csc-env-eff.git   # leave out -b <branch-name> for master
   cd csc-env-eff/_slides
   ```

2. Copy the theme files from the container into the folder:

   ```bash
   apptainer exec $HOME/bin/pandoc-env-eff.sif /bin/sh -c "cp -r /slidetools/* ."
   ```

3. Create a self-contained HTML slide page (`-t csc-eurocc-2019` selects the
   correct theme):

   ```bash
   $HOME/bin/pandoc-env-eff.sif -s -t csc-eurocc-2019 03_disk_areas.md
   ```

   Leave out `-s` for a faster build without embedded fonts and images.

4. To create the whole slide deck, add your page to the top of the Makefile
   at `csc-env-eff/_slides/Makefile` and run `make`.

> If the build above fails, try this alternative command. Copy the
container into the `_slides` folder first:
>
> ```bash
> apptainer exec -B $PWD pandoc-env-eff.sif /slidetools/convert.sh -s -t csc-eurocc-2019 03_disk_areas.md
> ```

> Note, don't publish the theme and slidefactory accessory files, just the
HTML. Note also that `a-publish` will not _overwrite_ files in Allas by
default, so you'll need to delete the old files in Allas
first.

## Preview the slides

The easiest way to preview the slides, and to share them with reviewers, is
to publish them in a test bucket in Allas (see below) and open the URL in your
browser. Add the URL to your pull request description.

Alternatively, if you connect with SSH, you can start a local HTTP server on
the login node and view the slides through SSH port forwarding:

1. Go to the directory with HTML files and run command:

   ```
   python3 -m http.server 80XX
   ```

   where XX is some random number. If the port is already in use, choose
   another one. Note that this example works with default system python, so
   make sure that you are not using any Tykky or other Python environment.
   **Note, this is an unencrypted link, don't view anything private!**
2. Check the login node name with `hostname` and launch another SSH session
   with local port forwarding to that same login node:

   ```
   ssh -L 80XX:localhost:80XX <username>@<login-node-name>
   ```

3. Open up the page in your local browser using URL `http://localhost:80XX`.
4. When done, please remember to shut down the server and release the port
   (ctrl-c in the python3 screen)!

## Publish HTML files in Allas

1. [Initialize Allas access](https://docs.csc.fi/data/Allas/using_allas/a_commands/)
   with:

   ```bash
   module load allas
   allas-conf project_2001659
   ```

2. Publish your slides:
   - Note, `a-publish` is recursive, so if you want only some subfolder, `cd`
     there first. Leave the *CSC_training* bucket for the full repository and
     master branch only.

     ```bash
     a-publish -b test-csc-env 0X_cool_chapter.html
     ```

   - `a-publish` will echo the URL, which in this case would be
     `https://a3s.fi/test-csc-env/0X_cool_chapter.html`.
     
3. If you need to update published slides

`a-publish` will not overwrite files that are already in Allas. To publish an
updated version, delete the old file first and then publish again:

```bash
a-delete test-csc-env/0X_cool_chapter.html
a-publish -b test-csc-env 0X_cool_chapter.html
```

The URL stays the same. (Don't use `a-put --override` for this: `a-put`
uploads the file as private, so the published URL stops working and shows an
`AccessDenied` error.)
     

## Link the files in eLena

To nicely link the files in eLena, choose "+Add an activity or resource" >
URL > Write the name "Slides: Topic name" and copy the Allas URL for the
slides. You can add in the Description the link to the GitHub page also.
Then, under "Appearance", choose "display" = embed.
