<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/write.svg?longCache=True)](https://pypi.org/project/write/)
[![](https://img.shields.io/pypi/v/write.svg?maxAge=3600)](https://pypi.org/project/write/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/write.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/write.py/)

#### Installation
```bash
$ [sudo] pip install write
```

#### Functions
function|`__doc__`
-|-
`write.write(path, content)` |write content to file. Creates directory if it doesn't exist

#### Examples
```python
>>> import write

>>> write.write("not-existing-folder/file",'string')
>>> open("not-existing-folder/file").read()
'string'
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>