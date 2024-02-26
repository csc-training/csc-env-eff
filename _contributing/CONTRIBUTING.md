# Contributing

## Starting as a writer

**CSC staff:** Before starting, ask to be added to the
[csc-training](https://github.com/csc-training) GitHub organization.

The rest of this document describes the workflow in GitHub as well as
instructions for previewing and deploying the documentation. See the
[style guide](STYLEGUIDE.md) for content and formatting instructions.

## For the impatient (note: this will differ for CSC Staff and non-staff)

Once you've joined the csc-training organization:

* (Sign in to GitHub) and edit the content.
* Scroll down to commit changes, create a new branch (don't push directly to
  master) and then make a pull request (PR).
* Assign a reviewer or merge yourself if it's just a small thing.

Users who are not a member of the csc-training organization should
create pull requests from a fork of the repo.

## Making changes using pull requests

The csc-env-eff repository uses 'master' as the default branch. You can make
changes using the web GUI, command-line or desktop application.

The master branch is not protected. You can make changes to it directly,
**but please don't**. Instead, make a "feature branch" for your change and then
create a pull request.

### Overview

#### Writer:

- Create your own branch (or fork) from master (or work in an already existing branch,
  if agreed).
- Create/bring there the content you want to work with. Pay attention to file
  naming! Avoid overly complicated/long filenames.
- Create a pull request for your work to be added to master
    - Assign a reviewer if you want.
        - **Tip:** If editing slides, add a link to the HTML-page
          ([see instructions for publishing slides in Allas](MD_INTO_HTML.md/#publish-html-files-in-allas)).
    - Write meaningful commit messages, so it's easier for reviewers to do
      their job.
    - Communicate! Use 'WIP' (= Work In Progress) in your PR title if you don't
      wish the branch to be merged to master (i.e. you want to continue working
      with it).
- You can also merge the branch yourself, but please delete the feature branch
  afterwards.

#### Reviewer:

If you get a request to review a PR, please contribute to help publish the
changes!

- Edit the pages as needed (perhaps via the web GUI).
    - It's ok to edit typos directly in the text.
- **Tip:**
    - Suggest changes so that they appear as a `diff` in the conversation tab,
      so that the author can simply commit/reject them.
    - In the 'Files changed' tab, scroll to the line you want to change and
      press the blue '+' at the start of the line.
    - In the appearing pop-up, press the sim-card-look-a-like icon with + and -
      on top of each other.
    - Write between the ticks (including the suggestion) what you want to
      appear in the page.
    - If you want to remove a line, delete the content (leave the ticks and
      the word 'suggestion').
    - If you want to remove lines, write the preceding and trailing lines.
    - Write a comment outside the ticks, if you want, and use 'Preview' to see
      the resulting `diff`.
    - Press 'Add Single Comment'.
- Once you're happy with the content, in the 'Files changed' tab, click 'Review
  changes' and select 'Approve'.
- Anyone can be a reviewer.

### Making pull requests using the web GUI

In the master branch, navigate to the page you want to edit, click the pen-logo 
at the top right and once ready, at the bottom, choose 'Create new branch from
this commit and start a pull request'. Note that you can give the branch a
descriptive name at this point. If you wish to edit an already existing branch,
first change to the correct branch using the 'branch' button in the upper left,
next to the path to the file. If you found an error in the pull request of your
own branch, you should commit to it directly instead of creating another pull
request (the two choices at the bottom).

### Making pull requests using the command-line

#### Overview:

- Clone the repository (if not done already):
  `git clone https://github.com/csc-training/csc-env-eff.git`.
- Change to master branch (if not there already): `git checkout master`.
- Update your local repository: `git pull`.
- Create a new branch from the master branch: `git checkout -b my-new-branch`.
- Create content and `add` edited files in your new branch:
  `git add file1.md file2.md`.
    - **Hint:** Use `git add .` to add all modified files in current directory,
      including subdirectories.
- Commit your changes: `git commit -m 'short description'`.
- Check status (all files committed etc.): `git status`.
- Push changes to remote repository: `git push origin my-new-branch`.
- Open a pull request to merge changes from your new branch into the master
  branch.
- Ask a colleague to review and merge the changes.
