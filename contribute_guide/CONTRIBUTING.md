# Contributing

## Starting as a writer

CSC staff: do these two things _first_:

1. Join the Git organization [CSCfi](https://github.com/CSCfi) by sending email to vcs-support@csc.fi.
2. Then [join here the CSC employees team](https://github.com/orgs/CSCfi/teams/employees/members). Membership
gives you permissions to edit source files that build the content. (Wait for a confirmation email.)

The rest of this document describes the workflow in Github as 
well as instructions for previewing and deploying the documentation. 
See [Style guide](STYLEGUIDE.md) for content and formatting instructions.

## For the impatient (Note: this will differ for CSC Staff and non-staff)

Once you've completed the steps above:
* (sign in GitHub) and edit then content
* Scroll down to commit changes (create a new branch, don't push directly to master) -> make a pull request
* Assign a reviewer or merge yourself if it's a small thing

## Making changes using pull requests

The csc-env-eff repository uses the 'master' as the default
branch. You can make changes in web gui, command line or desktop application.

Master branch is not protected. You can make changes to it directly, but please
don't. Instead, make a "feature branch" for your change and then create a pull request.

### Overview
**writer:**

 - Create your own branch from master (or work in an already existing branch, if agreed)
 - Create / bring there the content you want to work with. Pay attention to file naming!
 - When creating a new exercise / tutorial add it to it's subfolder's README.md
 - Make a pull request for your work to be added to Master
    - Assign a reviewer if you want
        - **Tip** Add a link to the html-page ([see instructions for publishing the slides in Allas](MD_into_html.md/#publish-html-files-in-allas) )
    - Write meaningful pull request messages, so it is easier for reviewers to do their job.
    - Communicate! Use "WIP" (= Work In Progress) in your pull request title, if you don't wish the branch to be merged to master (i.e. you want to continue working with it).
 - You can also merge the branch yourself, but please delete the feature branch afterwards, if you no longer use it

**Reviewer:** If you get a request to review a pull request, please contribute to help publish the changes!

 - Edit the pages as needed (perhaps via the Web GUI)
     - It's ok to edit typos directly in the text
 - **Pro tip** 
      - Suggest changes so that they appear as `diff` in the conversation tab, so that the author can simply commit/reject them
      - In the "Files changed" tab, scroll to the line you want to change and press the blue "+" at the start of the line
      - In the appearing pop-up, press the sim-card-look-a-like icon with + and - on top of each other
      - write between the tics (including the suggestion) what you want to appear in the page
      - If you want to remove a line, delete the content (and leave the tics and the word suggestion)
      - If you want to remove lines, write the preceding and trailing lines
      - Write a comment outside the tics, if you want, and use Preview to see the resulting `diff`
      - Press "Add Single Comment"
 - Once you're happy with the content, in the "Files changed" tab click "Review changes" -> "Approve"
 - Anyone can be a reviewer


### Making pull requests in the web GUI

In the master branch, navigate to the page you want to edit, click the pen-logo 
at the top right and once ready, at the bottom choose "Create new branch from this 
commit and start a pull request". Note, that you can give the branch a descriptive 
name at this point. If you wish to edit an already existing branch, first change to 
the correct branch in the "branch" button on upper left, next to the path to the 
file. If you found an error in the pull request of your own branch, you should commit 
to it directly instead of creating another pull request (the two choices at the bottom).

### Making pull requests on the command line

Overview:

 - Clone the reposity (if not done already) `git clone https://github.com/CSCfi/csc-env-eff`
 - Update local repository `git pull`
 - Change to master branch (if not already) `git checkout master` 
 - Make a new branch from the master branch `git checkout -b my-new-branch`
 - Work and commit in your new branch `emacs ...; git add file`
 - Commit your changes `git commit -m 'short description'`
 - Check status (all files committed etc.) `git status`
 - Push changes to github `git push origin my-new-branch`
 - Make a pull request to merge changes from your new branch into the develop branch (in the web guide)
 - Ask a person to review and merge the changes
