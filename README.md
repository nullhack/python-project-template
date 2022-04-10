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

  <h1 align="center"> Cookiecutter Python Base Project</h3>

  <p align="center">
    Cookiecutter for Python template with some awesome tools to quickstart any Python project.
    <br />
    <a href="https://github.com/nullhack/cookiecutter-python-base-project/issues">Report Bug</a>
    ·
    <a href="https://github.com/nullhack/cookiecutter-python-base-project/issues">Request Feature</a>
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

Python template with some awesome tools to quickstart any Python project. 
It includes automatic generation of API documentation, tests using PyTest, code coverage, 
Flake8 linting to enforce standardized Python coding, automatic UML diagrams generation using PyReverse, 
virtual environments using Poetry, workflow automation using Nox, 
code formating using black and a standard Dockerfile to kickstart your project using the power of Docker containers and much more. 

All you need to do is to install [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/usage.html)!

---

<!-- GETTING STARTED -->
## Getting Started

### [Live Example](https://github.com/nullhack/python-base-project)

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
   cookiecutter https://github.com/nullhack/cookiecutter-python-base-project
   # move into your newly created project folder
   ```
2. Install nox
   ```sh
   pip install --user --upgrade nox
   ```
3. Let nox do it's magic
   ```sh
   nox
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Improve documentation

See the [open issues](https://github.com/nullhack/cookiecutter-python-base-project/issues) for a full list of proposed features (and known issues).

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

Distributed under the MIT License. See [`LICENSE.txt`](https://github.com/nullhack/cookiecutter-python-base-project/blob/master/LICENSE.txt) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Eric Lopes - [@nullhack](https://github.com/nullhack)

Project Link: [https://github.com/nullhack/cookiecutter-python-base-project/](https://github.com/nullhack/cookiecutter-python-base-project/)

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
[contributors-shield]: https://img.shields.io/github/contributors/nullhack/cookiecutter-python-base-project.svg?style=for-the-badge
[contributors-url]: https://github.com/nullhack/cookiecutter-python-base-project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nullhack/cookiecutter-python-base-project.svg?style=for-the-badge
[forks-url]: https://github.com/nullhack/cookiecutter-python-base-project/network/members
[stars-shield]: https://img.shields.io/github/stars/nullhack/cookiecutter-python-base-project.svg?style=for-the-badge
[stars-url]: https://github.com/nullhack/cookiecutter-python-base-project/stargazers
[issues-shield]: https://img.shields.io/github/issues/nullhack/cookiecutter-python-base-project.svg?style=for-the-badge
[issues-url]: https://github.com/nullhack/cookiecutter-python-base-project/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green?style=for-the-badge
[license-url]: https://github.com/nullhack/cookiecutter-python-base-project/blob/master/LICENSE.txt
