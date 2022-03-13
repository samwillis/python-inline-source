import sourcetypes
from sourcetypes import html, sql

test_html: html = """
  <html>
    <body>
      <h1>Inline syntax highlighting!</h1>
    </body>
  </html>
"""

test_sql: sql = """
    SELECT test
    FROM a_table
"""

test_css: sourcetypes.css = """
  body {
    font-weight: bold;
    color: #f00;
  }
"""

test_javascript: sourcetypes.javascript = """
  function() {
    var text = "Some Text";
    alert(text)
  }
"""

test_typescript: sourcetypes.ts = """
  function() {
    var text = "Some Text";
    alert(text)
  }
"""

test_jsx: sourcetypes.jsx = """
  function() {
    const element = <h1>Hello, world!</h1>;
    return element
  }
"""

test_tsx: sourcetypes.tsx = """
  function() {
    const element = <h1>Hello, world!</h1>;
    return element
  }
"""

test_python: sourcetypes.python = """
  test = "123"
  def my_function():
      return f"My string: {test}"
"""

test_sql2: sourcetypes.sql = """
    SELECT test
    FROM a_table
"""

test_html2: "html" = """
  <html>
    <body>
      <h1>Inline syntax highlighting</h1>
    </body>
  </html>
"""
