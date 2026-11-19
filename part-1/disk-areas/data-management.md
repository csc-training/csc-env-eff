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
> - Learn to integrate research data management into your data processing and analysis workflows.
> - Organize and document a project folder on Roihu.
> - Use a checklist to decide what to keep, back up, remove and publish.

💬 Research data management (RDM) should be considered throughout the research lifecycle, including the computing phase. Decisions related to data, software and computing environments affect the quality, reproducibility and long-term value of research outputs. This page collects the key practices. For a full introduction, see CSC's [self-study research data management course](https://csc.fi/en/training-calendar/cscs-self-study-research-data-management-course/).

## Plan before you compute

Planning early helps you identify the storage, computing resources and services needed at different stages of the project, estimate capacity requirements, use resources efficiently, and ensure that sensitive data are handled in appropriate environments.

- A **Data Management Plan (DMP)** supports planning for how data will be collected, processed, documented, stored and shared throughout a project. It helps identify resource needs, responsibilities and potential risks early on.
- A **Software Management Plan (SMP)** complements the DMP by helping researchers manage code, software, dependencies, versions and computing environments.


💡 When planning, consider:

- **Data, storage and computing needs:** what resources are needed and how much capacity will be required?
- **Computing environments, software and services:** which services will you use, how will you access them, are specialised environments needed for sensitive data (e.g. [CSC Sensitive Data Services](https://docs.csc.fi/data/sensitive-data/)), and are there any costs or quotas?
- **Security requirements and access rights:** who grants access and who can access the data and services?
- **Documentation and metadata:** how will others understand and reuse your work (e.g. metadata, codebooks and notebooks)?
- **Workflows and software environments:** how will others reproduce your analyses (e.g. workflow descriptions, software versions and dependencies)?
- **Version control, backups and data quality:** how will reliability be ensured, and who is responsible for versioning, backups and quality control?
- **Storage, sharing and publication:** what will be stored, where will it be shared or published, and what can be removed?


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

🏷️ Meaningful and consistent file names are part of good documentation. Use descriptive names that indicate the content, version or date of a file.

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

- Was any part of the analysis done by hand/manually? If so, is it precisely documented, and does the documentation match what was actually done?
- Have we automated (coded) as much of the workflow as possible?
- Are data, code and documentation under version control where appropriate?
- Have we documented software versions, dependencies and computing environments?
- Can another team member reproduce the analysis using the available data, code and documentation?
- Have we saved all output that cannot be reconstructed from the original data and code?
- How far back in the workflow can results still be reproduced automatically?
- Can the data, code and documentation be cited with a persistent identifier (PID)?

## Before you publish

- Choose the data, code and documentation needed to understand or reproduce your results. In most cases this includes raw data, final datasets, analysis code and documentation, but not temporary or intermediate files.
- Provide sufficient metadata and documentation so that others can understand and reuse the data and reproduce the analysis.
- Check legal, ethical and access restrictions. Data can be **as open as possible, as closed as necessary**.
- Choose an appropriate licence for data (e.g. Creative Commons) and code (e.g. MIT or Apache).
- Find a trusted repository, preferably a discipline-specific repository when available, that provides a persistent identifier (e.g. DOI). Find data repositories: [re3data.org](https://www.re3data.org/), see also [CSC's services](https://research.csc.fi/service/?need=publish-preserve-data), e.g [Fairdata services](https://www.fairdata.fi), [ELIXIR Deposition databases](https://elixir-europe.org/platforms/data/elixir-deposition-databases) (for life science research)

## More information

- Docs CSC: [Data documentation and organization](https://docs.csc.fi/data/datasets/metadata-and-documentation/), [Publishing datasets](https://docs.csc.fi/data/datasets/publishing-datasets/), [Cleaning up data on scratch](https://docs.csc.fi/support/tutorials/clean-up-data/)
- RDMkit: [Documentation & metadata management](https://rdmkit.elixir-europe.org/metadata_management), [Data deletion](https://rdmkit.elixir-europe.org/data_deletion), [Data organisation](https://rdmkit.elixir-europe.org/data_organisation), [Your domain](https://rdmkit.elixir-europe.org/your_domain)
- [README file examples](https://data-guidelines.scilifelab.se/topics/readme-files/) (SciLifeLab)
- [CSC's self-study research data management course](https://csc.fi/en/training-calendar/cscs-self-study-research-data-management-course/)
- [AI‑ready data and FAIR data management for industry](https://lumi-ai-factory.github.io/data_management/) 
