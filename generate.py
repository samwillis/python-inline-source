import os, json, re

directory = os.path.dirname(os.path.realpath(__file__))

regex = '(:) ((((\w+)(\.))?(%s))|((")(%s)("))|((\')(%s)(\'))) (=) ([bBrRuU]?f?)("{3})'
#        ^      ^    ^     ^      ^  ^   ^     ^   ^   ^      ^   ^            ^
#        1      5    6     7      9  10  11    13  14  15     16  17           18

begin_captures = {
    "1": {"name": "punctuation.separator.colon.python"},
    "5": {"name": "source.python"},
    "6": {"name": "punctuation.separator.period.python"},
    "7": {"name": "meta.attribute.python"},
    "9": {"name": "string.quoted.single.python"},
    "10": {"name": "string.quoted.single.python"},
    "11": {"name": "string.quoted.single.python"},
    "13": {"name": "string.quoted.single.python"},
    "14": {"name": "string.quoted.single.python"},
    "15": {"name": "string.quoted.single.python"},
    "16": {"name": "keyword.operator.assignment.python"},
    "17": {"name": "storage.type.string.python"},
    "18": {"name": "string.quoted.multi.python"},
}


def make_vs_code_extension(languages):
    package_file_path = os.path.join(
        directory, "vscode-python-inline-source", "package.json"
    )
    readme_file_path = os.path.join(
        directory, "vscode-python-inline-source", "README.md"
    )
    add_supported_languages_to_readme(languages, readme_file_path)
    syntax_file_path = os.path.join(
        directory,
        "vscode-python-inline-source",
        "syntaxes",
        "python-inline-source.json",
    )
    with open(package_file_path, "r") as f:
        package = json.load(f)
    with open(syntax_file_path, "r") as f:
        syntax = json.load(f)
    embedded_languages = {}
    patterns = []
    for langname, options in languages.items():
        embedded_languages[options["contentName"]] = langname
        patterns.append(
            {
                "contentName": options["contentName"],
                "begin": regex % ((options["match"],) * 3),
                "beginCaptures": begin_captures,
                "end": '("{3})',
                "endCaptures": {"1": {"name": "string.quoted.multi.python"}},
                "patterns": [{"include": options["include"]}],
            }
        )
    package["contributes"]["grammars"][0]["embeddedLanguages"] = embedded_languages
    syntax["patterns"] = patterns
    with open(package_file_path, 'w') as f:
        json.dump(package, f, indent=4)
    with open(syntax_file_path, 'w') as f:
        json.dump(syntax, f, indent=4)


def make_python_types(languages):
    sourcetypes_file_path = os.path.join(
        directory, "python-sourcetypes", "sourcetypes.py"
    )
    readme_file_path = os.path.join(
        directory, "python-sourcetypes", "README.md"
    )
    add_supported_languages_to_readme(languages, readme_file_path)
    with open(sourcetypes_file_path, 'w') as f:
        f.writelines(
            [
                "from typing import Annotated\n",
                "\n",
                "source_code = Annotated[str, 'source_code']\n",
                "\n",
            ]
        )
        for langname, options in languages.items():
            f.write(f"{langname} = Annotated[source_code, '{langname}']\n")
            for alias in options["match"].split("|"):
                if alias != langname:
                    f.write(f"{alias} = {langname}\n")
            f.write("\n")


def add_supported_languages_to_readme(languages, readme_file_path):
    with open(readme_file_path, "r") as f:
        readme = f.read()
    readme_text = []
    for langname, options in languages.items():
        readme_text_line = f"\n- `{langname}`"
        aliases = [f"`{m}`" for m in options['match'].split("|") if m != langname]
        if aliases:
            if len(aliases) > 1:
                aliases[-1] = f"and {aliases[-1]}"
            readme_text_line = f"{readme_text_line} (aliased as {', '.join(aliases)})"
        readme_text.append(readme_text_line)
    readme = re.sub(r"(## Supported Languages\n)[^#]*", fr"\1{''.join(readme_text)}\n\n", readme)
    with open(readme_file_path, 'w') as f:
        f.write(readme)


def main():
    with open(os.path.join(directory, "languages.json"), "r") as f:
        languages = json.load(f)
    make_vs_code_extension(languages)
    make_python_types(languages)


if __name__ == "__main__":
    main()
