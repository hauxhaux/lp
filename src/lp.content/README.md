<div align="center">
    <h1 align="center">lp.content</h1>
</div>
<div align="center">
[![PyPI](https://img.shields.io/pypi/v/lp.content)](https://pypi.org/project/lp.content/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lp.content)](https://pypi.org/project/lp.content/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/lp.content)](https://pypi.org/project/lp.content/)
[![PyPI - License](https://img.shields.io/pypi/l/lp.content)](https://pypi.org/project/lp.content/)
[![PyPI - Status](https://img.shields.io/pypi/status/lp.content)](https://pypi.org/project/lp.content/)


[![PyPI - Plone Versions](https://img.shields.io/pypi/frameworkversions/plone/lp.content)](https://pypi.org/project/lp.content/)

[![CI](https://github.com/hauxhaux/lp.content/actions/workflows/main.yml/badge.svg)](https://github.com/hauxhaux/lp.content/actions/workflows/main.yml)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000)

[![GitHub contributors](https://img.shields.io/github/contributors/hauxhaux/lp.content)](https://github.com/hauxhaux/lp.content)
[![GitHub Repo stars](https://img.shields.io/github/stars/hauxhaux/lp.content?style=social)](https://github.com/hauxhaux/lp.content)

</div>

A new addon for Plone

## Features

TODO: List our awesome features

## Installation

Install lp.content with `pip`:

```shell
pip install lp.content
```

And to create the Plone site:

```shell
make create-site
```

## Contribute

- [Issue tracker](https://github.com/hauxhaux/lp.content/issues)
- [Source code](https://github.com/hauxhaux/lp.content/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:hauxhaux/lp.content.git
    cd lp.content
    ```

2.  Install this code base.

    ```shell
    make install
    ```


### Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

```{seealso}
You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.
```

## License

The project is licensed under GPLv2.

## Credits and acknowledgements 🙏

Generated using [Cookieplone (1.0.0)](https://github.com/plone/cookieplone) and [cookieplone-templates (ca9ba9f)](https://github.com/plone/cookieplone-templates/commit/ca9ba9fa67bc9a824eab13962a63db230c93679e) on 2026-03-18 17:59:09.780060. A special thanks to all contributors and supporters!
