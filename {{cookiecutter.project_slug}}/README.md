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
    <a href="https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_slug}}/readme.html"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/issues">Report Bug</a>
    ·
    <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/issues">Request Feature</a>
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

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To run this project locally, you will need to install the prerequisites and follow the installation section.

### Prerequisites

This Project depends on the following projects.
* UV
  ```sh
  pip install --user --upgrade uv
  ```

* Taskipy
  ```sh
  pip install --user --upgrade taskipy
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
   cd {{cookiecutter.project_slug}}
   ```
2. Install UV and taskipy
   ```sh
   pip install --user --upgrade uv taskipy
   ```
3. Install requirements for development
   ```sh
   uv pip install '.[dev]'
   ```
4. Run tests
   ```sh
   uv run task test
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Some useful examples of how this project can be used:

*  Install requirements
   ```sh
   uv run task '.[dev]'
   ```

*  Run tests
   ```sh
   uv run task test
   ```

*  Run the project
   ```sh
   uv run main.py
   ```

*  Generate API documentation
   ```sh
   uv run task doc-html
   ```

*  Build a docker image for tests
   ```sh
   docker build --target test -t {{cookiecutter.package_name}}:test
   docker run -ti --rm {{cookiecutter.package_name}}:test
   ```

*  Build a docker image to run the root files only without running any test
   ```sh
   docker build --target prod -t {{cookiecutter.package_name}}:prod
   docker run -ti --rm {{cookiecutter.package_name}}:prod
   ```
   

_For more examples, please refer to the [Documentation](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_slug}}/readme.html)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add tests
- [x] Add code coverage
- [x] Improve documentation
- [ ] Watch for new best standards

See the [open issues](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/issues) for a full list of proposed features (and known issues).

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


<!-- CONTACT -->
## Contact

{{cookiecutter.full_name}} - [@{{cookiecutter.github_username}}](https://github.com/{{cookiecutter.github_username}}) - {{cookiecutter.email}}

Project Link: [https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This project was created using cookiecutter and Nullhack's python-project-template:

* [NullHack's python-project-template](https://github.com/nullhack/python-project-template/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the {{cookiecutter.license}} License. See [`LICENSE`](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/blob/main/LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?style=for-the-badge
[contributors-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?style=for-the-badge
[forks-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/network/members
[stars-shield]: https://img.shields.io/github/stars/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?style=for-the-badge
[stars-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/stargazers
[issues-shield]: https://img.shields.io/github/issues/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?style=for-the-badge
[issues-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/issues
[license-shield]: https://img.shields.io/badge/license-{{cookiecutter.license}}-green?style=for-the-badge
[license-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/blob/main/LICENSE

