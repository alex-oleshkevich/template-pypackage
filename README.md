[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python package.  
Based on [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).

## Features

-   Testing setup with `pytest`
-   Github actions for lining and publishing
-   `poetry` for dependency management
-   `black` for code formatting
-   `flake8` for code linting
-   `mypy` for type checking
-   `pre-commit` checking code before pushing

## Quick start

Install Cookiecutter if you haven't installed it yet.

```bash
pip install -U cookiecutter
```

Generate a Python package

```bash
cookiecutter https://github.com/alex-oleshkevich/template-pypackage.git
```

Then:

-   install dependencies `poetry install`
-   install pre-commit hooks `pre-commit install`
-   create [a PyPi token](https://pypi.org/manage/account/) for package uploads
-   setup a [Github action secret](https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository) named `PYPI_TOKEN`

## Releasing a package

If you want to release a package do:

-   bump a package version in `pyproject.toml` `poetry version 1.0.0`
-   commit changes `git add pyproject.toml` and `git commit pyproject.toml`
-   tag the release `git tag v1.0.0`
-   push changes `git push && git push --tags`
-   create a new [Github release](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release)

Once a release created, the `Publish` Github action will be triggered.
