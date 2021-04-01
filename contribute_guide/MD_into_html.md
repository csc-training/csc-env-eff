# Convert Markdown into html, preview, and publish

## Copy the Singularity tool image to Puhti. (*e.g.* in `$HOME/bin` which is used in the examples below)
   - Initialize Allas with project_2001659 (see below, works only for CSC staff)
   - `a-get pandocTool/pandoc.sif`
   - Give execute permissions `chmod u+x pandoc.sif`

## Copy the theme and other dependencies to local directory (in Puhti)

1. Go the the same directory as the source md files (= your git root directory for csc-env-eff in Puhti) (If you haven't yet cloned the repository, do so: git clone https://github.com/CSCfi/csc-env-eff). Note, this must be a subfolder in your $HOME.
2. Run command 
   ```bash
   singularity exec $HOME/bin/pandoc.sif /bin/sh -c "cp -r /slidetools/* ."
   ```
3. Now you can transform the md files to html faster and without font 
   embedding using simple command 
   ```bash
   $HOME/bin/pandoc.sif 01_my_lecture.md
   ```
4. To create a self contained html *slide* page add `-s` *i.e.* instead
   ```bash
   $HOME/bin/pandoc.sif -s 01_my_lecture.md
   ```
5. To create the whole site add your page to the top of the Makefile (located in: csc-env-eff/slides/Makefile) list and run `make`

Note, don't publish the theme and slidefactory accessory files, just the html (and related images etc.)!

## Speed up testing how the slides look like directly from Puhti

Start a local http server in Puhti and access slides with your browser

1. Go to the directory with html files (*i.e.* your csc-env git root) and run command 
   ```
   python3 -m http.server 80XX
   ```
   , where XX is some random number. 
   If the port is already in use, choose another one. Note that this example works 
   with default system python, so make sure that you are not using any conda or python modules.
   **Note, this is an unencrypted link, don't view anything private!**
2. Launch another ssh session with local port forwarding 
   ```
   ssh -L 80XX:localhost:80XX <your username>@puhti-login2.csc.fi
   ````
   where XX is the port from step 1. and 
   login node name must match also with step 1. command.
3. Open up the pages in your local browser with a link to `http://localhost:80XX`
4. When done, please remember to shut down the server and release the port! (ctrl-c in the python3 screen does this)

## Publish html files in Allas

1. [Initialise Allas access](https://docs.csc.fi/data/Allas/using_allas/a_commands/) with 
   ```bash
   module load allas
   allas-conf project_2001659
   ```
2. Publish your slides
   - Note, `a-publish` is recursive, so if you want only some subfolder, `cd` there first.
     Leave the *csc-env* bucket for the full repository and master branch only.
   ```bash
   a-publish -b my-csc-env 0X_cool_chapter.html
   ```
   - `a-publish` will echo the url, which in this case would be *https://a3s.fi/my-csc-env/0X_cool_chapter.html*
   
   ## Link the files in e-Lena
   
   To nicely link the files in e-Lena, choose "+Add an activity or resource" -> URL -> Write the name "Slides: Topic name" and copy the Allas URL for the slides. You can write in the Description the link to github page also. Then under Appearance choose "display" = embed.

