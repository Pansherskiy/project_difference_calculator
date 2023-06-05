<h2 align='center'>Difference generator</h2>

---

<h3 align='center'>Hexlet tests and linter status:</h3>
<div style="text-align:center">
    <a href="https://github.com/Pansherskiy/project_difference_generator/actions/workflows/hexlet-check.yml"><img src="https://github.com/Pansherskiy/project_difference_generator/actions/workflows/hexlet-check.yml/badge.svg" alt="Actions Status"></a>
    <a href="https://github.com/Pansherskiy/project_difference_generator/actions/workflows/test-and-linter-check.yml"><img src="https://github.com/Pansherskiy/project_difference_generator/actions/workflows/test-and-linter-check.yml/badge.svg" alt="test-and-linter-check"></a>
</div>
<h3 align='center'>Сode quality and test coverage</h3>
<div style="text-align:center">
    <a href="https://codeclimate.com/github/Pansherskiy/project_difference_generator/maintainability"><img src="https://api.codeclimate.com/v1/badges/14c1326419db56c39355/maintainability" /></a>
    <a href="https://codeclimate.com/github/Pansherskiy/project_difference_generator/test_coverage"><img src="https://api.codeclimate.com/v1/badges/14c1326419db56c39355/test_coverage" /></a>
</div>

<h3 align='center'>Used technologies</h3>

<div style="text-align:center">
    <img src="https://img.shields.io/badge/Python-v3.10-blue?style=plastic&logo=python" alt="Python v3.10">
    <img src="https://img.shields.io/badge/flake8-v6.0.0-green?style=plastic&logo=flake8" alt="flake8 v6.0.0">
    <img src="https://img.shields.io/badge/Pyyaml-v6.0-blue?style=plastic&logo=Python" alt="Pyyaml v6.0">
</div>

<div style="text-align:center">
    <img src="https://img.shields.io/badge/Poetry-v1.3.2-blue?style=plastic&logo=poetry" alt="Poetry v1.3.2">
    <img src="https://img.shields.io/badge/Git-v2.34.1-red?style=plastic&logo=Git" alt="Git v2.34.1">
    <img src="https://img.shields.io/badge/Pytest-v7.3.1-blue?style=plastic&logo=Pytest" alt="Pytest v7.3.1">
</div>


---

Difference generator is a program that determines the 
difference between two JSON or YAML files. The input formats are
`.json`, `.yaml` or `.yml`, as a result of the program, you can get
differences in three formats: `stylish`(default), `plain`, `json`.

---

<h3 align='center'>Installing</h3>
1. Сlone the project to your local repository

`git clone git@github.com:Pansherskiy/project_difference_generator.git`

2. Go to the project folder `cd project_difference_generator` and run the commands:

* `make install` - will install the virtual environment and dependencies
* `make build` - will build the package before installation
* `make package-install` - install the package on the system

Now the program is ready to use

---

<h3 align='center'>Usage</h3>

Command `gendiff -h`
```commandline
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

---

<h3 align='center'>Examples</h3>

* Comparing JSON files:
[![asciicast](https://asciinema.org/a/589790.svg)](https://asciinema.org/a/589790)
* Comparing YAML files:
[![asciicast](https://asciinema.org/a/589799.svg)](https://asciinema.org/a/589799)
* Comparing nested JSON files:
[![asciicast](https://asciinema.org/a/589800.svg)](https://asciinema.org/a/589800)
* Comparing nested YAML files:
[![asciicast](https://asciinema.org/a/589802.svg)](https://asciinema.org/a/589802)
* Comparing JSON and YAML files:
[![asciicast](https://asciinema.org/a/589804.svg)](https://asciinema.org/a/589804)