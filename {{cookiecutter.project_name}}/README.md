<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center"> {{cookiecutter.project_name}}</h3>

  <p align="center">
    {{cookiecutter.project_short_description}}
    <br />
    <a href="https://htmlpreview.github.io/?https://raw.githubusercontent.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/main/docs/api/{{cookiecutter.project_name}}/index.html"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://htmlpreview.github.io/?https://raw.githubusercontent.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/main/docs/pytest_report.html">Tests</a>
    ·
    <a href="https://htmlpreview.github.io/?https://raw.githubusercontent.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/main/docs/cov-report/index.html">Code Coverage</a>
    ·
    <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/issues">Report Bug</a>
    ·
    <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#uml-diagrams">UML Diagrams</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

{{cookiecutter.project_short_description}}

### UML Diagrams

#### Packages

  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/raw/main/docs/uml/diagrams/packages_new_package.png">
    <img src="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/raw/main/docs/uml/diagrams/packages_new_package.png" alt="uml-diagram-packages">
  </a>
  
---

#### Classes

  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/raw/main/docs/uml/diagrams/classes_new_package.png">
    <img src="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/raw/main/docs/uml/diagrams/classes_new_package.png" alt="uml-diagram-classes">
  </a>
  
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This Project depends on the following projects.
* poetry
  ```sh
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
  ```
  
* nox
  ```sh
  pip install --user --upgrade nox
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}
   cd {{cookiecutter.project_name}}
   ```
2. Install NPM packages
   ```sh
   poetry install
   ```
3. Run tests
   ```sh
   nox -s tests
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Some useful examples of how this project can be used:

*  Run tests
   ```sh
   nox -s tests
   ```
   
*  Run code lint
   ```sh
   nox -s lint
   ```
   
*  Generate API documentation
   ```sh
   nox -s api-docs
   ```
   
*  Run pre-commit checks
   ```sh
   nox -s pre-commit
   ```

_For more examples, please refer to the [Documentation](https://htmlpreview.github.io/?https://raw.githubusercontent.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/main/docs/api/{{cookiecutter.project_name}}/index.html)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add tests
- [x] Add code coverage
- [ ] Improve documentation
- [ ] Include more tests

See the [open issues](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the {{cookiecutter.license}} License. See [`LICENSE.txt`](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/LICENSE.txt) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

{{cookiecutter.full_name}} - [@{{cookiecutter.github_username}}](https://github.com/{{cookiecutter.github_username}}) - {{cookiecuter.email}}

Project Link: [https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Some great references to start from

* [Choose an Open Source License](https://choosealicense.com)

References and sources of inspiration

* [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
* [Best practices for Python projects in 2021](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/)
* [5 Pytest Best Practices for Writing Great Python Tests](https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.svg?style=for-the-badge
[contributors-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.svg?style=for-the-badge
[forks-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/network/members
[stars-shield]: https://img.shields.io/github/stars/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.svg?style=for-the-badge
[stars-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/stargazers
[issues-shield]: https://img.shields.io/github/issues/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.svg?style=for-the-badge
[issues-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/issues
[license-shield]: https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.svg?style=for-the-badge
[license-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/blob/master/LICENSE.txt

