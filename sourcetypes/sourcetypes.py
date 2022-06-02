try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

source_code = Annotated[str, 'source_code']

markdown = Annotated[source_code, 'markdown']
md = markdown

html = Annotated[source_code, 'html']

django_html = Annotated[source_code, 'django_html']
django = django_html

django_txt = Annotated[source_code, 'django_txt']

jinja = Annotated[source_code, 'jinja']

jinja_html = Annotated[source_code, 'jinja_html']

css = Annotated[source_code, 'css']
style = css
styles = css

scss = Annotated[source_code, 'scss']

less = Annotated[source_code, 'less']

sass = Annotated[source_code, 'sass']

stylus = Annotated[source_code, 'stylus']

javascript = Annotated[source_code, 'javascript']
js = javascript

jsx = Annotated[source_code, 'jsx']
javascriptreact = jsx
react = jsx

typescript = Annotated[source_code, 'typescript']
ts = typescript

tsx = Annotated[source_code, 'tsx']
typescriptreact = tsx

coffeescript = Annotated[source_code, 'coffeescript']
coffee = coffeescript

sql = Annotated[source_code, 'sql']

json = Annotated[source_code, 'json']

yaml = Annotated[source_code, 'yaml']

graphql = Annotated[source_code, 'graphql']

xml = Annotated[source_code, 'xml']

python = Annotated[source_code, 'python']

