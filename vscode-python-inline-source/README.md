# Python Inline Source Syntax Highlighting

VS Code plugin to add syntax highlight to multi line Python strings using type 
annotations. Supports `html`, `css`, `javascript`, `typescript`, `sql`, `graphql`, 
multiple *css extension languages*, *template languages* and many more, 
[see below](#supported-languages) for a full list.

## Installation

Install `python-inline-source` from extensions (`ctrl + shift + x` or `cmd + shift + x` 
on mac).

Also available on [marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=samwillis.python-inline-source)

## Example

![Example](docs/examples.png)

## Usage

Use a type decoration named for language that you are using, the simplest for of this is
to do something like this:

```
html = str  # Create an alias of the str type named for the language you are using

my_html_string: html = """
  <h1>Some HTML</h1>
"""
```

In order to aid with the type decorations the `sourcetypes` package can be 
installed (`pip install sourcetypes`) which allows this for all supported 
languages:

```
import sourcetypes

my_html_string: sourcetypes.html = """
  <h1>Some HTML</h1>
"""
```

The `sourcetypes` package uses [typing.Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)
to annotate the `str` type with the language used. You can use 
[typing.get_type_hints](https://docs.python.org/3/library/typing.html#typing.get_type_hints) 
at runtime to determine the language that a string has been annotated with.

## Supported Languages

- `markdown` (aliased as `md`)
- `html`
- `django_html` (aliased as `django`)
- `django_txt`
- `jinja`
- `jinja_html`
- `css` (aliased as `style`, and `styles`)
- `scss`
- `less`
- `sass`
- `stylus`
- `javascript` (aliased as `js`)
- `jsx` (aliased as `javascriptreact`, and `react`)
- `typescript` (aliased as `ts`)
- `tsx` (aliased as `typescriptreact`)
- `coffeescript` (aliased as `coffee`)
- `sql`
- `json`
- `yaml`
- `graphql`
- `xml`
- `python`

## Requirements

- At least Visual Studio Code v1.64.0 recommended, not tested on older versions.

## Release Notes

### [0.0.2] - 2022-03-13
- Doc tweaks

### [0.0.1] - 2022-03-11
- Alpha release