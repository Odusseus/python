# python
Repository for python programs

https://pythonexamples.org/
https://programminghistorian.org/
https://www.codecademy.com/catalog/language/python
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction

# VSCode config
.vscode \ settings.json

1. Pyton
2. Pytest
  * Config
  ```
   "python.testing.pytestArgs": [
    "mattest",
    "--cov-report",
    "xml:coverage/cov.xml",
    "--cov-report",
    "html:coverage",
    "--cov=mat"
  ],
  "python.testing.unittestEnabled": true,
  "python.testing.pytestEnabled": true,
  "python.testing.unittestArgs": [
    "-v",
    "-s",
    ".",
    "-p",
    "*_test.py"
  ]
  ```
3. Coverage Gutters (ryanluker)
