# Previewing the site locally

The <https://csc-training.github.io/csc-env-eff> site is built using *Jekyll* and
the *Just the Docs* theme. When developing new material (e.g. tutorials), it is
useful to build the site locally to preview the changes.

## Step 1. Install Jekyll

In order to build the site locally, you need to first install Jekyll on your
own computer. Detailed instructions for different operating systems are
available in the
[Jekyll documentation](https://jekyllrb.com/docs/installation/).

For Ubuntu 22.04, the steps are as follows:

1. Jekyll is a Ruby gem, so install Ruby and other prerequisites.
   ```bash
   sudo apt install ruby-full build-essential zlib1g-dev
   ```
2. Edit your `~/.bashrc` file to configure a local gem installation directory
   for your user.
   ```bash
   echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
   echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
   echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```
3. Install Jekyll and Bundler (used to manage and run gems).
   ```bash
   gem install jekyll bundler
   ```

## Step 2. Build the site locally

1. Open a Terminal.
2. Clone the csc-env-eff git repo.
   ```bash
   git clone https://github.com/csc-training/csc-env-eff.git
   ```
3. In the root directory, build the site and serve it on a local server.
   ```bash
   cd csc-env-eff
   bundle exec jekyll serve
   ```
4. **Note:** When doing this the first time, you will likely get an error about
   missing dependencies. Install them all.
   ```bash
   bundle install
   ```
   You might also get another error if you've installed Ruby v3.0.0 or newer.
   These versions do not ship with `webrick` and the solution is to add it to
   your dependencies manually.
   ```bash
   bundle add webrick
   ```
5. Re-run the `bundle exec jekyll serve` command and browse to
   <http://localhost:4000> to view the site.
