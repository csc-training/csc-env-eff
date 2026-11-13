---
layout: default
title: Managing your data during computing
parent: 3. Disk areas
grand_parent: Part 1
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/disk-areas/disk-areas-tutorial-data-management.html
---

# Managing your data during computing

> In this tutorial you
>
> - Learn why research data management matters while you compute, not only when you publish.
> - Organize and document a project folder on Roihu.
> - Use a checklist to decide what to keep, back up, remove and publish.

💬 Research data management (RDM) is easy to postpone until the end of a project, but most of the important decisions are made during the computing phase. This page collects the key practices. For a full introduction, see CSC's [self-study research data management course](https://csc.fi/en/training-calendar/cscs-self-study-research-data-management-course/).

## Plan before you compute

- A **Data Management Plan (DMP)** describes how data will be collected, stored, processed, documented, shared and preserved during a project. Many funders require one.
- A **Software Management Plan (SMP)** complements the DMP by describing how code, dependencies, versions and environments are managed.
- Planning early tells you which computing and storage services you need at different stages, how much space you need and for how long, and whether your data need a secure environment (_e.g._ [CSC Sensitive Data Services](https://docs.csc.fi/data/sensitive-data/)).

💡 When planning, consider:

- How will you document your work and create metadata (_e.g._ electronic notebooks, automatically generated metadata)?
- Which computing environments, tools and software will you use?
- How will you manage access rights?
- How will you ensure data quality?
- How will you handle version control and backups, and when will you remove data you no longer need?
- Where will data be stored after the analysis, and which versions will be shared or published?

## Organize and document a project folder

1. On Roihu, go to your own folder on `/scratch` and create a small example project:

   ```bash
   cd /scratch/<project>/$USER   # replace <project> with your CSC project, e.g. project_2001234
   mkdir -p my-analysis/{raw,processed,results,scripts}
   ```

2. Create a `README.md` in the project folder, _e.g._ with `nano my-analysis/README.md`, and fill in the template below:

   ```text
   # my-analysis

   Purpose:      What is this analysis for?
   Contact:      Name, email
   Created:      YYYY-MM-DD

   ## Folders
   raw/          Original input data. Never modified. Source: <where it came from>
   processed/    Intermediate files produced by scripts/. Can be regenerated.
   results/      Final outputs reported in papers or reports.
   scripts/      Code and batch job scripts used to produce processed/ and results/.

   ## Environment
   Software and versions (e.g. modules or containers used):

   ## Processing steps
   1. ...

   ## Backups
   Where are copies kept (e.g. Allas bucket name)? Who makes them and how often?
   ```

3. Compare the folders. Which of them would you need to back up? Which could you delete and regenerate if needed?

💡 `raw/`, `scripts/` and `results/` (plus the `README.md`) are worth backing up, _e.g._ to [Allas]({{ site.baseurl }}{% link part-1/allas/allas-backup.md %}). `processed/` can be regenerated from the raw data and scripts, so it is the first candidate for cleaning up, as long as the scripts and environment are documented.

☝🏻 Your batch job scripts are documentation too: keep them in version control together with the rest of your code, _e.g._ using Git and GitHub/GitLab.

## Find data to clean up

1. Use `csc-workspaces` to see how full your project's disk areas are.
2. Use `lue` to find out where most of your data and files are (see the [LUE tutorial]({{ site.baseurl }}{% link part-1/disk-areas/lue.md %})).
3. For the largest folders, ask:
   - Is this raw data, an intermediate file or a final result?
   - Is it a duplicate or an outdated version?
   - Could it be regenerated from raw data and code?
   - Is it backed up?

⚠️ Files on `/scratch` that have not been used for a while are [removed automatically](https://docs.csc.fi/computing/usage-policy/#disk-cleaning). Always keep raw data and everything needed to reproduce your results safely stored elsewhere, and write down what you removed and why.

## Reproducibility checklist

Go through these questions with your research group. The answers help you decide which data, code, models and documentation are worth saving and, if possible, publishing.

- Was any part of the analysis done by hand? If so, is it precisely documented, and does the documentation match what was actually done?
- Have we automated (coded) as much as possible?
- Are we using version control?
- Have we documented our software environment?
- Have we saved all output that cannot be reconstructed from the original data and code?
- How far back in the analysis pipeline can we go before the results are no longer (automatically) reproducible?
- Can the data and documentation be cited with a persistent identifier (PID)?

## Before you publish

- Choose the datasets needed to understand or reproduce your results (usually raw and final data, code and documentation, not temporary files).
- Provide metadata and documentation, and use open, long-term file formats where possible.
- Check legal, ethical and access restrictions. Data can be **as open as possible, as closed as necessary**.
- Publish in a trusted repository and get a persistent identifier (_e.g._ DOI). See [re3data.org](https://www.re3data.org/) and CSC's [Fairdata services](https://www.fairdata.fi).

## More information

- Docs CSC: [Data documentation and organization](https://docs.csc.fi/data/datasets/metadata-and-documentation/), [Publishing datasets](https://docs.csc.fi/data/datasets/publishing-datasets/), [Cleaning up data on scratch](https://docs.csc.fi/support/tutorials/clean-up-data/)
- RDMkit: [Metadata management](https://rdmkit.elixir-europe.org/metadata_management), [Data deletion](https://rdmkit.elixir-europe.org/data_deletion), [Your domain](https://rdmkit.elixir-europe.org/your_domain)
- [README file examples](https://data-guidelines.scilifelab.se/topics/readme-files/) (SciLifeLab)
- [CSC's self-study research data management course](https://csc.fi/en/training-calendar/cscs-self-study-research-data-management-course/)
