# sparv-sbx-sentiment-analysis

Sparv Plugins to perform sentiment analysis as annotations

[![CI(check)](https://github.com/spraakbanken/sparv-sbx-sentiment-analysis/actions/workflows/check.yml/badge.svg)](https://github.com/spraakbanken/sparv-sbx-sentiment-analysis/actions/workflows/check.yml)
[![CI(test)](https://github.com/spraakbanken/sparv-sbx-sentiment-analysis/actions/workflows/test.yml/badge.svg)](https://github.com/spraakbanken/sparv-sbx-sentiment-analysis/actions/workflows/test.yml)
[![CI(scheduled)](https://github.com/spraakbanken/sparv-sbx-sentiment-analysis/actions/workflows/scheduled.yml/badge.svg)](https://github.com/spraakbanken/sparv-sbx-sentiment-analysis/actions/workflows/scheduled.yml)
[![Codecov](https://codecov.io/gh/spraakbanken/sparv-sbx-sentiment-analysis/coverage.svg)](https://codecov.io/gh/spraakbanken/sparv-sbx-sentiment-analysis)

This repo contains the following projects:

- [sparv-sbx-sentence-sentiment-kb-sent](./sparv-sbx-sentence-sentiment-kb-sent/) [![PyPI version](https://badge.fury.io/py/sparv-sbx-sentence-sentiment-kb-sent.svg)](https://pypi.org/project/sparv-sbx-sentence-sentiment-kb-sent)

## Development

### Development prerequisites

- [`uv`](https://docs.astral.sh/uv/)
- [`pre-commit`](https://pre-commit.org)

For starting to develop on this repository:

- Clone the repo (in one of the ways below): (in one of the ways below):
  - `git clone git@github.com:spraakbanken/sparv-sbx-sentiment-analysis.git`
  - `git clone https://github.com/spraakbanken/sparv-sbx-sentiment-analysis.git`
- Setup environment: `make dev`
- Install `pre-commit` hooks: `pre-commit install`

Do your work.

Tasks to do:

- Test the code with `make test` or `make test-w-coverage`.
- Lint the code with `make lint`.
- Check formatting with `make check-fmt`.
- Format the code with `make fmt`.
- Type-check the code with `make type-check`.
- Test the examples with:
  - `make test-example-small-txt`
  - `make test-example-issue-10`

This repo uses [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).

### Release a new version

#### sparv-sbx-sentence-sentiment-kb-sent

- Prepare the CHANGELOG: `make sparv-sbx-sentence-sentiment-kb-sent/CHANGELOG.md`.
- Edit `CHANGELOG.md` to your liking.
- Add to git: `git add --update`
- Commit with `git commit -m 'chore(release): prepare release'` or `cog commit chore 'prepare release' release`.
- Bump version (depends on [`bump-my-version](https://callowayproject.github.io/bump-my-version/))
  - First `cd sparv-sbx-sentence-sentiment-kb-sent`
  - Major: `make bumpversion part=major`
  - Minor: `make bumpversion part=minor`
  - Patch: `make bumpversion part=patch` or `make bumpversion`
  - Go back to repo root `cd -`
- Push `main` and tags to GitHub: `git push main --tags` or `make publish`
  - GitHub Actions will build, test and publish the package to [PyPi](https://pypi.prg).
- Add metadata for [Språkbanken's resource](https://spraakbanken.gu.se/resurser)
  - Generate metadata: `make generate-metadata`
  - Upload the files from `assets/metadata/export/sbx_metadata/utility` to <https://github.com/spraakbanken/metadata/tree/main/yaml/utility>.
