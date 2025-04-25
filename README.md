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

  <h1 align="center"> Python Project Template</h3>

  <p align="center">
    Cookiecutter for Python template with some awesome tools to quickstart any Python project.
    <br />
    <a href="https://github.com/nullhack/python-project-template/issues">Report Bug</a>
    ·
    <a href="https://github.com/nullhack/python-project-template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Python template with some awesome tools to quickstart a Python project with the industry best practices. 
It includes automatic generation of API documentation, tests using PyTest, code coverage, 
ruff linting to enforce standardized Python coding and formatting, virtual environments using uv, workflow automation using Taskipy and a space optimized Dockerfile to kickstart your project and run tests using the power of Docker containers. 

You only need to install [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/usage.html)!

---

<!-- GETTING STARTED -->
## Getting Started

### [Live Example](https://nullhack.github.io/python-project-template/)

To get a local copy up and running follow these simple steps.

### Prerequisites

This Project depends on the following projects.
* cookiecutter
  ```sh
  pip install --user --upgrade cookiecutter
  ```

### Installation

1. Replicate the template locally
   ```sh
   cookiecutter https://github.com/nullhack/python-project-template
   # move into your newly created project folder
   ```
2. Install uv and Taskipy
   ```sh
   pip install --user --upgrade uv
   ```
3. Let Taskipy do it's magic
   ```sh
   uv venv
   uv pip install .[dev]
   uv task test
   uv task run
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [X] Update packages and look for new industry standards to include
- [ ] Automatically deploy new documentation on new PR merged
- [ ] Make the github actions and gitea actions run without errors

See the [open issues](https://github.com/nullhack/python-project-template/issues) for a full list of proposed features (and known issues).

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

Distributed under the MIT License. See [`LICENSE`](https://github.com/nullhack/python-project-template/blob/main/LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

eol - [@nullhack](https://github.com/nullhack)

Project Link: [https://github.com/nullhack/python-project-template/](https://github.com/nullhack/python-project-template/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments and thanks

This project was heavily based on some great references.

* [Choose an Open Source License](https://choosealicense.com)
* [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
* [Best practices for Python projects in 2021](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/)
* [5 Pytest Best Practices for Writing Great Python Tests](https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Beyond Hypermodern: Python is easy now (2024)](https://rdrn.me/postmodern-python/)
* [Pytest Best Practices](https://pytest-with-eric.com/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/nullhack/python-project-template.svg?style=for-the-badge
[contributors-url]: https://github.com/nullhack/python-project-template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nullhack/python-project-template.svg?style=for-the-badge
[forks-url]: https://github.com/nullhack/python-project-template/network/members
[stars-shield]: https://img.shields.io/github/stars/nullhack/python-project-template.svg?style=for-the-badge
[stars-url]: https://github.com/nullhack/python-project-template/stargazers
[issues-shield]: https://img.shields.io/github/issues/nullhack/python-project-template.svg?style=for-the-badge
[issues-url]: https://github.com/nullhack/python-project-template/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green?style=for-the-badge
[license-url]: https://github.com/nullhack/python-project-template/blob/main/LICENSE.txt
