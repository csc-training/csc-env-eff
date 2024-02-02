# Content and formatting instructions

## General help

- For tutorials and exercises, please see this
  [Markdown syntax guide](https://www.markdownguide.org/tools/jekyll/) and this
  [Markdown example tutorial](example_tutorial.md).
- The csc-env-eff website uses the Just the Docs Jekyll theme,
  [see documentation here](https://just-the-docs.com/).
- For slides, see this
  [syntax guide](https://github.com/csc-training/slidefactory-template/blob/master/guide/syntax-guide.md)
  and this [Markdown example slide set](../_slides/example.md).
  - Please use the `csc-eurocc-2019` theme.
- When in doubt, check how other pages are formatted.

## Organizing content

- Try to make standalone slide stacks/hands-ons with a good name.
- The content should be as concise as possible, but as lengthy as needed.
- Link generously to [Docs CSC](https://docs.csc.fi) for additional
  information.
  - Some details can be introduced via tutorials/exercises.

## Accessibility

- [General guidelines](https://www.saavutettavuusvaatimukset.fi/).
- Make accessible content! In short:
  - `[Read more here](/link/to/some/page)` is not accessible.
    `[Read more about free use cases](/link/to/some/page)` is better.
  - Avoid long walls of text and long sentences.
  - Lists and clear titles: good!
  - Use descriptive alt-texts for images and videos.
  - Avoid presenting something ONLY as a video and use captions/subtitles.
    Also, do present important or difficult-to-follow things with videos.
  - Avoid using loadable PDFs.
  - Avoid using only color to signal some meaning.

## Images, linked documents

- Put all images used in slides under `_slides/img` folder.
  - Images for tutorials/exercises can have their own `/img` folders in their
    respective directories, e.g. `/part-1/prerequisites/img`.
- Put large files in Allas (write-access with project 2001659), bucket
  **CSC_training**.
  - New files easy to share with `a-publish your-file.tgz -b CSC_training` and
    then access at `https://a3s.fi/CSC_training/your-file.tgz`.
  - Existing files can be updated (overwritten) with
    `a-put -b CSC_training --override your-file.tgz`.

## Syntax highlighting

- Write Slurm flags in long format, e.g. `--nodes` instead of `-N`, etc.
- All examples should use minimum viable reserved resources. Don't write
  examples with `--time=72:00:00`, `--gres=gpu:v100:4`, `--cpus-per-task=40`
  unless explicitly needed. Users tend to use these as default values.
- Internal links as `[cool page](page.md)`, `[stuff in page](page.md#anchor)`,
  `[stuff in other section](../other_section/page.md)`,
  `[stuff elsewhere](../other_section/page.md#anchor)` (avoid _internal_ links
  with `https://...`).
- For code blocks (marked with three backticks), specify the language
  explicitly, e.g. ` ```bash` or ` ```python`.
- If you don't want any syntax highlighting, just use ` ```text`.
- For a list of all supported languages, see
  <https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers>.
- Give commands, environment variables, command options, as well as partition 
  names between two backticks, i.e. `srun`, `$LOCAL_SCRATCH`, `--gres`,
  `small`.

## Terminology

- When referring collectively to compute servers, use term
  "CSC supercomputers". Puhti and Mahti (or LUMI) should be used explicitly
  only when needed.
